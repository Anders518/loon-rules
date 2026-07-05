# Grok

本目录由上游 `Grok/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Grok.list`](./Grok.list) | 5 | `Grok/Grok.yaml` |
| [`Grok_Domain.list`](./Grok_Domain.list) | 4 | `Grok/Grok_Domain.yaml` |
| [`Grok_No_Resolve.list`](./Grok_No_Resolve.list) | 5 | `Grok/Grok_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Grok/Grok.list, policy=AI, tag=Grok, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Grok/Grok_Domain.list, policy=AI, tag=Grok Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Grok/Grok_No_Resolve.list, policy=AI, tag=Grok No Resolve, enabled=true
```
