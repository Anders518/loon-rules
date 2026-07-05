# RustDesk

本目录由上游 `RustDesk/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`RustDesk.list`](./RustDesk.list) | 3 | `RustDesk/RustDesk.yaml` |
| [`RustDesk_Domain.list`](./RustDesk_Domain.list) | 3 | `RustDesk/RustDesk_Domain.yaml` |
| [`RustDesk_No_Resolve.list`](./RustDesk_No_Resolve.list) | 3 | `RustDesk/RustDesk_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/RustDesk/RustDesk.list, policy=AI, tag=RustDesk, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/RustDesk/RustDesk_Domain.list, policy=AI, tag=RustDesk Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/RustDesk/RustDesk_No_Resolve.list, policy=AI, tag=RustDesk No Resolve, enabled=true
```
