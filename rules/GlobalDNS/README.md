# GlobalDNS

本目录由上游 `GlobalDNS/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`GlobalDNS.list`](./GlobalDNS.list) | 567 | `GlobalDNS/GlobalDNS.yaml` |
| [`GlobalDNS_Domain.list`](./GlobalDNS_Domain.list) | 168 | `GlobalDNS/GlobalDNS_Domain.yaml` |
| [`GlobalDNS_IP.list`](./GlobalDNS_IP.list) | 407 | `GlobalDNS/GlobalDNS_IP.yaml` |
| [`GlobalDNS_No_Resolve.list`](./GlobalDNS_No_Resolve.list) | 567 | `GlobalDNS/GlobalDNS_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GlobalDNS/GlobalDNS.list, policy=AI, tag=GlobalDNS, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GlobalDNS/GlobalDNS_Domain.list, policy=AI, tag=GlobalDNS Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GlobalDNS/GlobalDNS_IP.list, policy=AI, tag=GlobalDNS IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GlobalDNS/GlobalDNS_No_Resolve.list, policy=AI, tag=GlobalDNS No Resolve, enabled=true
```
