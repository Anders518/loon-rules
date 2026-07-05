# Alipan

本目录由上游 `Alipan/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Alipan.list`](./Alipan.list) | 17 | `Alipan/Alipan.yaml` |
| [`Alipan_Domain.list`](./Alipan_Domain.list) | 17 | `Alipan/Alipan_Domain.yaml` |
| [`Alipan_No_Resolve.list`](./Alipan_No_Resolve.list) | 17 | `Alipan/Alipan_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Alipan/Alipan.list, policy=AI, tag=Alipan, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Alipan/Alipan_Domain.list, policy=AI, tag=Alipan Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Alipan/Alipan_No_Resolve.list, policy=AI, tag=Alipan No Resolve, enabled=true
```
