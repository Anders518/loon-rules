# BlockHttpDNSPlus

本目录由上游 `BlockHttpDNSPlus/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`BlockHttpDNSPlus.list`](./BlockHttpDNSPlus.list) | 12 | `BlockHttpDNSPlus/BlockHttpDNSPlus.yaml` |
| [`BlockHttpDNSPlus_No_Resolve.list`](./BlockHttpDNSPlus_No_Resolve.list) | 12 | `BlockHttpDNSPlus/BlockHttpDNSPlus_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/BlockHttpDNSPlus/BlockHttpDNSPlus.list, policy=AI, tag=BlockHttpDNSPlus, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/BlockHttpDNSPlus/BlockHttpDNSPlus_No_Resolve.list, policy=AI, tag=BlockHttpDNSPlus No Resolve, enabled=true
```
