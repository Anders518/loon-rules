# Signal

本目录由上游 `Signal/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Signal.list`](./Signal.list) | 2 | `Signal/Signal.yaml` |
| [`Signal_Domain.list`](./Signal_Domain.list) | 2 | `Signal/Signal_Domain.yaml` |
| [`Signal_No_Resolve.list`](./Signal_No_Resolve.list) | 2 | `Signal/Signal_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Signal/Signal.list, policy=AI, tag=Signal, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Signal/Signal_Domain.list, policy=AI, tag=Signal Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Signal/Signal_No_Resolve.list, policy=AI, tag=Signal No Resolve, enabled=true
```
