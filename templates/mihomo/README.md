# Mihomo Template

This directory contains a public-safe Mihomo template that mirrors the current Loon strategy design.

## Design goals

- Use Accademia upstream Clash/Mihomo YAML rule files directly.
- Keep the same practical routing model as the Loon config:
  - `Lk2` and `wd` as daily primary subscriptions.
  - `ssd-bk` as manual backup only.
  - `WG_PRIVATE` only for private WireGuard CIDR.
  - `lililib.net` or another personal domain always direct.
  - `AI`, `Crypto`, `BANK-HK`, `BANK-SG`, `BANK-US`, and `BANK-DE` as independent policies.
  - GitHub/raw/CDN resource domains through `主代理`.
- Use blackmatrix7 only as fallback for categories currently missing from Accademia:
  - OpenAI
  - Claude
  - Crypto
  - Binance
  - OKX

## Files

```text
mihomo_hybrid_optimized.yaml
```

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

The first version is intentionally conservative. DNS uses `redir-host` and domestic DoH defaults; later iterations can add a stricter Accademia-style `nameserver-policy` once the proxy and rule provider structure is verified.
