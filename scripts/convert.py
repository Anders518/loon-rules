#!/usr/bin/env python3
"""Convert Accademia/Additional_Rule_For_Clash rule-provider YAML files to Loon .list rules.

This script intentionally keeps conversion conservative:
- Mihomo/Clash domain behavior items such as '+.example.com' become 'DOMAIN-SUFFIX,example.com'.
- Plain domain behavior items such as 'example.com' become 'DOMAIN,example.com'.
- Classical rules already using Loon-compatible rule types are kept as-is after whitespace normalization.
- Unsupported rule types are skipped and summarized in build/summary.md.
"""

from __future__ import annotations

import ipaddress
import os
import re
import sys
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

OUT_DIR = Path("rules")
BUILD_DIR = Path("build")

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
    name: str
    source_path: str
    source_url: str
    output_path: Path
    rules: list[str] = field(default_factory=list)
    skipped: dict[str, int] = field(default_factory=dict)


def request_json(url: str) -> Any:
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def discover_yaml_files(path: str = "") -> list[str]:
    url = f"{UPSTREAM_API_ROOT}/{path}" if path else UPSTREAM_API_ROOT
    if path:
        url += f"?ref={UPSTREAM_BRANCH}"
    else:
        url += f"?ref={UPSTREAM_BRANCH}"

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
    response = requests.get(source_url, timeout=30)
    response.raise_for_status()
    data = yaml.safe_load(response.text)

    if isinstance(data, dict) and isinstance(data.get("payload"), list):
        return data["payload"]

    if isinstance(data, list):
        return data

    return []


def source_path_to_output_name(source_path: str) -> str:
    # Example: Gemini/Gemini_Domain.yaml -> Gemini_Domain.list
    stem = Path(source_path).stem
    parent = Path(source_path).parent.name

    if parent and parent != "." and not stem.startswith(parent):
        return f"{parent}_{stem}.list"
    return f"{stem}.list"


def is_plain_domain(value: str) -> bool:
    if ":" in value or "/" in value or "*" in value:
        return False
    return bool(DOMAIN_RE.fullmatch(value))


def normalize_classical(parts: list[str]) -> str | None:
    rule_type = parts[0].strip().upper()
    if rule_type not in SUPPORTED_CLASSICAL:
        return None

    # Keep no-resolve and other trailing options when present.
    normalized = [rule_type] + [part.strip() for part in parts[1:] if part.strip()]

    if len(normalized) < 2 and rule_type not in {"FINAL"}:
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

    # Domain behavior can contain bare IP/CIDR entries in some upstream files.
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
    output_name = source_path_to_output_name(source_path)
    output_path = OUT_DIR / output_name
    result = ConvertResult(
        name=output_name.removesuffix(".list"),
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
        f.write(f"# Source: {source_url}\n")
        f.write("# Converted for Loon. Auto-generated; do not edit manually.\n\n")
        f.write("\n".join(result.rules))
        f.write("\n")

    return result


def write_summary(results: list[ConvertResult]) -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = BUILD_DIR / "summary.md"

    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Conversion Summary\n\n")
        f.write(f"Upstream: `{UPSTREAM_OWNER}/{UPSTREAM_REPO}`\n\n")
        f.write("| Output | Rules | Source | Skipped |\n")
        f.write("| --- | ---: | --- | ---: |\n")

        for result in sorted(results, key=lambda r: str(r.output_path)):
            skipped_total = sum(result.skipped.values())
            f.write(
                f"| `{result.output_path}` | {len(result.rules)} | "
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


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Remove stale generated lists so deleted/renamed upstream files do not linger.
    for old_file in OUT_DIR.glob("*.list"):
        old_file.unlink()

    source_paths = discover_yaml_files()
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
        except Exception as exc:  # noqa: BLE001 - keep CI summary useful.
            failed.append((source_path, str(exc)))
            print(f"Failed {source_path}: {exc}", file=sys.stderr)

    write_summary(results)

    if failed:
        print("\nSome files failed to convert:", file=sys.stderr)
        for source_path, error in failed:
            print(f"- {source_path}: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
