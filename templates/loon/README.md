# Loon Template

这个目录提供参考 `Accademia/Clash_Configuration_Template` 思路改造的 Loon 模板。

## 设计原则

Loon 与 Mihomo / Clash Meta 不是同一套配置模型，所以这里不做一比一转换，而是保留可迁移的部分：

- 白名单 / 黑名单两种路由思路；
- 国内优先直连；
- 海外 APP / AI / 流媒体 / 社交 / 工具按类别分流；
- IP 规则放在域名规则之后；
- 最后用 `FINAL` 兜底；
- 规则集通过本仓库自动生成的 `rules/<分类>/*.list` 引用。

## 文件

- `loon_whitelist.conf`：白名单模式。国内与局域网直连，明确列出的海外服务走代理，最终兜底直连。
- `loon_blacklist.conf`：黑名单模式。国内与局域网直连，广告/隐私类拦截，GFW/海外服务走代理，最终兜底代理。
- `loon_hybrid_optimized.conf`：结合当前手动配置习惯的公开安全模板。保留地区筛选、业务策略组、敏感网站固定节点、WireGuard 内网和个人直连域名占位符。

## 使用前必须修改

模板中的这些内容都是占位符：

- `<SUBSCRIPTION_URL_PRIMARY>`
- `<SUBSCRIPTION_URL_BACKUP>`
- `<PERSONAL_DIRECT_DOMAIN>`
- `<WG_PRIVATE_CIDR>`
- `<SENSITIVE_BANK_DOMAIN>`
- `<SENSITIVE_PAYMENT_DOMAIN>`
- `<SENSITIVE_EXCHANGE_DOMAIN>`

请只在本地私有配置里替换，不要提交到公开仓库。

## 推荐使用顺序

1. 先运行 GitHub Actions 生成 `rules/`；
2. 打开 `rules/README.md` 看所有分类；
3. 常规新配置用 `loon_whitelist.conf` 或 `loon_blacklist.conf`；
4. 从现有手动配置迁移，优先用 `loon_hybrid_optimized.conf`；
5. 把订阅 URL、个人域名、WireGuard CIDR、敏感网站清单只填在本地配置中。

## 注意

Mihomo 模板中的这些能力不能直接等价迁移到 Loon：

- `rule-providers` 原生 YAML 管理；
- `proxy-providers` 自动拉取节点；
- Clash Meta 的链式代理 / relay / dialer-proxy；
- 完整的 DNS nameserver-policy；
- geosite / geoip / mrs 原生规则集。

本仓库的定位是：用 GitHub Actions 把上游规则转换成 Loon 可订阅的文本规则，再提供 Loon 配置骨架。