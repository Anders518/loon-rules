# BaiduNetDisk

本目录由上游 `BaiduNetDisk/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`BaiduNetDisk.list`](./BaiduNetDisk.list) | 19 | `BaiduNetDisk/BaiduNetDisk.yaml` |
| [`BaiduNetDisk_Domain.list`](./BaiduNetDisk_Domain.list) | 19 | `BaiduNetDisk/BaiduNetDisk_Domain.yaml` |
| [`BaiduNetDisk_No_Resolve.list`](./BaiduNetDisk_No_Resolve.list) | 19 | `BaiduNetDisk/BaiduNetDisk_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/BaiduNetDisk/BaiduNetDisk.list, policy=AI, tag=BaiduNetDisk, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/BaiduNetDisk/BaiduNetDisk_Domain.list, policy=AI, tag=BaiduNetDisk Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/BaiduNetDisk/BaiduNetDisk_No_Resolve.list, policy=AI, tag=BaiduNetDisk No Resolve, enabled=true
```
