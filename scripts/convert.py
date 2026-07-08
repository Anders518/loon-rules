#!/usr/bin/env python3
"""Convert Accademia/Additional_Rule_For_Clash YAML rule-providers to Loon .list files.

Generated layout:

rules/
  README.md
  Gemini/
    README.md
    Gemini_Domain.list

The script keeps conversion conservative and generates usage docs for Loon Remote Rule.
"""

from __future__ import annotations

import ipaddress
import os
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import requests
import yaml

UPSTREAM_OWNER = "Accademia"
UPSTREAM_REPO = "Additional_Rule_For_Clash"
UPSTREAM_BRANCH = "main"
UPSTREAM_API_ROOT = f"https://api.github.com/repos/{UPSTREAM_OWNER}/{UPSTREAM_REPO}/contents"
UPSTREAM_RAW_ROOT = f"https://raw.githubusercontent.com/{UPSTREAM_OWNER}/{UPSTREAM_REPO}/{UPSTREAM_BRANCH}"
REPO_RAW_ROOT = "https://raw.githubusercontent.com/Anders518/loon-rules/main"

OUT_DIR = Path("rules")
BUILD_DIR = Path("build")
DEFAULT_POLICY = "AI"
REQUEST_RETRIES = 3

SUPPORTED_CLASSICAL = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "DOMAIN-REGEX",
    "IP-CIDR",
    "IP-CIDR6",
    "GEOIP",
    "USER-AGENT",
    "URL-REGEX",
    "DST-PORT",
    "SRC-IP-CIDR",
}

DOMAIN_RE = re.compile(r"^(?:[A-Za-z0-9_-]+\.)+[A-Za-z0-9_-]+$", re.ASCII)


@dataclass
class ConvertResult:
    category: str
    name: str
    source_path: str
    source_url: str
    output_path: Path
    rules: list[str] = field(default_factory=list)
    skipped: dict[str, int] = field(default_factory=dict)

    @property
    def raw_url(self) -> str:
        return f"{REPO_RAW_ROOT}/{self.output_path.as_posix()}"

    @property
    def loon_tag(self) -> str:
        return self.name.replace("_", " ")

    @property
    def loon_remote_rule(self) -> str:
        return f"{self.raw_url}, policy={DEFAULT_POLICY}, tag={self.loon_tag}, enabled=true"


def github_headers(*, api: bool = False) -> dict[str, str]:
    headers = {"User-Agent": "Anders518-loon-rules-sync"}
    if api:
        headers["Accept"] = "application/vnd.github+json"
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get_with_retries(url: str, *, api: bool = False) -> requests.Response:
    last_exc: Exception | None = None
    for attempt in range(1, REQUEST_RETRIES + 1):
        try:
            response = requests.get(url, headers=github_headers(api=api), timeout=30)
            response.raise_for_status()
            return response
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            if attempt < REQUEST_RETRIES:
                time.sleep(2 * attempt)
    assert last_exc is not None
    raise last_exc


def request_json(url: str) -> Any:
    return get_with_retries(url, api=True).json()


def discover_yaml_files(path: str = "") -> list[str]:
    url = f"{UPSTREAM_API_ROOT}/{path}?ref={UPSTREAM_BRANCH}" if path else f"{UPSTREAM_API_ROOT}?ref={UPSTREAM_BRANCH}"
    entries = request_json(url)
    files: list[str] = []

    for entry in entries:
        entry_type = entry.get("type")
        entry_path = entry.get("path", "")
        name = entry.get("name", "")

        if entry_type == "dir":
            files.extend(discover_yaml_files(entry_path))
        elif entry_type == "file" and name.endswith((".yaml", ".yml")):
            files.append(entry_path)

    return sorted(files)


def load_payload(source_url: str) -> list[Any]:
    response = get_with_retries(source_url)
    data = yaml.safe_load(response.text)

    if isinstance(data, dict) and isinstance(data.get("payload"), list):
        return data["payload"]

    if isinstance(data, list):
        return data

    return []


