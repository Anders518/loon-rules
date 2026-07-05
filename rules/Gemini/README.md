# Gemini

本目录由上游 `Gemini/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Gemini.list`](./Gemini.list) | 46 | `Gemini/Gemini.yaml` |
| [`Gemini_Domain.list`](./Gemini_Domain.list) | 57 | `Gemini/Gemini_Domain.yaml` |
| [`Gemini_No_Resolve.list`](./Gemini_No_Resolve.list) | 46 | `Gemini/Gemini_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini.list, policy=AI, tag=Gemini, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_Domain.list, policy=AI, tag=Gemini Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_No_Resolve.list, policy=AI, tag=Gemini No Resolve, enabled=true
```
