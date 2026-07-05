# Fastly

本目录由上游 `Fastly/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Fastly.list`](./Fastly.list) | 21 | `Fastly/Fastly.yaml` |
| [`Fastly_IP.list`](./Fastly_IP.list) | 21 | `Fastly/Fastly_IP.yaml` |
| [`Fastly_No_Resolve.list`](./Fastly_No_Resolve.list) | 21 | `Fastly/Fastly_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Fastly/Fastly.list, policy=AI, tag=Fastly, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Fastly/Fastly_IP.list, policy=AI, tag=Fastly IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Fastly/Fastly_No_Resolve.list, policy=AI, tag=Fastly No Resolve, enabled=true
```
