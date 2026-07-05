# Apple

本目录由上游 `Apple/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Apple.list`](./Apple.list) | 23 | `Apple/Apple.yaml` |
| [`Apple_Domain.list`](./Apple_Domain.list) | 21 | `Apple/Apple_Domain.yaml` |
| [`Apple_IP.list`](./Apple_IP.list) | 1 | `Apple/Apple_IP.yaml` |
| [`Apple_No_Resolve.list`](./Apple_No_Resolve.list) | 23 | `Apple/Apple_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Apple/Apple.list, policy=AI, tag=Apple, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Apple/Apple_Domain.list, policy=AI, tag=Apple Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Apple/Apple_IP.list, policy=AI, tag=Apple IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Apple/Apple_No_Resolve.list, policy=AI, tag=Apple No Resolve, enabled=true
```
