# Aqara

本目录由上游 `Aqara/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`AqaraCN.list`](./AqaraCN.list) | 15 | `Aqara/AqaraCN.yaml` |
| [`AqaraCN._Domain.list`](./AqaraCN._Domain.list) | 14 | `Aqara/AqaraCN._Domain.yaml` |
| [`AqaraCN._No_Resolve.list`](./AqaraCN._No_Resolve.list) | 15 | `Aqara/AqaraCN._No_Resolve.yaml` |
| [`AqaraGlobal.list`](./AqaraGlobal.list) | 45 | `Aqara/AqaraGlobal.yaml` |
| [`AqaraGlobal._Domain.list`](./AqaraGlobal._Domain.list) | 36 | `Aqara/AqaraGlobal._Domain.yaml` |
| [`AqaraGlobal._IP.list`](./AqaraGlobal._IP.list) | 3 | `Aqara/AqaraGlobal._IP.yaml` |
| [`AqaraGlobal._No_Resolve.list`](./AqaraGlobal._No_Resolve.list) | 45 | `Aqara/AqaraGlobal._No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraCN.list, policy=AI, tag=AqaraCN, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraCN._Domain.list, policy=AI, tag=AqaraCN. Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraCN._No_Resolve.list, policy=AI, tag=AqaraCN. No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraGlobal.list, policy=AI, tag=AqaraGlobal, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraGlobal._Domain.list, policy=AI, tag=AqaraGlobal. Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraGlobal._IP.list, policy=AI, tag=AqaraGlobal. IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Aqara/AqaraGlobal._No_Resolve.list, policy=AI, tag=AqaraGlobal. No Resolve, enabled=true
```
