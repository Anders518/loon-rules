# Mihomo Template

This directory contains a public-safe Mihomo template built around the Accademia DNS-first idea.

## Design goals

- DNS is the first-class control plane; routing rules are the second layer.
- Avoid fake-ip and avoid fallback DNS.
- Use `redir-host` with deterministic DNS behavior.
- Resolve CN, system, and personal-direct domains through domestic/system DNS.
- Resolve GitHub/raw/CDN resource domains through `主代理` DNS.
- Resolve AI domains through `AI` DNS.
- Resolve Crypto / Binance / OKX through `Crypto` DNS.
- Resolve regional bank rules through `BANK-HK`, `BANK-SG`, `BANK-US`, and `BANK-DE` DNS.
- Use Accademia upstream Clash/Mihomo YAML rule files directly where available.
- Use blackmatrix7 only as fallback for categories currently missing from Accademia:
  - OpenAI
  - Claude
  - Crypto
  - Binance
  - OKX
- Keep `Lk2` and `wd` as daily primary subscriptions.
- Keep `ssd-bk` as manual backup only.

## Files

```text
mihomo_hybrid_optimized.yaml
```

## DNS structure

The template intentionally uses:

```yaml
enhanced-mode: redir-host
fallback: []
nameserver-policy:
  rule-set:geosite-cn,china: domestic DoH
  rule-set:gemini,grok,copilot,openai,claude: DoH#AI
  rule-set:crypto,binance,okx: DoH#Crypto
  rule-set:bank-hk: DoH#BANK-HK
  rule-set:bank-sg: DoH#BANK-SG
  rule-set:bank-us: DoH#BANK-US
  rule-set:bank-de: DoH#BANK-DE
```

This is the main difference from a normal rule-heavy Mihomo file. The goal is to prevent DNS from becoming a side-channel that contradicts the later routing decision.

## Rendering

The public template contains placeholders such as:

```text
<MIHOMO_PROXY_PROVIDER_LINES>
<MIHOMO_STATIC_PROXY_LINES>
<MIHOMO_PRIMARY_PROVIDER_NAMES>
<MIHOMO_BACKUP_PROVIDER_NAMES>
<MIHOMO_WG_PROXY_NAMES>
<PERSONAL_DIRECT_DOMAIN>
<WG_PRIVATE_CIDR>
```

The private repository renders these into:

```text
generated/mihomo_hybrid_optimized.yaml
```

## Notes

Do not put real subscription URLs, WireGuard keys, endpoints, or personal sensitive domains in this public repository.

After each DNS change, validate with the target Mihomo client because some frontends lag behind Mihomo core support for policy-bound DNS syntax such as `https://1.1.1.1/dns-query#AI`.
