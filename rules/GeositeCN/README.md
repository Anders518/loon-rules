# GeositeCN

本目录由上游 `GeositeCN/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`GeositeCN.list`](./GeositeCN.list) | 4781 | `GeositeCN/GeositeCN.yaml` |
| [`GeositeCN_Domain.list`](./GeositeCN_Domain.list) | 4764 | `GeositeCN/GeositeCN_Domain.yaml` |
| [`GeositeCN_No_Resolve.list`](./GeositeCN_No_Resolve.list) | 4781 | `GeositeCN/GeositeCN_No_Resolve.yaml` |
| [`GeositeCN_domain.2025-12-03.list`](./GeositeCN_domain.2025-12-03.list) | 6619 | `GeositeCN/备用数据/GeositeCN_domain.2025-12-03.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GeositeCN/GeositeCN.list, policy=AI, tag=GeositeCN, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GeositeCN/GeositeCN_Domain.list, policy=AI, tag=GeositeCN Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GeositeCN/GeositeCN_No_Resolve.list, policy=AI, tag=GeositeCN No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/GeositeCN/GeositeCN_domain.2025-12-03.list, policy=AI, tag=GeositeCN domain.2025-12-03, enabled=true
```
