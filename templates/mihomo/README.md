# Mihomo Template

This directory contains a public-safe Mihomo template built around the user's working Nikki/Mihomo configuration and the Accademia DNS-first idea.

## Design goals

- DNS is the first-class control plane; routing rules are the second layer.
- Avoid fake-ip and avoid fallback DNS.
- Use `redir-host` with deterministic DNS behavior.
- Match blacklist routing semantics: unmatched traffic goes to `主代理`, and unmatched DNS now also goes through `主代理`.
- Use `nameserver-policy` to pull CN, system, personal-direct, and other known direct domains back to domestic/system DNS.
- Use generic provider names such as `primary-a`, `primary-b`, and `backup`; do not hard-code real subscription brand names in the public template.
- Manual regional selectors such as `香港节点`, `日本节点`, and `美国节点` use all providers, including `backup`.
- Url-test groups such as `香港时延优选` and `美国时延优选` use only primary providers, so backup nodes are available for manual selection but are not auto-selected.
- Backup providers should use provider-level `override.additional-prefix`, for example `[BK] `, so backup nodes are visually identifiable in Nikki.
- Preserve the working config's group order, especially `PROXY_CHAIN`, `SENSITIVE_FIXED`, `BANK-*`, `Crypto`, and `AI` near the top.
- Custom static proxies can use `dialer-proxy: PROXY_CHAIN`.
- Custom rules are injected before public rule sets.
- Japan-only sites are handled by `JapanSites.yaml` and routed to `日本策略`.
- Use Accademia upstream Clash/Mihomo YAML rule files directly where available.
- Use blackmatrix7 only as fallback for categories currently missing from Accademia: OpenAI, Claude, Crypto, Binance, and OKX.

## Files

```text
mihomo_hybrid_optimized.yaml
rules/JapanSites.yaml
```

## DNS structure

The template intentionally uses:

```yaml
enhanced-mode: redir-host
nameserver:
  - https://1.1.1.1/dns-query#主代理
  - https://8.8.8.8/dns-query#主代理
fallback: []
nameserver-policy:
  +.<PERSONAL_DIRECT_DOMAIN>: system
  rule-set:geosite-cn,china: domestic DoH
  rule-set:gemini,grok,copilot,apple-ai: DoH#AI
  rule-set:japan-sites: DoH#日本策略
  rule-set:bank-hk: DoH#BANK-HK
  rule-set:bank-sg: DoH#BANK-SG
  rule-set:bank-us: DoH#BANK-US
  rule-set:bank-de: DoH#BANK-DE
```

Resolution order:

```text
1. If a domain matches nameserver-policy, use the policy-specific resolver.
2. If it does not match nameserver-policy, use nameserver, which now resolves through 主代理.
3. fallback remains disabled, so there is no second automatic resolver path.
```

## Latest DNS change

Changed default `nameserver` from domestic DoH:

```yaml
- https://dns.alidns.com/dns-query
- https://doh.pub/dns-query
```

to proxy-side DoH:

```yaml
- https://1.1.1.1/dns-query#主代理
- https://8.8.8.8/dns-query#主代理
```

`default-nameserver` and `proxy-server-nameserver` remain domestic to bootstrap DNS/proxy-provider hostnames before proxy groups are fully ready. CN/direct domains continue to be routed back to domestic/system DNS by `nameserver-policy`.

Classical providers such as blackmatrix7 OpenAI, Claude, Crypto, Binance, and OKX are kept in traffic rules, not DNS policy, to avoid Nikki warnings about classical providers in DNS matching.

## Rendering

The public template contains placeholders such as:

```text
<MIHOMO_PROXY_PROVIDER_LINES>
<MIHOMO_STATIC_PROXY_LINES>
<MIHOMO_ALL_PROVIDER_NAME_LINES>
<MIHOMO_PRIMARY_PROVIDER_NAME_LINES>
<MIHOMO_WG_PROXY_NAMES>
<MIHOMO_CUSTOM_RULE_LINES>
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
