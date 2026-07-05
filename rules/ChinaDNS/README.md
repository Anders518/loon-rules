# ChinaDNS

本目录由上游 `ChinaDNS/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`ChinaDNS.list`](./ChinaDNS.list) | 67 | `ChinaDNS/ChinaDNS.yaml` |
| [`ChinaDNS_Domain.list`](./ChinaDNS_Domain.list) | 24 | `ChinaDNS/ChinaDNS_Domain.yaml` |
| [`ChinaDNS_IP.list`](./ChinaDNS_IP.list) | 42 | `ChinaDNS/ChinaDNS_IP.yaml` |
| [`ChinaDNS_No_Resolve.list`](./ChinaDNS_No_Resolve.list) | 67 | `ChinaDNS/ChinaDNS_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaDNS/ChinaDNS.list, policy=AI, tag=ChinaDNS, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaDNS/ChinaDNS_Domain.list, policy=AI, tag=ChinaDNS Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaDNS/ChinaDNS_IP.list, policy=AI, tag=ChinaDNS IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/ChinaDNS/ChinaDNS_No_Resolve.list, policy=AI, tag=ChinaDNS No Resolve, enabled=true
```
