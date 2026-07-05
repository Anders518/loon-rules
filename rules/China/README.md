# China

本目录由上游 `China/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`China.list`](./China.list) | 3045 | `China/China.yaml` |
| [`China_Domain.list`](./China_Domain.list) | 3044 | `China/China_Domain.yaml` |
| [`China_No_Resolve.list`](./China_No_Resolve.list) | 3045 | `China/China_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/China/China.list, policy=AI, tag=China, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/China/China_Domain.list, policy=AI, tag=China Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/China/China_No_Resolve.list, policy=AI, tag=China No Resolve, enabled=true
```
