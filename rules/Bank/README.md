# Bank

本目录由上游 `Bank/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`BankAU.list`](./BankAU.list) | 15 | `Bank/BankAU.yaml` |
| [`BankAU_Domain.list`](./BankAU_Domain.list) | 15 | `Bank/BankAU_Domain.yaml` |
| [`BankAU_No_Resolve.list`](./BankAU_No_Resolve.list) | 15 | `Bank/BankAU_No_Resolve.yaml` |
| [`BankCA.list`](./BankCA.list) | 8 | `Bank/BankCA.yaml` |
| [`BankCA_Domain.list`](./BankCA_Domain.list) | 8 | `Bank/BankCA_Domain.yaml` |
| [`BankCA_No_Resolve.list`](./BankCA_No_Resolve.list) | 8 | `Bank/BankCA_No_Resolve.yaml` |
| [`BankDE.list`](./BankDE.list) | 10 | `Bank/BankDE.yaml` |
| [`BankDE_Domain.list`](./BankDE_Domain.list) | 10 | `Bank/BankDE_Domain.yaml` |
| [`BankDE_No_Resolve.list`](./BankDE_No_Resolve.list) | 10 | `Bank/BankDE_No_Resolve.yaml` |
| [`BankFR.list`](./BankFR.list) | 10 | `Bank/BankFR.yaml` |
| [`BankFR_Domain.list`](./BankFR_Domain.list) | 10 | `Bank/BankFR_Domain.yaml` |
| [`BankFR_No_Resolve.list`](./BankFR_No_Resolve.list) | 10 | `Bank/BankFR_No_Resolve.yaml` |
| [`BankHK.list`](./BankHK.list) | 16 | `Bank/BankHK.yaml` |
| [`BankHK_Domain.list`](./BankHK_Domain.list) | 20 | `Bank/BankHK_Domain.yaml` |
| [`BankHK_No_Resolve.list`](./BankHK_No_Resolve.list) | 16 | `Bank/BankHK_No_Resolve.yaml` |
| [`BankJP.list`](./BankJP.list) | 7 | `Bank/BankJP.yaml` |
| [`BankJP_Domain.list`](./BankJP_Domain.list) | 7 | `Bank/BankJP_Domain.yaml` |
| [`BankJP_No_Resolve.list`](./BankJP_No_Resolve.list) | 7 | `Bank/BankJP_No_Resolve.yaml` |
| [`BankNL.list`](./BankNL.list) | 10 | `Bank/BankNL.yaml` |
| [`BankNL_Domain.list`](./BankNL_Domain.list) | 10 | `Bank/BankNL_Domain.yaml` |
| [`BankNL_No_Resolve.list`](./BankNL_No_Resolve.list) | 10 | `Bank/BankNL_No_Resolve.yaml` |
| [`BankSG.list`](./BankSG.list) | 10 | `Bank/BankSG.yaml` |
| [`BankSG_Domain.list`](./BankSG_Domain.list) | 16 | `Bank/BankSG_Domain.yaml` |
| [`BankSG_No_Resolve.list`](./BankSG_No_Resolve.list) | 10 | `Bank/BankSG_No_Resolve.yaml` |
| [`BankUK.list`](./BankUK.list) | 28 | `Bank/BankUK.yaml` |
| [`BankUK_Domain.list`](./BankUK_Domain.list) | 28 | `Bank/BankUK_Domain.yaml` |
| [`BankUK_No_Resolve.list`](./BankUK_No_Resolve.list) | 28 | `Bank/BankUK_No_Resolve.yaml` |
| [`BankUS.list`](./BankUS.list) | 45 | `Bank/BankUS.yaml` |
| [`BankUS_Domain.list`](./BankUS_Domain.list) | 50 | `Bank/BankUS_Domain.yaml` |
| [`BankUS_No_Resolve.list`](./BankUS_No_Resolve.list) | 45 | `Bank/BankUS_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankAU.list, policy=AI, tag=BankAU, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankAU_Domain.list, policy=AI, tag=BankAU Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankAU_No_Resolve.list, policy=AI, tag=BankAU No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankCA.list, policy=AI, tag=BankCA, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankCA_Domain.list, policy=AI, tag=BankCA Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankCA_No_Resolve.list, policy=AI, tag=BankCA No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankDE.list, policy=AI, tag=BankDE, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankDE_Domain.list, policy=AI, tag=BankDE Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankDE_No_Resolve.list, policy=AI, tag=BankDE No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankFR.list, policy=AI, tag=BankFR, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankFR_Domain.list, policy=AI, tag=BankFR Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankFR_No_Resolve.list, policy=AI, tag=BankFR No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankHK.list, policy=AI, tag=BankHK, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankHK_Domain.list, policy=AI, tag=BankHK Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankHK_No_Resolve.list, policy=AI, tag=BankHK No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankJP.list, policy=AI, tag=BankJP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankJP_Domain.list, policy=AI, tag=BankJP Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankJP_No_Resolve.list, policy=AI, tag=BankJP No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankNL.list, policy=AI, tag=BankNL, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankNL_Domain.list, policy=AI, tag=BankNL Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankNL_No_Resolve.list, policy=AI, tag=BankNL No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankSG.list, policy=AI, tag=BankSG, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankSG_Domain.list, policy=AI, tag=BankSG Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankSG_No_Resolve.list, policy=AI, tag=BankSG No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUK.list, policy=AI, tag=BankUK, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUK_Domain.list, policy=AI, tag=BankUK Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUK_No_Resolve.list, policy=AI, tag=BankUK No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUS.list, policy=AI, tag=BankUS, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUS_Domain.list, policy=AI, tag=BankUS Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Bank/BankUS_No_Resolve.list, policy=AI, tag=BankUS No Resolve, enabled=true
```
