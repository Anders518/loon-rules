# Copilot

本目录由上游 `Copilot/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Copilot.list`](./Copilot.list) | 16 | `Copilot/Copilot.yaml` |
| [`Copilot_Domain.list`](./Copilot_Domain.list) | 16 | `Copilot/Copilot_Domain.yaml` |
| [`Copilot_No_Resolve.list`](./Copilot_No_Resolve.list) | 16 | `Copilot/Copilot_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot.list, policy=AI, tag=Copilot, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_Domain.list, policy=AI, tag=Copilot Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_No_Resolve.list, policy=AI, tag=Copilot No Resolve, enabled=true
```
