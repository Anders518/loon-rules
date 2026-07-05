# Loon Config Pre-push Checklist

本清单用于所有 Loon 配置相关提交。任何修改 `templates/loon/*.conf`、渲染脚本、README 示例或 private repo 生成逻辑前，都必须先完成本清单。

官方文档入口：

```text
https://nsloon.app/docs/intro/
```

## 1. 先确定本次改动涉及的配置区域

- [ ] `[General]`
- [ ] `[Proxy]`
- [ ] `[Remote Proxy]`
- [ ] `[Remote Filter]`
- [ ] `[Proxy Group]`
- [ ] `[Rule]`
- [ ] `[Remote Rule]`
- [ ] `[Host]`
- [ ] `[Rewrite]`
- [ ] `[Script]`
- [ ] `[Plugin]`
- [ ] `[Mitm]`
- [ ] 渲染变量 / 占位符
- [ ] GitHub Actions 渲染流程

## 2. 逐项查询官方文档

每个新增或修改字段都必须能在官方文档中找到依据。

| 配置区域 | 官方文档类别 |
| --- | --- |
| `[Proxy]` | 节点 |
| `[Remote Proxy]` | 节点 |
| `[Remote Filter]` | 节点 |
| `[Proxy Group]` | 策略 |
| `[Rule]` | 规则 |
| `[Remote Rule]` | 规则 |
| `[Host]` | DNS |
| `[Rewrite]` | 复写 |
| `[Script]` | 脚本 |
| `[Plugin]` | 插件 |
| `[Mitm]` | 其他配置 |
| `[General]` | 其他配置 / DNS / 对应专题页面 |

## 3. 字段级检查

逐个字段确认：

- [ ] 字段名大小写正确；
- [ ] 分隔符正确；
- [ ] 参数顺序正确；
- [ ] 布尔值写法正确；
- [ ] 策略组名与引用一致；
- [ ] 远程规则格式符合 Loon；
- [ ] 没有混入 Mihomo / Clash / Stash 专属语法；
- [ ] WireGuard 节点行按 Loon 官方节点格式原样维护；
- [ ] 不确定字段只保留注释，不启用。

## 4. 安全检查

- [ ] public repo 不包含真实订阅 URL；
- [ ] public repo 不包含 WireGuard private-key / preshared-key；
- [ ] public repo 不包含证书或 passphrase；
- [ ] public repo 不包含个人域名；
- [ ] public repo 不包含敏感网站清单；
- [ ] private repo 也避免在 Actions log 中输出敏感字段。

## 5. 推送前结论

只有全部满足时才能推送：

```text
官方文档已核对：是
字段级复核完成：是
无公开敏感信息：是
不确定配置未启用：是
```
