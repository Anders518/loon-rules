# FakeLocation

本目录由上游 `FakeLocation/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`FakeLocationBiliBili.list`](./FakeLocationBiliBili.list) | 28 | `FakeLocation/FakeLocationBiliBili.yaml` |
| [`FakeLocationBiliBili_No_Resolve.list`](./FakeLocationBiliBili_No_Resolve.list) | 29 | `FakeLocation/FakeLocationBiliBili_No_Resolve.yaml` |
| [`FakeLocationDouBan.list`](./FakeLocationDouBan.list) | 5 | `FakeLocation/FakeLocationDouBan.yaml` |
| [`FakeLocationDouBan_No_Resolve.list`](./FakeLocationDouBan_No_Resolve.list) | 5 | `FakeLocation/FakeLocationDouBan_No_Resolve.yaml` |
| [`FakeLocationDouYin.list`](./FakeLocationDouYin.list) | 5 | `FakeLocation/FakeLocationDouYin.yaml` |
| [`FakeLocationDouYin_No_Resolve.list`](./FakeLocationDouYin_No_Resolve.list) | 5 | `FakeLocation/FakeLocationDouYin_No_Resolve.yaml` |
| [`FakeLocationKuaiShou.list`](./FakeLocationKuaiShou.list) | 2 | `FakeLocation/FakeLocationKuaiShou.yaml` |
| [`FakeLocationKuaiShou_No_Resolve.list`](./FakeLocationKuaiShou_No_Resolve.list) | 2 | `FakeLocation/FakeLocationKuaiShou_No_Resolve.yaml` |
| [`FakeLocationTieBa.list`](./FakeLocationTieBa.list) | 4 | `FakeLocation/FakeLocationTieBa.yaml` |
| [`FakeLocationTieBa_No_Resolve.list`](./FakeLocationTieBa_No_Resolve.list) | 4 | `FakeLocation/FakeLocationTieBa_No_Resolve.yaml` |
| [`FakeLocationWeiBo.list`](./FakeLocationWeiBo.list) | 4 | `FakeLocation/FakeLocationWeiBo.yaml` |
| [`FakeLocationWeiBo_No_Resolve.list`](./FakeLocationWeiBo_No_Resolve.list) | 4 | `FakeLocation/FakeLocationWeiBo_No_Resolve.yaml` |
| [`FakeLocationXiGua.list`](./FakeLocationXiGua.list) | 1 | `FakeLocation/FakeLocationXiGua.yaml` |
| [`FakeLocationXiGua_No_Resolve.list`](./FakeLocationXiGua_No_Resolve.list) | 1 | `FakeLocation/FakeLocationXiGua_No_Resolve.yaml` |
| [`FakeLocationXianYu.list`](./FakeLocationXianYu.list) | 16 | `FakeLocation/FakeLocationXianYu.yaml` |
| [`FakeLocationXianYu_No_Resolve.list`](./FakeLocationXianYu_No_Resolve.list) | 16 | `FakeLocation/FakeLocationXianYu_No_Resolve.yaml` |
| [`FakeLocationXiaoHongShu.list`](./FakeLocationXiaoHongShu.list) | 3 | `FakeLocation/FakeLocationXiaoHongShu.yaml` |
| [`FakeLocationXiaoHongShu_No_Resolve.list`](./FakeLocationXiaoHongShu_No_Resolve.list) | 3 | `FakeLocation/FakeLocationXiaoHongShu_No_Resolve.yaml` |
| [`FakeLocationZhiHu.list`](./FakeLocationZhiHu.list) | 9 | `FakeLocation/FakeLocationZhiHu.yaml` |
| [`FakeLocationZhiHu_No_Resolve.list`](./FakeLocationZhiHu_No_Resolve.list) | 9 | `FakeLocation/FakeLocationZhiHu_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationBiliBili.list, policy=AI, tag=FakeLocationBiliBili, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationBiliBili_No_Resolve.list, policy=AI, tag=FakeLocationBiliBili No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationDouBan.list, policy=AI, tag=FakeLocationDouBan, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationDouBan_No_Resolve.list, policy=AI, tag=FakeLocationDouBan No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationDouYin.list, policy=AI, tag=FakeLocationDouYin, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationDouYin_No_Resolve.list, policy=AI, tag=FakeLocationDouYin No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationKuaiShou.list, policy=AI, tag=FakeLocationKuaiShou, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationKuaiShou_No_Resolve.list, policy=AI, tag=FakeLocationKuaiShou No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationTieBa.list, policy=AI, tag=FakeLocationTieBa, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationTieBa_No_Resolve.list, policy=AI, tag=FakeLocationTieBa No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationWeiBo.list, policy=AI, tag=FakeLocationWeiBo, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationWeiBo_No_Resolve.list, policy=AI, tag=FakeLocationWeiBo No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXiGua.list, policy=AI, tag=FakeLocationXiGua, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXiGua_No_Resolve.list, policy=AI, tag=FakeLocationXiGua No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXianYu.list, policy=AI, tag=FakeLocationXianYu, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXianYu_No_Resolve.list, policy=AI, tag=FakeLocationXianYu No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXiaoHongShu.list, policy=AI, tag=FakeLocationXiaoHongShu, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationXiaoHongShu_No_Resolve.list, policy=AI, tag=FakeLocationXiaoHongShu No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationZhiHu.list, policy=AI, tag=FakeLocationZhiHu, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/FakeLocation/FakeLocationZhiHu_No_Resolve.list, policy=AI, tag=FakeLocationZhiHu No Resolve, enabled=true
```
