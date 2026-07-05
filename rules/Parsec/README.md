# Parsec

本目录由上游 `Parsec/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Parsec.list`](./Parsec.list) | 1 | `Parsec/Parsec.yaml` |
| [`Parsec_Domain.list`](./Parsec_Domain.list) | 1 | `Parsec/Parsec_Domain.yaml` |
| [`Parsec_No_Resolve.list`](./Parsec_No_Resolve.list) | 1 | `Parsec/Parsec_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Parsec/Parsec.list, policy=AI, tag=Parsec, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Parsec/Parsec_Domain.list, policy=AI, tag=Parsec Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Parsec/Parsec_No_Resolve.list, policy=AI, tag=Parsec No Resolve, enabled=true
```
