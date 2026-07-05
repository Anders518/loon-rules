# Loon Rules

把 `Accademia/Additional_Rule_For_Clash` 的 Mihomo / Clash 规则集自动转换成 Loon 可用的 `.list` 远程规则，并提供参考 Loon 配置模板。

## 目录结构

转换后会按上游分类目录保存：

```text
rules/
  README.md
  Gemini/
    README.md
    Gemini_Domain.list
    Gemini_IP.list
  OpenAI/
    README.md
    OpenAI_Domain.list
    OpenAI_IP.list
```

这样每类规则不会全部堆在同一个文件夹里。

模板文件保存在：

```text
templates/loon/
  README.md
  loon_whitelist.conf
  loon_blacklist.conf
```

## 使用方式

第一次 Actions 跑完后，先看：

```text
rules/README.md
```

里面会列出所有分类和常用 Loon 引用示例。

每个分类目录也会有自己的说明文件，例如：

```text
rules/Gemini/README.md
rules/OpenAI/README.md
```

如果想直接套用配置骨架，看：

```text
templates/loon/README.md
```

## Loon 示例

```ini
[Remote Rule]
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_Domain.list, policy=AI, tag=Gemini Domain, enabled=true
https://raw.githubusercontent.com/Anders518/loon-rules/main/rules/Gemini/Gemini_IP.list, policy=AI, tag=Gemini IP, enabled=true
```

把 `policy=AI` 改成你 Loon 中真实存在的策略组名。

## 模板选择

- `templates/loon/loon_whitelist.conf`：白名单模式。国内和未命中流量默认直连，只有明确列出的海外服务走代理。
- `templates/loon/loon_blacklist.conf`：黑名单模式。国内直连，海外服务和未命中流量默认代理。

## 自动更新

GitHub Actions 每 6 小时自动运行一次，也可以手动运行：

```text
Actions -> Sync Loon Rules -> Run workflow
```

每次运行会：

1. 扫描上游所有 `.yaml` / `.yml` 规则集；
2. 按上游目录分类生成 `rules/<分类>/*.list`；
3. 生成 `rules/README.md` 和每个分类目录的 `README.md`；
4. 提交更新后的规则和说明文件。

## 转换说明

支持的主要转换：

```text
+.example.com    -> DOMAIN-SUFFIX,example.com
example.com      -> DOMAIN,example.com
1.2.3.0/24       -> IP-CIDR,1.2.3.0/24,no-resolve
2001:db8::/32    -> IP-CIDR6,2001:db8::/32,no-resolve
```

已经是兼容格式的 classical 规则会保留，例如：

```text
DOMAIN-SUFFIX,example.com
IP-CIDR,1.2.3.0/24,no-resolve
```

不适合直接转换到 Loon 的 Mihomo / Clash 专用规则类型会被跳过，并记录在：

```text
build/summary.md
```
