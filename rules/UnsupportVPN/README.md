# UnsupportVPN

本目录由上游 `UnsupportVPN/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`UnsupportVPN.list`](./UnsupportVPN.list) | 1 | `UnsupportVPN/UnsupportVPN.yaml` |
| [`UnsupportVPN_Domain.list`](./UnsupportVPN_Domain.list) | 1 | `UnsupportVPN/UnsupportVPN_Domain.yaml` |
| [`UnsupportVPN_No_Resolve.list`](./UnsupportVPN_No_Resolve.list) | 1 | `UnsupportVPN/UnsupportVPN_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/UnsupportVPN/UnsupportVPN.list, policy=AI, tag=UnsupportVPN, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/UnsupportVPN/UnsupportVPN_Domain.list, policy=AI, tag=UnsupportVPN Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/UnsupportVPN/UnsupportVPN_No_Resolve.list, policy=AI, tag=UnsupportVPN No Resolve, enabled=true
```
