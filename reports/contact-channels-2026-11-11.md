# 2026-11-11 首页联系方式修改报告

本次在上一版完整网站上增量修改，未部署。仅两个首页新增联系入口；产品、分类、About页面未改。

## 可见入口计数

每格的2次分别是联系区1次、页脚1次。

| 页面 | 邮箱 | Facebook | Messenger | Instagram |
| --- | ---: | ---: | ---: | ---: |
| https://yekaifrank.com/ | 2 | 2 | 2 | 2 |
| https://yekaifrank.com/es/ | 2 | 2 | 2 | 2 |
| 其他所有HTML页面 | 0 | 0 | 0 | 0 |

两个首页共有16个新增链接和16个内联SVG。邮箱标签显示完整邮箱地址，其他标签使用平台品牌名；英语/西语aria-label分别对应各页面语言。所有新增链接均带target="_blank"与rel="noopener noreferrer"；SVG使用currentColor和aria-hidden="true"，没有外部图标引用。

源码字面计数与可见入口不同：每个首页邮箱文本共6次（2个标签、2个mailto、2个JSON-LD字段），Facebook链接3次（2个可见入口、1个sameAs），Messenger链接2次（仅可见入口），Instagram链接3次（2个可见入口、1个sameAs）。联系方式还保存在生成用JSON数据源中，不代表其他页面暴露。

## Organization

- 两个首页增加email和sales contactPoint，联系电话沿用原有+86 19883954016，availableLanguage为English和Spanish。
- sameAs仅包含Facebook和Instagram主页；Messenger不在sameAs中。
- 没有添加Logo、占位符、其他账号或新的电话号码。

## 文件变更

修改5个已有文件：

| 文件 | 修改内容 |
| --- | --- |
| index.html | 英文联系区、页脚、Organization及本地CSS引用 |
| es/index.html | 西语同上 |
| scripts/maintain_seo.py | 在公共生成收尾流程调用联系方式生成器 |
| scripts/check_regeneration.py | 每轮生成后加入联系方式检查 |
| REVIEW-NOTES.txt | 追加本次记录，标明邮箱及社媒已提供 |

新增8个文件：

| 文件 | 用途 |
| --- | --- |
| contact-channels.css | 首页次要渠道样式，22px图标及最小44×44px链接区域 |
| scripts/contact-channels.json | 真实联系方式和英西语无障碍标签 |
| scripts/build_contact_channels.py | 内联SVG、首页HTML及Organization的可重复生成 |
| scripts/validate_contact_channels.py | 页面范围、计数、旧ID、JSON-LD和资源引用检查 |
| reports/contacts-validation-2026-11-11.json | 联系方式详细检查结果 |
| reports/seo-validation-2026-11-11.json | 44个可索引页面的逐页SEO及链接检查 |
| reports/regeneration-validation-2026-11-11.json | 两轮重新生成及询盘模拟结果 |
| reports/contact-channels-2026-11-11.md | 本报告 |

除上述文件外，原有文件与上一版逐字节相同；首页去除这次新增块及Organization字段后，原有内容不变（JSON序列化空白不计）。没有改产品顺序、数据、图片、URL、语言切换、WhatsApp、已有标题或描述。

## 验证结果

| 检查 | 实测结果 |
| --- | --- |
| 联系方式出现范围与位置 | 仅两个首页；每个渠道联系区/页脚各1次 |
| 旧Facebook数字ID | 源码及交付包扫描0处 |
| dist/ | 原包及当前包均不存在；netlify.toml发布根目录，未创建dist |
| 新增外部脚本/样式/图片引用 | 0；新增图标全部内联、CSS仅本地引用 |
| 既有外部资源 | style.css原有1条Google Fonts样式引用，保持不变；不能称整个原站完全无外部请求 |
| 全站JSON-LD解析 | 86段通过json.loads |
| sitemap与可索引页面 | 44个，真实文件、非noindex、canonical一致 |
| canonical/hreflang互指 | 44个页面通过 |
| title/description | 保留原值；逐页字符数见JSON，已有西语1个63字符title未改 |
| 本地HTML/CSS链接与资源引用 | 1432个，缺文件0，缺锚点0 |
| 连续重新生成 | 2轮成功；第二轮0文件变化，入口未丢失/重复 |
| 受保护文件 | 88个保持不变 |
| 离线WhatsApp询盘模拟 | 32页、194种配置、290个场景、0失败 |
| 浏览器渲染 | **未验证**；Chromium启动因socket权限限制失败 |
| 手机显示与实际触控区域 | **未验证**；静态CSS明确min-width/min-height 44px |
| 图标实际渲染样子 | **未验证**；已检查SVG路径、尺寸及currentColor/aria属性 |
| 运行时网络请求 | **未验证**；本次0新增外部资源是源码差异检查结论 |
| 邮箱投递、账号可达性、线上Netlify/GSC | **未验证**；未发送消息、未部署 |

复核命令（网站根目录）：

```text
python scripts/validate_contact_channels.py
python scripts/validate_seo.py
python scripts/check_regeneration.py
```

对比上一版时，联系方式检查可追加`--baseline /path/to/previous/site`。重新生成可运行原有`python scripts/build-products.py`；生成器会自动补齐首页联系方式，不修改产品JSON或询盘脚本。

## 待确认

本次四个渠道均已按提供值写入，无新增资料缺口。上线前请在真实浏览器和手机上确认图标显示、链接点击及WhatsApp仍为主要询盘入口。本次没有处理旧报告中需要工厂确认的产品命名、空壳页、产品富媒体资格等事项。
