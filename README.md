# Loon Rules

This repository converts rule-provider YAML files from Accademia/Additional_Rule_For_Clash into Loon-compatible text rule lists.

Generated files are written to `rules/*.list` by GitHub Actions.

## Update

The workflow runs every 6 hours and can also be started manually from the Actions tab.

## Example

After the first workflow run, use files under:

`https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/`

Example file names:

- `Gemini_Domain.list`
- `Gemini_IP.list`
- `OpenAI_Domain.list`
- `OpenAI_IP.list`

In Loon, add the generated raw file URL as a Remote Rule and set the policy to your own policy group name.

## Notes

The converter is conservative. It converts domain, domain-suffix, IP-CIDR, IP-CIDR6, and other compatible classical rule lines. Unsupported Mihomo-only or Clash-only rule types are skipped.
