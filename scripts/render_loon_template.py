#!/usr/bin/env python3
"""Render Loon templates with centralized YAML variables.

Loon `.conf` files do not provide a reliable native variable/include mechanism, so this
script performs variable substitution before the config is imported by Loon.

Usage:
  python scripts/render_loon_template.py \
    --template templates/loon/loon_hybrid_optimized.conf \
    --variables templates/loon/variables.public.yml \
    --output generated/loon_hybrid_optimized.conf
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

PLACEHOLDER_RE = re.compile(r"<([A-Z0-9_]+)>")


def scalar_to_string(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    return str(value)


def flatten(data: dict[str, Any], prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}

    for key, value in data.items():
        normalized_key = f"{prefix}_{key}" if prefix else str(key)
        normalized_key = normalized_key.upper()

        if isinstance(value, dict):
            result.update(flatten(value, normalized_key))
        else:
            result[normalized_key] = scalar_to_string(value)

    return result


def add_aliases(values: dict[str, str]) -> dict[str, str]:
    aliases = dict(values)

    # Short aliases used by existing templates.
    alias_map = {
        "PRIMARY": "SUBSCRIPTION_PRIMARY_NAME",
        "BACKUP": "SUBSCRIPTION_BACKUP_NAME",
        "SUBSCRIPTION_URL_PRIMARY": "SUBSCRIPTION_PRIMARY_URL",
        "SUBSCRIPTION_URL_BACKUP": "SUBSCRIPTION_BACKUP_URL",
        "PERSONAL_DIRECT_DOMAIN": "PRIVATE_PERSONAL_DIRECT_DOMAIN",
        "WG_NODE_NAME": "PRIVATE_WG_NODE_NAME",
        "WG_NODE_NAMES": "PRIVATE_WG_NODE_NAMES",
        "WG_PRIVATE_CIDR": "PRIVATE_WG_PRIVATE_CIDR",
        "URL_TEST_INTERVAL": "GENERAL_URL_TEST_INTERVAL",
        "URL_TEST_TOLERANCE": "GENERAL_URL_TEST_TOLERANCE",
    }

    for alias, source in alias_map.items():
        if source in values:
            aliases[alias] = values[source]

    # Backward compatibility: if only wg_node_name is defined, use it as wg_node_names too.
    if "WG_NODE_NAMES" not in aliases and "WG_NODE_NAME" in aliases:
        aliases["WG_NODE_NAMES"] = aliases["WG_NODE_NAME"]

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
        missing_list = ", ".join(sorted(missing))
        raise SystemExit(f"Missing template variables: {missing_list}")

    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Loon template with YAML variables.")
    parser.add_argument("--template", required=True, help="Path to source template file.")
    parser.add_argument("--variables", required=True, help="Path to YAML variables file.")
    parser.add_argument("--output", required=True, help="Path to rendered output file.")
    args = parser.parse_args()

    template_path = Path(args.template)
    variables_path = Path(args.variables)
    output_path = Path(args.output)

    template_text = template_path.read_text(encoding="utf-8")
    variables_data = yaml.safe_load(variables_path.read_text(encoding="utf-8")) or {}

    if not isinstance(variables_data, dict):
        raise SystemExit("Variables file must contain a YAML mapping.")

    variables = add_aliases(flatten(variables_data))
    rendered = render(template_text, variables)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Rendered {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
