# PreRepairEasyPrivacy

本目录由上游 `PreRepairEasyPrivacy/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`PreRepairEasyPrivacy.list`](./PreRepairEasyPrivacy.list) | 49 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy.yaml` |
| [`PreRepairEasyPrivacy_DIRECT.list`](./PreRepairEasyPrivacy_DIRECT.list) | 28 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_DIRECT.yaml` |
| [`PreRepairEasyPrivacy_DIRECT_No_Resolve.list`](./PreRepairEasyPrivacy_DIRECT_No_Resolve.list) | 28 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_DIRECT_No_Resolve.yaml` |
| [`PreRepairEasyPrivacy_No_Resolve.list`](./PreRepairEasyPrivacy_No_Resolve.list) | 49 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_No_Resolve.yaml` |
| [`PreRepairEasyPrivacy_PROXY.list`](./PreRepairEasyPrivacy_PROXY.list) | 5 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_PROXY.yaml` |
| [`PreRepairEasyPrivacy_PROXY_No_Resolve.list`](./PreRepairEasyPrivacy_PROXY_No_Resolve.list) | 5 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_PROXY_No_Resolve.yaml` |
| [`PreRepairEasyPrivacy_REJECT.list`](./PreRepairEasyPrivacy_REJECT.list) | 17 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_REJECT.yaml` |
| [`PreRepairEasyPrivacy_REJECT_No_Resolve.list`](./PreRepairEasyPrivacy_REJECT_No_Resolve.list) | 17 | `PreRepairEasyPrivacy/PreRepairEasyPrivacy_REJECT_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy.list, policy=AI, tag=PreRepairEasyPrivacy, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_DIRECT.list, policy=AI, tag=PreRepairEasyPrivacy DIRECT, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_DIRECT_No_Resolve.list, policy=AI, tag=PreRepairEasyPrivacy DIRECT No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_No_Resolve.list, policy=AI, tag=PreRepairEasyPrivacy No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_PROXY.list, policy=AI, tag=PreRepairEasyPrivacy PROXY, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_PROXY_No_Resolve.list, policy=AI, tag=PreRepairEasyPrivacy PROXY No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_REJECT.list, policy=AI, tag=PreRepairEasyPrivacy REJECT, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/PreRepairEasyPrivacy/PreRepairEasyPrivacy_REJECT_No_Resolve.list, policy=AI, tag=PreRepairEasyPrivacy REJECT No Resolve, enabled=true
```
