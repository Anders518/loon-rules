# VirtualFinance

本目录由上游 `VirtualFinance/` 目录自动转换生成。

## 文件

| 文件 | 规则数 | 上游源文件 |
| --- | ---: | --- |
| [`Monzo.list`](./Monzo.list) | 4 | `VirtualFinance/Monzo.yaml` |
| [`Monzo_No_Resolve.list`](./Monzo_No_Resolve.list) | 4 | `VirtualFinance/Monzo_No_Resolve.yaml` |
| [`Paypal.list`](./Paypal.list) | 3 | `VirtualFinance/Paypal.yaml` |
| [`Paypal_No_Resolve.list`](./Paypal_No_Resolve.list) | 3 | `VirtualFinance/Paypal_No_Resolve.yaml` |
| [`Revolut.list`](./Revolut.list) | 3 | `VirtualFinance/Revolut.yaml` |
| [`Revolut_No_Resolve.list`](./Revolut_No_Resolve.list) | 3 | `VirtualFinance/Revolut_No_Resolve.yaml` |
| [`Wise.list`](./Wise.list) | 2 | `VirtualFinance/Wise.yaml` |
| [`Wise_No_Resolve.list`](./Wise_No_Resolve.list) | 2 | `VirtualFinance/Wise_No_Resolve.yaml` |

## Loon Remote Rule 示例

把 `policy=AI` 改成你的实际策略组名。

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Monzo.list, policy=AI, tag=Monzo, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Monzo_No_Resolve.list, policy=AI, tag=Monzo No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Paypal.list, policy=AI, tag=Paypal, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Paypal_No_Resolve.list, policy=AI, tag=Paypal No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Revolut.list, policy=AI, tag=Revolut, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Revolut_No_Resolve.list, policy=AI, tag=Revolut No Resolve, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Wise.list, policy=AI, tag=Wise, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/VirtualFinance/Wise_No_Resolve.list, policy=AI, tag=Wise No Resolve, enabled=true
```
