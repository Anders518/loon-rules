# eMuleServer

本目录由上游 `eMuleServer/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`eMuleServer.list`](./eMuleServer.list) | 55 | `eMuleServer/eMuleServer.yaml` |
| [`eMuleServer_IP.list`](./eMuleServer_IP.list) | 55 | `eMuleServer/eMuleServer_IP.yaml` |
| [`eMuleServer_No_Resolve.list`](./eMuleServer_No_Resolve.list) | 55 | `eMuleServer/eMuleServer_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/eMuleServer/eMuleServer.list, policy=AI, tag=eMuleServer, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/eMuleServer/eMuleServer_IP.list, policy=AI, tag=eMuleServer IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/eMuleServer/eMuleServer_No_Resolve.list, policy=AI, tag=eMuleServer No Resolve, enabled=true
```
