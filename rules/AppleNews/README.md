# AppleNews

本目录由上游 `AppleNews/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`AppleNews.list`](./AppleNews.list) | 11 | `AppleNews/AppleNews.yaml` |
| [`AppleNews_Domain.list`](./AppleNews_Domain.list) | 11 | `AppleNews/AppleNews_Domain.yaml` |
| [`AppleNews_No_Resolve.list`](./AppleNews_No_Resolve.list) | 11 | `AppleNews/AppleNews_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleNews/AppleNews.list, policy=AI, tag=AppleNews, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleNews/AppleNews_Domain.list, policy=AI, tag=AppleNews Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/AppleNews/AppleNews_No_Resolve.list, policy=AI, tag=AppleNews No Resolve, enabled=true
```
