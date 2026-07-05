# Pornhub

本目录由上游 `Pornhub/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Pornhub.list`](./Pornhub.list) | 23 | `Pornhub/Pornhub.yaml` |
| [`Pornhub_Domain.list`](./Pornhub_Domain.list) | 18 | `Pornhub/Pornhub_Domain.yaml` |
| [`Pornhub_No_Resolve.list`](./Pornhub_No_Resolve.list) | 23 | `Pornhub/Pornhub_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Pornhub/Pornhub.list, policy=AI, tag=Pornhub, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Pornhub/Pornhub_Domain.list, policy=AI, tag=Pornhub Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Pornhub/Pornhub_No_Resolve.list, policy=AI, tag=Pornhub No Resolve, enabled=true
```
