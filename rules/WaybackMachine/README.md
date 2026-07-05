# WaybackMachine

本目录由上游 `WaybackMachine/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`WaybackMachine.list`](./WaybackMachine.list) | 7 | `WaybackMachine/WaybackMachine.yaml` |
| [`WaybackMachine_Domain.list`](./WaybackMachine_Domain.list) | 1 | `WaybackMachine/WaybackMachine_Domain.yaml` |
| [`WaybackMachine_IP.list`](./WaybackMachine_IP.list) | 6 | `WaybackMachine/WaybackMachine_IP.yaml` |
| [`WaybackMachine_No_Resolve.list`](./WaybackMachine_No_Resolve.list) | 7 | `WaybackMachine/WaybackMachine_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WaybackMachine/WaybackMachine.list, policy=AI, tag=WaybackMachine, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WaybackMachine/WaybackMachine_Domain.list, policy=AI, tag=WaybackMachine Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WaybackMachine/WaybackMachine_IP.list, policy=AI, tag=WaybackMachine IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/WaybackMachine/WaybackMachine_No_Resolve.list, policy=AI, tag=WaybackMachine No Resolve, enabled=true
```
