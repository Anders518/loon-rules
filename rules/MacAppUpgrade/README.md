# MacAppUpgrade

本目录由上游 `MacAppUpgrade/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`MacAppUpgrade.list`](./MacAppUpgrade.list) | 476 | `MacAppUpgrade/MacAppUpgrade.yaml` |
| [`MacAppUpgrade_Domain.list`](./MacAppUpgrade_Domain.list) | 475 | `MacAppUpgrade/MacAppUpgrade_Domain.yaml` |
| [`MacAppUpgrade_No_Resolve.list`](./MacAppUpgrade_No_Resolve.list) | 476 | `MacAppUpgrade/MacAppUpgrade_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MacAppUpgrade/MacAppUpgrade.list, policy=AI, tag=MacAppUpgrade, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MacAppUpgrade/MacAppUpgrade_Domain.list, policy=AI, tag=MacAppUpgrade Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/MacAppUpgrade/MacAppUpgrade_No_Resolve.list, policy=AI, tag=MacAppUpgrade No Resolve, enabled=true
```
