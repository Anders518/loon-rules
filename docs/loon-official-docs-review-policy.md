# Loon Official Docs Review Policy

本仓库涉及 Loon 配置语法的任何变更，必须以 Loon 官方文档为准，不允许凭经验或其他客户端配置习惯直接推断。

官方文档入口：

```text
https://nsloon.app/docs/intro/
```

## 强制流程

每次修改以下文件前，必须先查官方文档对应章节：

```text
templates/loon/*.conf
templates/loon/*.yml
scripts/render_loon_template.py
README 中的 Loon 配置示例
private repo 中的 Loon 配置模板或渲染逻辑
```

涉及以下段落或字段时，必须逐项核对：

| 配置区域 | 必查官方文档 |
| --- | --- |
| `[Proxy]` 节点行 | 节点 / 节点（代理服务器） |
| `[Remote Proxy]` 订阅节点 | 节点 / 节点（代理服务器） |
| `[Remote Filter]` 节点筛选 | 节点 / 筛选节点 |
| `[Proxy Group]` 策略组 | 策略 |
| `[Rule]` 本地规则 | 规则 / 域名类规则 / IP类规则 / Final |
| `[Remote Rule]` 远程规则 | 规则 / 订阅规则 |
| `[Host]` / DNS 映射 | DNS / DNS映射 |
| DNS 相关 General 项 | DNS |
| `[Rewrite]` | 复写 |
| `[Script]` | 脚本 |
| `[Plugin]` | 插件 |
| `[Mitm]` | 其他配置 / MITM 相关说明 |
| 其他 `[General]` 字段 | 其他配置 |

## 提交前检查清单

每次提交 Loon 配置变更前，必须确认：

- [ ] 已打开 Loon 官方文档入口。
- [ ] 已打开被修改配置区域的对应官方章节。
- [ ] 每个新增字段都能在官方文档中找到对应语法或说明。
- [ ] 每个字段的大小写、分隔符、参数名、布尔值写法已按官方文档核对。
- [ ] 没有把 Mihomo / Clash / Stash 语法直接搬到 Loon。
- [ ] 没有把无法确认的字段写成默认启用。
- [ ] 不确定的配置只写成注释，不写成启用项。
- [ ] 没有把真实订阅 URL、密钥、证书、个人域名、敏感网站清单写入 public repo。
- [ ] 如果是 private repo，也避免把敏感内容写进公开 issue、PR、Actions 日志。

## WireGuard 特别规则

WireGuard 节点必须按 Loon 官方 `[Proxy]` 节点格式维护。

本仓库不拆解、重组或猜测 WireGuard 字段。做法是：

1. 在 private repo 的变量文件中保存完整 Loon 官方格式节点行；
2. public 模板只提供 `<WG_PROXY_LINES>` 插槽；
3. 渲染器只做原样注入，不改写字段；
4. 每次修改 WireGuard 行前，先核对官方“节点（代理服务器）”文档。

## 执行原则

如果官方文档无法确认某个字段或语法：

- 不推送启用配置；
- 可以在模板中写成注释，并标记“待官方文档确认”；
- 或暂停修改，先要求用户提供 Loon App 导出的有效配置样例。
