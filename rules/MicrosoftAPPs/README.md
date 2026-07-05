# MicrosoftAPPs

本目录由上游 `MicrosoftAPPs/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`MicrosoftAPPs.list`](./MicrosoftAPPs.list) | 63 | `MicrosoftAPPs/MicrosoftAPPs.yaml` |
| [`MicrosoftAPPs_Domain.list`](./MicrosoftAPPs_Domain.list) | 60 | `MicrosoftAPPs/MicrosoftAPPs_Domain.yaml` |
| [`MicrosoftAPPs_No_Resolve.list`](./MicrosoftAPPs_No_Resolve.list) | 63 | `MicrosoftAPPs/MicrosoftAPPs_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MicrosoftAPPs/MicrosoftAPPs.list, policy=AI, tag=MicrosoftAPPs, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MicrosoftAPPs/MicrosoftAPPs_Domain.list, policy=AI, tag=MicrosoftAPPs Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MicrosoftAPPs/MicrosoftAPPs_No_Resolve.list, policy=AI, tag=MicrosoftAPPs No Resolve, enabled=true
```