def source_category(source_path: str) -> str:
    path = Path(source_path)
    if len(path.parts) > 1:
        return path.parts[0]
    return "Misc"


def source_path_to_output_path(source_path: str) -> Path:
    path = Path(source_path)
    category = source_category(source_path)
    return OUT_DIR / category / f"{path.stem}.list"


def is_plain_domain(value: str) -> bool:
    if ":" in value or "/" in value or "*" in value:
        return False
    return bool(DOMAIN_RE.fullmatch(value))


def normalize_classical(parts: list[str]) -> str | None:
    rule_type = parts[0].strip().upper()
    if rule_type not in SUPPORTED_CLASSICAL:
        return None

    normalized = [rule_type] + [part.strip() for part in parts[1:] if part.strip()]
    if len(normalized) < 2:
        return None

    return ",".join(normalized)


def normalize_rule(item: Any) -> tuple[str | None, str | None]:
    value = str(item).strip().strip("'\"")

    if not value or value.startswith("#"):
        return None, "empty_or_comment"

    if value.startswith("+."):
        domain = value[2:].strip().strip(".")
        if domain and is_plain_domain(domain):
            return f"DOMAIN-SUFFIX,{domain}", None
        return None, "invalid_domain_suffix"

    try:
        network = ipaddress.ip_network(value, strict=False)
        rule_type = "IP-CIDR6" if network.version == 6 else "IP-CIDR"
        return f"{rule_type},{network.with_prefixlen},no-resolve", None
    except ValueError:
        pass

    if is_plain_domain(value):
        return f"DOMAIN,{value}", None

    if "," in value:
        parts = value.split(",")
        classical = normalize_classical(parts)
        if classical:
            return classical, None
        return None, parts[0].strip().upper() or "unsupported_classical"

    return None, "unsupported_item"


def convert_one(source_path: str) -> ConvertResult:
    source_url = f"{UPSTREAM_RAW_ROOT}/{source_path}"
    output_path = source_path_to_output_path(source_path)
    category = source_category(source_path)
    name = output_path.stem

    result = ConvertResult(
        category=category,
        name=name,
        source_path=source_path,
        source_url=source_url,
        output_path=output_path,
    )

    payload = load_payload(source_url)
    seen: set[str] = set()

    for item in payload:
        rule, skipped_reason = normalize_rule(item)
        if rule:
            if rule not in seen:
                seen.add(rule)
                result.rules.append(rule)
        else:
            reason = skipped_reason or "unknown"
            result.skipped[reason] = result.skipped.get(reason, 0) + 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.write(f"# Name: {result.name}\n")
        f.write(f"# Category: {result.category}\n")
        f.write(f"# Source: {source_url}\n")
        f.write("# Converted for Loon. Auto-generated; do not edit manually.\n\n")
        f.write("\n".join(result.rules))
        f.write("\n")

    return result


def group_by_category(results: list[ConvertResult]) -> dict[str, list[ConvertResult]]:
    grouped: dict[str, list[ConvertResult]] = {}
    for result in results:
        grouped.setdefault(result.category, []).append(result)
    return {key: sorted(value, key=lambda item: item.name) for key, value in sorted(grouped.items())}


def write_rules_index(results: list[ConvertResult]) -> None:
    grouped = group_by_category(results)
    index_path = OUT_DIR / "README.md"

    with index_path.open("w", encoding="utf-8") as f:
        f.write("# Loon Rules Index\n\n")
        f.write("规则按上游目录分类保存。每个分类目录都有自己的 `README.md` 和 Loon 引用示例。\n\n")
        f.write("默认示例使用 `policy=AI`，请改成你自己 Loon 配置里的策略组名。\n\n")
        f.write("## 分类\n\n")
        f.write("| 分类 | 规则数 | 目录 |\n")
        f.write("| --- | ---: | --- |\n")
        for category, items in grouped.items():
            f.write(f"| `{category}` | {len(items)} | [`rules/{category}/`](./{category}/) |\n")

        f.write("\n## 常用示例\n\n")
        preferred = ["Gemini", "OpenAI", "Claude", "Copilot"]
        for category in preferred:
            if category not in grouped:
                continue
            f.write(f"### {category}\n\n")
            f.write("```ini\n[Remote Rule]\n")
            for item in grouped[category]:
                f.write(f"{item.loon_remote_rule}\n")
            f.write("```\n\n")


