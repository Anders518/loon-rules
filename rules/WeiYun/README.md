# WeiYun

本目录由上游 `WeiYun/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`WeiYun.list`](./WeiYun.list) | 18 | `WeiYun/WeiYun.yaml` |
| [`WeiYun_Domain.list`](./WeiYun_Domain.list) | 7 | `WeiYun/WeiYun_Domain.yaml` |
| [`WeiYun_IP.list`](./WeiYun_IP.list) | 11 | `WeiYun/WeiYun_IP.yaml` |
| [`WeiYun_No_Resolve.list`](./WeiYun_No_Resolve.list) | 18 | `WeiYun/WeiYun_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WeiYun/WeiYun.list, policy=AI, tag=WeiYun, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WeiYun/WeiYun_Domain.list, policy=AI, tag=WeiYun Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WeiYun/WeiYun_IP.list, policy=AI, tag=WeiYun IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WeiYun/WeiYun_No_Resolve.list, policy=AI, tag=WeiYun No Resolve, enabled=true
```
