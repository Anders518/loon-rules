# ChinaMax

本目录由上游 `ChinaMax/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`ChinaMax.list`](./ChinaMax.list) | 97984 | `ChinaMax/ChinaMax.yaml` |
| [`ChinaMax_Domain.list`](./ChinaMax_Domain.list) | 97946 | `ChinaMax/ChinaMax_Domain.yaml` |
| [`ChinaMax_Domain.list`](./ChinaMax_Domain.list) | 117262 | `ChinaMax/备用数据/ChinaMax_Domain.yaml` |
| [`ChinaMax_No_Resolve.list`](./ChinaMax_No_Resolve.list) | 97984 | `ChinaMax/ChinaMax_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaMax/ChinaMax.list, policy=AI, tag=ChinaMax, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaMax/ChinaMax_Domain.list, policy=AI, tag=ChinaMax Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaMax/ChinaMax_Domain.list, policy=AI, tag=ChinaMax Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaMax/ChinaMax_No_Resolve.list, policy=AI, tag=ChinaMax No Resolve, enabled=true
```
