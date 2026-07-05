# HomeIP

本目录由上游 `HomeIP/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`HomeIPJP.list`](./HomeIPJP.list) | 40 | `HomeIP/HomeIPJP.yaml` |
| [`HomeIPJP_No_Resolve.list`](./HomeIPJP_No_Resolve.list) | 40 | `HomeIP/HomeIPJP_No_Resolve.yaml` |
| [`HomeIPUS.list`](./HomeIPUS.list) | 95 | `HomeIP/HomeIPUS.yaml` |
| [`HomeIPUS_No_Resolve.list`](./HomeIPUS_No_Resolve.list) | 95 | `HomeIP/HomeIPUS_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HomeIP/HomeIPJP.list, policy=AI, tag=HomeIPJP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HomeIP/HomeIPJP_No_Resolve.list, policy=AI, tag=HomeIPJP No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HomeIP/HomeIPUS.list, policy=AI, tag=HomeIPUS, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HomeIP/HomeIPUS_No_Resolve.list, policy=AI, tag=HomeIPUS No Resolve, enabled=true
```
