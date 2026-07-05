#!/usr/bin/env python3
"""Render Loon templates with centralized YAML variables."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

PLACEHOLDER_RE = re.compile(r"<([A-Z0-9_]+)>")


def value_to_string(value: Any, key: str) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        sep = "\n" if key.endswith("_LINES") else ","
        return sep.join(str(item) for item in value)
    return str(value)


def flatten(data: dict[str, Any], prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in data.items():
        normalized_key = f"{prefix}_{key}" if prefix else str(key)
        normalized_key = normalized_key.upper()
        if isinstance(value, dict):
            result.update(flatten(value, normalized_key))
        else:
            result[normalized_key] = value_to_string(value, normalized_key)
    return result


def add_aliases(values: dict[str, str]) -> dict[str, str]:
    aliases = dict(values)
    alias_map = {
        "PRIMARY": "SUBSCRIPTION_PRIMARY_NAME",
        "PRIMARY_NAMES": "SUBSCRIPTION_PRIMARY_NAMES",
        "PRIMARY_PROXY_LINES": "SUBSCRIPTION_PRIMARY_PROXY_LINES",
        "BACKUP": "SUBSCRIPTION_BACKUP_NAME",
        "BACKUP_NAMES": "SUBSCRIPTION_BACKUP_NAMES",
        "BACKUP_PROXY_LINES": "SUBSCRIPTION_BACKUP_PROXY_LINES",
        "SUBSCRIPTION_URL_PRIMARY": "SUBSCRIPTION_PRIMARY_URL",
        "SUBSCRIPTION_URL_BACKUP": "SUBSCRIPTION_BACKUP_URL",
        "PERSONAL_DIRECT_DOMAIN": "PRIVATE_PERSONAL_DIRECT_DOMAIN",
        "WG_NODE_NAME": "PRIVATE_WG_NODE_NAME",
        "WG_NODE_NAMES": "PRIVATE_WG_NODE_NAMES",
        "WG_PROXY_LINES": "PRIVATE_WG_PROXY_LINES",
        "WG_PRIVATE_CIDR": "PRIVATE_WG_PRIVATE_CIDR",
        "URL_TEST_INTERVAL": "GENERAL_URL_TEST_INTERVAL",
        "URL_TEST_TOLERANCE": "GENERAL_URL_TEST_TOLERANCE",
    }
    for alias, source in alias_map.items():
        if source in values:
            aliases[alias] = values[source]

    if "PRIMARY_NAMES" not in aliases and "PRIMARY" in aliases:
        aliases["PRIMARY_NAMES"] = aliases["PRIMARY"]
    if "BACKUP_NAMES" not in aliases and "BACKUP" in aliases:
        aliases["BACKUP_NAMES"] = aliases["BACKUP"]
    if "WG_NODE_NAMES" not in aliases and "WG_NODE_NAME" in aliases:
        aliases["WG_NODE_NAMES"] = aliases["WG_NODE_NAME"]
    if "WG_PROXY_LINES" not in aliases:
        aliases["WG_PROXY_LINES"] = "# Add WireGuard lines in variables file"
    if "PRIMARY_PROXY_LINES" not in aliases and "PRIMARY" in aliases and "SUBSCRIPTION_URL_PRIMARY" in aliases:
        aliases["PRIMARY_PROXY_LINES"] = f"{aliases['PRIMARY']} = {aliases['SUBSCRIPTION_URL_PRIMARY']},parser-enabled=true,udp=true,block-quic=true,fast-open=default,vmess-aead=true,skip-cert-verify=true,enabled=true,flexible-sni=false"
    if "BACKUP_PROXY_LINES" not in aliases and "BACKUP" in aliases and "SUBSCRIPTION_URL_BACKUP" in aliases:
        aliases["BACKUP_PROXY_LINES"] = f"{aliases['BACKUP']} = {aliases['SUBSCRIPTION_URL_BACKUP']},parser-enabled=true,udp=true,block-quic=true,fast-open=default,vmess-aead=true,skip-cert-verify=true,enabled=true,flexible-sni=false"
    return aliases


def render(template_text: str, variables: dict[str, str]) -> str:
    missing: set[str] = set()
    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        if name not in variables:
            missing.add(name)
            return match.group(0)
        return variables[name]
    rendered = PLACEHOLDER_RE.sub(replace, template_text)
    if missing:
        raise SystemExit("Missing template variables: " + ", ".join(sorted(missing)))
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Loon template with YAML variables.")
    parser.add_argument("--template", required=True)
    parser.add_argument("--variables", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    template_path = Path(args.template)
    variables_path = Path(args.variables)
    output_path = Path(args.output)

    template_text = template_path.read_text(encoding="utf-8")
    variables_data = yaml.safe_load(variables_path.read_text(encoding="utf-8")) or {}
    if not isinstance(variables_data, dict):
        raise SystemExit("Variables file must contain a YAML mapping.")

    rendered = render(template_text, add_aliases(flatten(variables_data)))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Rendered {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
