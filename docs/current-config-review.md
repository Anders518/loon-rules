# Current Loon Config Review

基于用户当前 Loon 配置的优化建议。敏感字段、订阅 URL、证书和 passphrase 不写入本仓库。

## 当前结构判断

当前配置大体是：

```text
手动节点 / 远程订阅
  -> 地区 Remote Filter
  -> 地区 select / url-test / load-balance
  -> 业务策略组：主代理、AI、Crypto、BANK-US、wg
  -> 本地 Rule + Remote Rule
  -> 插件层
```

这个结构可用，不建议完全重写。更适合做成“现有配置 + 自动生成规则 + 精简重复规则”的模式。

## 优先级最高的优化

### 1. 敏感业务不要走负载均衡

银行、交易所、支付、强风控服务应尽量固定出口 IP。当前 `BANK-US` 和 `Crypto` 的方向是对的，但建议继续保持手动选择，不要让它们走 `load-balance`。

推荐：

```ini
BANK-US = select,美国BK节点,美国节点,DIRECT,img-url = banknote
Crypto = select,新国节点,美国节点,香港节点,img-url = bitcoinsign.circle
AI = select,新国策略,美国策略,新国节点,美国节点,img-url = person.circle
```

说明：

- `BANK-US`：优先 BK，美国备用；不要负载均衡。
- `Crypto`：优先稳定区域，避免频繁切 IP。
- `AI`：可用地区策略，也保留手动节点兜底。

### 2. 降低 url-test / load-balance 频率

当前多个地区策略使用 `interval = 60`，地区越多，后台测试越频繁。若目标是省电，建议改为：

```ini
香港时延优选 = url-test,香港节点,interval = 300,tolerance = 50
台湾时延优选 = url-test,台湾节点,interval = 300,tolerance = 50
日本时延优选 = url-test,日本节点,interval = 300,tolerance = 50
韩国时延优选 = url-test,韩国节点,interval = 300,tolerance = 50
新国时延优选 = url-test,新国节点,interval = 300,tolerance = 50
美国时延优选 = url-test,美国节点,interval = 300,tolerance = 50
```

负载均衡也建议从 60 改到 300 或更高。游戏场景除外。

### 3. Remote Rule 去重

当前同时使用了：

```text
Advertising_Domain + Advertising
China_Domain + China
Claude / OpenAI / AI.lsr
China.list + REGION_SPLITTER
```

这会提高规则数量和维护复杂度。推荐方案：

- `LAN` 放在最前；
- 广告只保留一组主规则；
- 中国规则保留 `REGION_SPLITTER` + 一组 China；
- AI 规则使用本仓库生成的 Accademia 规则作为补充，不要和太多综合 AI 规则重复堆叠。

推荐顺序：

```ini
[Remote Rule]
# 1. 局域网 / 中国区域
https://kelee.one/Tool/Loon/Lsr/LAN_SPLITTER.lsr, policy=DIRECT, tag=LAN, enabled=true
https://kelee.one/Tool/Loon/Lsr/REGION_SPLITTER.lsr, policy=DIRECT, tag=CN REGION, enabled=true

# 2. 广告 / 隐私
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Advertising/Advertising.list, policy=REJECT, tag=AD, enabled=true

# 3. 中国直连
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/China/China.list, policy=DIRECT, tag=China, enabled=true

# 4. AI 细分
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/OpenAI/OpenAI_Domain.list, policy=AI, tag=OpenAI Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/OpenAI/OpenAI_IP.list, policy=AI, tag=OpenAI IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Claude/Claude_Domain.list, policy=AI, tag=Claude Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Claude/Claude_IP.list, policy=AI, tag=Claude IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_Domain.list, policy=AI, tag=Gemini Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_IP.list, policy=AI, tag=Gemini IP, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_Domain.list, policy=AI, tag=Copilot Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Copilot/Copilot_IP.list, policy=AI, tag=Copilot IP, enabled=true

# 5. 金融 / Crypto / Telegram
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/PayPal/PayPal.list, policy=BANK-US, tag=Paypal, enabled=true
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Crypto/Crypto.list, policy=Crypto, tag=Crypto, enabled=true
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram.list, policy=主代理, tag=Telegram, enabled=true
```

如需规则源互备，可以保留 `AI.lsr`，但建议先禁用，观察 Accademia + blackmatrix7 是否已经足够：

```ini
https://kelee.one/Tool/Loon/Lsr/AI.lsr, policy=AI, tag=AI Backup, enabled=false
```

### 4. 本地 Rule 保持短而高优先级

本地 `[Rule]` 建议只放非常个人化、必须抢先匹配的规则：

```ini
[Rule]
DOMAIN-SUFFIX,zozo.com,日本策略
DOMAIN-SUFFIX,rakuten.co.jp,日本策略
DOMAIN-SUFFIX,zozo.jp,日本策略
DOMAIN-SUFFIX,melonbooks.co.jp,日本策略
DOMAIN-SUFFIX,booth.pm,日本策略
DOMAIN-SUFFIX,dmm.com,日本策略
DOMAIN-SUFFIX,dmm.co.jp,日本策略
DOMAIN-SUFFIX,dlsite.com,日本策略
DOMAIN-KEYWORD,duolingo,主代理
DOMAIN-KEYWORD,webank,DIRECT
DOMAIN-SUFFIX,linkcube.org,DIRECT
DOMAIN-SUFFIX,gafuru.com,DIRECT
DOMAIN-SUFFIX,msmp.abchina.com.cn,REJECT
IP-CIDR,10.8.0.0/16,wg
DOMAIN-SUFFIX,lilillib.net,DIRECT
FINAL,主代理
```

注意检查 `lilillib.net` 是否拼写正确。当前 `real-ip` 中出现的是 `*.lililib.net`，本地规则里是 `lilillib.net`，两者拼写不同。

### 5. MITM 配置应清理重复字段

当前 `[Mitm]` 里存在重复的 `ca-p12` / `ca-passphrase` 字段，并且 `hostname =` 为空。建议：

- 不需要 MITM 时，保持 `hostname =` 为空，并移除重复证书字段；
- 不要把证书、passphrase、订阅 URL 提交到 GitHub；
- 只对确实需要重写/脚本的域名启用 MITM。

推荐骨架：

```ini
[Mitm]
skip-server-cert-verify = false
hostname =
```

如果必须启用 MITM，请在本地私有配置里保留证书，不要同步到仓库。

## 建议的落地方式

1. 保留你的现有节点订阅、Remote Filter、插件设置；
2. 把 `interval = 60` 批量调成 `interval = 300`；
3. 把 AI 规则切换到本仓库生成的 `rules/OpenAI`、`rules/Claude`、`rules/Gemini`、`rules/Copilot`；
4. 清理重复的广告、中国、AI 远程规则；
5. 敏感业务继续使用手动 select，不使用负载均衡；
6. 清理 `[Mitm]` 重复字段。

## 白名单还是黑名单

你当前 `FINAL,主代理` 更接近黑名单 / 全局兜底代理。若你希望“常驻 VPN 但国内 App 几乎无感”，建议未来改成：

```ini
GEOIP,CN,DIRECT
FINAL,DIRECT
```

并只让明确列出的海外服务走 `主代理` / `AI` / `Crypto` / `BANK-US`。这就是本仓库 `templates/loon/loon_whitelist.conf` 的方向。

如果你更看重海外流量不漏走直连，则继续保留：

```ini
FINAL,主代理
```

也就是当前配置方向。