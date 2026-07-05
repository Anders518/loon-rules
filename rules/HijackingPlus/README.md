# HijackingPlus

本目录由上游 `HijackingPlus/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`HijackingPlus.list`](./HijackingPlus.list) | 30 | `HijackingPlus/HijackingPlus.yaml` |
| [`HijackingPlus_No_Resolve.list`](./HijackingPlus_No_Resolve.list) | 30 | `HijackingPlus/HijackingPlus_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HijackingPlus/HijackingPlus.list, policy=AI, tag=HijackingPlus, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/HijackingPlus/HijackingPlus_No_Resolve.list, policy=AI, tag=HijackingPlus No Resolve, enabled=true
```