def write_category_readmes(results: list[ConvertResult]) -> None:
    grouped = group_by_category(results)

    for category, items in grouped.items():
        readme_path = OUT_DIR / category / "README.md"
        with readme_path.open("w", encoding="utf-8") as f:
            f.write(f"# {category}\n\n")
            f.write(f"本目录由上游 `{category}/` 目录自动转换生成。\n\n")
            f.write("## 文件\n\n")
            f.write("| 文件 | 规则数 | 上游源文件 |\n")
            f.write("| --- | ---: | --- |\n")
            for item in items:
                f.write(f"| [`{item.output_path.name}`](./{item.output_path.name}) | {len(item.rules)} | `{item.source_path}` |\n")

            f.write("\n## Loon Remote Rule 示例\n\n")
            f.write("把 `policy=AI` 改成你的实际策略组名。\n\n")
            f.write("```ini\n[Remote Rule]\n")
            for item in items:
                f.write(f"{item.loon_remote_rule}\n")
            f.write("```\n")


def write_summary(results: list[ConvertResult], failed: list[tuple[str, str]]) -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = BUILD_DIR / "summary.md"

    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Conversion Summary\n\n")
        f.write(f"Upstream: `{UPSTREAM_OWNER}/{UPSTREAM_REPO}`\n\n")
        f.write("| Category | Output | Rules | Source | Skipped |\n")
        f.write("| --- | --- | ---: | --- | ---: |\n")

        for result in sorted(results, key=lambda r: str(r.output_path)):
            skipped_total = sum(result.skipped.values())
            f.write(
                f"| `{result.category}` | `{result.output_path}` | {len(result.rules)} | "
                f"`{result.source_path}` | {skipped_total} |\n"
            )

        f.write("\n## Skipped Details\n\n")
        for result in sorted(results, key=lambda r: str(r.output_path)):
            if not result.skipped:
                continue
            f.write(f"### `{result.output_path}`\n\n")
            for reason, count in sorted(result.skipped.items()):
                f.write(f"- `{reason}`: {count}\n")
            f.write("\n")

        if failed:
            f.write("\n## Failed Upstream Files\n\n")
            f.write("These files failed to convert during this run. Existing successful outputs are still published.\n\n")
            for source_path, error in failed:
                f.write(f"- `{source_path}`: `{error}`\n")


def main() -> int:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        source_paths = discover_yaml_files()
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to discover upstream YAML files: {exc}", file=sys.stderr)
        return 1

    if not source_paths:
        print("No YAML files discovered from upstream.", file=sys.stderr)
        return 1

    results: list[ConvertResult] = []
    failed: list[tuple[str, str]] = []

    for source_path in source_paths:
        try:
            result = convert_one(source_path)
            results.append(result)
            print(f"Generated {result.output_path}: {len(result.rules)} rules")
        except Exception as exc:  # noqa: BLE001
            failed.append((source_path, str(exc)))
            print(f"Failed {source_path}: {exc}", file=sys.stderr)

    if not results:
        print("No rules were converted successfully.", file=sys.stderr)
        if failed:
            print("\nAll attempted files failed:", file=sys.stderr)
            for source_path, error in failed:
                print(f"- {source_path}: {error}", file=sys.stderr)
        return 1

    write_rules_index(results)
    write_category_readmes(results)
    write_summary(results, failed)

    if failed:
        print("\nSome upstream files failed to convert; continuing because successful outputs exist.", file=sys.stderr)
        for source_path, error in failed:
            print(f"- {source_path}: {error}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
