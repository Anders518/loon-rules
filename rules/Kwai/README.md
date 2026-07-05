# Kwai

本目录由上游 `Kwai/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Kwai.list`](./Kwai.list) | 12 | `Kwai/Kwai.yaml` |
| [`Kwai_Domain.list`](./Kwai_Domain.list) | 12 | `Kwai/Kwai_Domain.yaml` |
| [`Kwai_No_Resolve.list`](./Kwai_No_Resolve.list) | 12 | `Kwai/Kwai_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Kwai/Kwai.list, policy=AI, tag=Kwai, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Kwai/Kwai_Domain.list, policy=AI, tag=Kwai Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Kwai/Kwai_No_Resolve.list, policy=AI, tag=Kwai No Resolve, enabled=true
```
