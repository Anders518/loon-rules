# Loon Template

这个目录提供一个参考 `Accademia/Clash_Configuration_Template` 思路改造的 Loon 模板。

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

## 使用前必须修改

模板中的策略组名是示例：

- `AI`
- `PROXY`
- `DIRECT`
- `REJECT`

请按你自己的 Loon 节点和策略组名称调整。

## 推荐使用顺序

1. 先运行 GitHub Actions 生成 `rules/`；
2. 打开 `rules/README.md` 看所有分类；
3. 从本目录选择一个模板；
4. 把模板中的 `policy=AI`、`policy=PROXY` 改成你的策略组；
5. 在 Loon 里导入或复制对应段落。

## 注意

Mihomo 模板中的这些能力不能直接等价迁移到 Loon：

- `rule-providers` 原生 YAML 管理；
- `proxy-providers` 自动拉取节点；
- Clash Meta 的链式代理 / relay / dialer-proxy；
- 完整的 DNS nameserver-policy；
- geosite / geoip / mrs 原生规则集。

本仓库的定位是：用 GitHub Actions 把上游规则转换成 Loon 可订阅的文本规则，再提供 Loon 配置骨架。