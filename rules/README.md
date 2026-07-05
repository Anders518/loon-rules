# Loon Rules Index

规则按上游目录分类保存。每个分类目录都有自己的 `README.md` 和 Loon 引用示例。

默认示例使用 `policy=AI`，请改成你自己 Loon 配置里的策略组名。

## 分类

| 分类 | 规则数 | 目录 |
| --- | ---: | --- |
| `Alipan` | 3 | [`rules/Alipan/`](./Alipan/) |
| `Apple` | 4 | [`rules/Apple/`](./Apple/) |
| `AppleAI` | 3 | [`rules/AppleAI/`](./AppleAI/) |
| `AppleNews` | 3 | [`rules/AppleNews/`](./AppleNews/) |
| `Aqara` | 7 | [`rules/Aqara/`](./Aqara/) |
| `BaiduNetDisk` | 3 | [`rules/BaiduNetDisk/`](./BaiduNetDisk/) |
| `Bank` | 30 | [`rules/Bank/`](./Bank/) |
| `BlockHttpDNSPlus` | 2 | [`rules/BlockHttpDNSPlus/`](./BlockHttpDNSPlus/) |
| `China` | 3 | [`rules/China/`](./China/) |
| `ChinaDNS` | 4 | [`rules/ChinaDNS/`](./ChinaDNS/) |
| `ChinaMax` | 4 | [`rules/ChinaMax/`](./ChinaMax/) |
| `Copilot` | 3 | [`rules/Copilot/`](./Copilot/) |
| `FakeLocation` | 20 | [`rules/FakeLocation/`](./FakeLocation/) |
| `Fastly` | 3 | [`rules/Fastly/`](./Fastly/) |
| `Gemini` | 3 | [`rules/Gemini/`](./Gemini/) |
| `GeoRouting_For_Domain` | 51 | [`rules/GeoRouting_For_Domain/`](./GeoRouting_For_Domain/) |
| `GeoRouting_For_IP` | 34 | [`rules/GeoRouting_For_IP/`](./GeoRouting_For_IP/) |
| `GeositeCN` | 4 | [`rules/GeositeCN/`](./GeositeCN/) |
| `GlobalDNS` | 4 | [`rules/GlobalDNS/`](./GlobalDNS/) |
| `Grok` | 3 | [`rules/Grok/`](./Grok/) |
| `HijackingPlus` | 2 | [`rules/HijackingPlus/`](./HijackingPlus/) |
| `HomeIP` | 4 | [`rules/HomeIP/`](./HomeIP/) |
| `Kwai` | 3 | [`rules/Kwai/`](./Kwai/) |
| `MacAppUpgrade` | 3 | [`rules/MacAppUpgrade/`](./MacAppUpgrade/) |
| `MicrosoftAPPs` | 3 | [`rules/MicrosoftAPPs/`](./MicrosoftAPPs/) |
| `Parsec` | 3 | [`rules/Parsec/`](./Parsec/) |
| `Pornhub` | 3 | [`rules/Pornhub/`](./Pornhub/) |
| `PreRepairEasyPrivacy` | 8 | [`rules/PreRepairEasyPrivacy/`](./PreRepairEasyPrivacy/) |
| `RustDesk` | 3 | [`rules/RustDesk/`](./RustDesk/) |
| `Signal` | 3 | [`rules/Signal/`](./Signal/) |
| `UnsupportVPN` | 3 | [`rules/UnsupportVPN/`](./UnsupportVPN/) |
| `VirtualFinance` | 8 | [`rules/VirtualFinance/`](./VirtualFinance/) |
| `WaybackMachine` | 4 | [`rules/WaybackMachine/`](./WaybackMachine/) |
| `WeiYun` | 4 | [`rules/WeiYun/`](./WeiYun/) |
| `eMuleServer` | 3 | [`rules/eMuleServer/`](./eMuleServer/) |

## 常用示例

### Gemini

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini.list, policy=AI, tag=Gemini, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_Domain.list, policy=AI, tag=Gemini Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_No_Resolve.list, policy=AI, tag=Gemini No Resolve, enabled=true
```

### Copilot

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot.list, policy=AI, tag=Copilot, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_Domain.list, policy=AI, tag=Copilot Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_No_Resolve.list, policy=AI, tag=Copilot No Resolve, enabled=true
```

