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

## Loon 是否支持变量？

不要假设 Loon `.conf` 原生支持变量、宏或 `include`。为了集中维护配置区，本仓库使用“源码模板 + YAML 变量 + 渲染脚本”的方式：

```text
templates/loon/variables.public.yml
        +
templates/loon/loon_hybrid_optimized.conf
        ↓
scripts/render_loon_template.py
        ↓
generated/loon_hybrid_optimized.conf
```

Loon 应导入或订阅 `generated/loon_hybrid_optimized.conf`。源码模板里的 `<PLACEHOLDER>` 只给渲染脚本使用。

## GitHub Actions 能不能放敏感配置？

可以把敏感值放进 GitHub Actions Secrets，但不建议在这个 public repo 中这样做。

原因是：Secrets 只保护 Actions 运行时的输入。如果 Actions 把真实订阅 URL、个人域名、WireGuard CIDR、证书或敏感网站清单渲染进 `generated/*.conf`，然后再 commit 到公开仓库，秘密仍然会公开。

因此本仓库的安全策略是：

- public repo 只保存公开模板、公开占位变量和公开生成结果；
- 不在 public repo 的 Actions Secrets 里维护真实 Loon 私有配置；
- 不把真实渲染后的个人配置提交到 public repo；
- 真实配置只在本地渲染，或放到 private repo / 私有分支 / 私有存储中维护。

## 文件

- `loon_whitelist.conf`：白名单模式。国内与局域网直连，明确列出的海外服务走代理，最终兜底直连。
- `loon_blacklist.conf`：黑名单模式。国内与局域网直连，广告/隐私类拦截，GFW/海外服务走代理，最终兜底代理。
- `loon_hybrid_optimized.conf`：结合当前手动配置习惯的公开安全模板。保留地区筛选、业务策略组、敏感网站固定节点、WireGuard 内网和个人直连域名占位符。
- `variables.public.yml`：公开示例变量文件，只包含占位符。

## 私有变量推荐做法

在本地创建一个不会提交的文件：

```text
templates/loon/variables.private.yml
```

然后把真实值写进去，例如：

```yaml
subscription:
  primary_name: "Lk2"
  backup_name: "ssd-bk"
  primary_url: "真实主订阅 URL"
  backup_url: "真实备用订阅 URL"

private:
  personal_direct_domain: "你的个人域名"
  wg_node_name: "你的 WireGuard 节点名"
  wg_private_cidr: "你的 WireGuard 内网 CIDR"
```

本地渲染：

```bash
python scripts/render_loon_template.py \
  --template templates/loon/loon_hybrid_optimized.conf \
  --variables templates/loon/variables.private.yml \
  --output generated/private/loon_hybrid_optimized.conf
```

`generated/private/` 和 `variables.private.yml` 都应加入 `.gitignore`。

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
5. 把订阅 URL、个人域名、WireGuard CIDR、敏感网站清单只填在本地配置中；
6. 需要远程订阅完整私有配置时，用 private repo 或其他私有托管方式，不要用 public raw URL。

## 注意

Mihomo 模板中的这些能力不能直接等价迁移到 Loon：

- `rule-providers` 原生 YAML 管理；
- `proxy-providers` 自动拉取节点；
- Clash Meta 的链式代理 / relay / dialer-proxy；
- 完整的 DNS nameserver-policy；
- geosite / geoip / mrs 原生规则集。

本仓库的定位是：用 GitHub Actions 把上游规则转换成 Loon 可订阅的文本规则，再提供 Loon 配置骨架。