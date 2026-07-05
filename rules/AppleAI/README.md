# AppleAI

本目录由上游 `AppleAI/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`AppleAI.list`](./AppleAI.list) | 8 | `AppleAI/AppleAI.yaml` |
| [`AppleAI_Domain.list`](./AppleAI_Domain.list) | 8 | `AppleAI/AppleAI_Domain.yaml` |
| [`AppleAI_No_Resolve.list`](./AppleAI_No_Resolve.list) | 8 | `AppleAI/AppleAI_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleAI/AppleAI.list, policy=AI, tag=AppleAI, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleAI/AppleAI_Domain.list, policy=AI, tag=AppleAI Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleAI/AppleAI_No_Resolve.list, policy=AI, tag=AppleAI No Resolve, enabled=true
```
