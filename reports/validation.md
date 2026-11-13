# 静态验证结果

命令：`python scripts/validate_seo.py`（退出码0）；另在隔离副本运行`python scripts/build-products.py`后再验证（退出码0）。未将再生成副本覆盖交付版，以免带入旧脚本的其他排版变化。

| 检查 | 交付版 | 完整生成后隔离副本 |
| --- | --- | --- |
| 可索引页面 | 44 | 44 |
| sitemap URL | 44 | 44 |
| JSON-LD可解析 | 86 | 86 |
| HTML/CSS本地资源引用 | 1430 | 1430 |
| 丢失文件/锚点 | 0 | 0 |
| canonical/hreflang/描述一致性错误 | 0 | 0 |

全部44个canonical指向自身，en/es-MX/x-default互指正确；sitemap URL集合与原包一致、均真实存在且非noindex，lastmod均2026-11-10。所有英文description≤155，西语≤160。

标题逐页记录如下；本次只缩短指定的西语打草轮标题。另有西语crimped-wire-brush-wheels标题63字符，超出60的编辑目标，按“只改指定项目”保留并报告；60不是Google硬性字符上限。

| URL | Title字符 | Description字符 | canonical | hreflang互指 |
| --- | --- | --- | --- | --- |
| https://yekaifrank.com/ | 58 | 132 | https://yekaifrank.com/ | 通过 |
| https://yekaifrank.com/about/ | 56 | 147 | https://yekaifrank.com/about/ | 通过 |
| https://yekaifrank.com/abrasive-filament-brush/ | 57 | 149 | https://yekaifrank.com/abrasive-filament-brush/ | 通过 |
| https://yekaifrank.com/abrasive-flap-disc/ | 57 | 155 | https://yekaifrank.com/abrasive-flap-disc/ | 通过 |
| https://yekaifrank.com/es/ | 60 | 155 | https://yekaifrank.com/es/ | 通过 |
| https://yekaifrank.com/es/about/ | 59 | 159 | https://yekaifrank.com/es/about/ | 通过 |
| https://yekaifrank.com/es/abrasive-filament-brush/ | 60 | 158 | https://yekaifrank.com/es/abrasive-filament-brush/ | 通过 |
| https://yekaifrank.com/es/abrasive-flap-disc/ | 56 | 153 | https://yekaifrank.com/es/abrasive-flap-disc/ | 通过 |
| https://yekaifrank.com/es/products/3-and-6-bundle-wire-trimmer-heads/ | 59 | 136 | https://yekaifrank.com/es/products/3-and-6-bundle-wire-trimmer-heads/ | 通过 |
| https://yekaifrank.com/es/products/abrasive-filament-brushes/ | 54 | 134 | https://yekaifrank.com/es/products/abrasive-filament-brushes/ | 通过 |
| https://yekaifrank.com/es/products/abrasive-flap-discs/ | 51 | 150 | https://yekaifrank.com/es/products/abrasive-flap-discs/ | 通过 |
| https://yekaifrank.com/es/products/banded-twisted-cup-brushes/ | 47 | 130 | https://yekaifrank.com/es/products/banded-twisted-cup-brushes/ | 通过 |
| https://yekaifrank.com/es/products/blister-card-brush-sets/ | 53 | 130 | https://yekaifrank.com/es/products/blister-card-brush-sets/ | 通过 |
| https://yekaifrank.com/es/products/copper-coated-wire-wheels/ | 51 | 131 | https://yekaifrank.com/es/products/copper-coated-wire-wheels/ | 通过 |
| https://yekaifrank.com/es/products/crimped-wire-brush-wheels/ | 63 | 144 | https://yekaifrank.com/es/products/crimped-wire-brush-wheels/ | 通过 |
| https://yekaifrank.com/es/products/crimped-wire-cup-brushes/ | 49 | 130 | https://yekaifrank.com/es/products/crimped-wire-cup-brushes/ | 通过 |
| https://yekaifrank.com/es/products/nylon-grass-trimmer-brushes/ | 59 | 140 | https://yekaifrank.com/es/products/nylon-grass-trimmer-brushes/ | 通过 |
| https://yekaifrank.com/es/products/plastic-handle-hand-brushes/ | 60 | 139 | https://yekaifrank.com/es/products/plastic-handle-hand-brushes/ | 通过 |
| https://yekaifrank.com/es/products/red-knotted-wire-cup-brush/ | 59 | 130 | https://yekaifrank.com/es/products/red-knotted-wire-cup-brush/ | 通过 |
| https://yekaifrank.com/es/products/shaft-mounted-wire-wheels/ | 53 | 135 | https://yekaifrank.com/es/products/shaft-mounted-wire-wheels/ | 通过 |
| https://yekaifrank.com/es/products/stringer-knotted-wheels/ | 51 | 127 | https://yekaifrank.com/es/products/stringer-knotted-wheels/ | 通过 |
| https://yekaifrank.com/es/products/twisted-wire-grass-trimmer-heads/ | 45 | 141 | https://yekaifrank.com/es/products/twisted-wire-grass-trimmer-heads/ | 通过 |
| https://yekaifrank.com/es/products/twisted-wire-wheels/ | 50 | 151 | https://yekaifrank.com/es/products/twisted-wire-wheels/ | 通过 |
| https://yekaifrank.com/es/products/wide-crimped-wire-wheels/ | 47 | 130 | https://yekaifrank.com/es/products/wide-crimped-wire-wheels/ | 通过 |
| https://yekaifrank.com/es/steel-wire-wheel-brush/ | 58 | 153 | https://yekaifrank.com/es/steel-wire-wheel-brush/ | 通过 |
| https://yekaifrank.com/es/wire-grass-trimmer-head/ | 57 | 157 | https://yekaifrank.com/es/wire-grass-trimmer-head/ | 通过 |
| https://yekaifrank.com/products/3-and-6-bundle-wire-trimmer-heads/ | 59 | 139 | https://yekaifrank.com/products/3-and-6-bundle-wire-trimmer-heads/ | 通过 |
| https://yekaifrank.com/products/abrasive-filament-brushes/ | 51 | 135 | https://yekaifrank.com/products/abrasive-filament-brushes/ | 通过 |
| https://yekaifrank.com/products/abrasive-flap-discs/ | 45 | 133 | https://yekaifrank.com/products/abrasive-flap-discs/ | 通过 |
| https://yekaifrank.com/products/banded-twisted-cup-brushes/ | 52 | 131 | https://yekaifrank.com/products/banded-twisted-cup-brushes/ | 通过 |
| https://yekaifrank.com/products/blister-card-brush-sets/ | 49 | 116 | https://yekaifrank.com/products/blister-card-brush-sets/ | 通过 |
| https://yekaifrank.com/products/copper-coated-wire-wheels/ | 51 | 131 | https://yekaifrank.com/products/copper-coated-wire-wheels/ | 通过 |
| https://yekaifrank.com/products/crimped-wire-brush-wheels/ | 51 | 141 | https://yekaifrank.com/products/crimped-wire-brush-wheels/ | 通过 |
| https://yekaifrank.com/products/crimped-wire-cup-brushes/ | 50 | 133 | https://yekaifrank.com/products/crimped-wire-cup-brushes/ | 通过 |
| https://yekaifrank.com/products/nylon-grass-trimmer-brushes/ | 53 | 141 | https://yekaifrank.com/products/nylon-grass-trimmer-brushes/ | 通过 |
| https://yekaifrank.com/products/plastic-handle-hand-brushes/ | 53 | 142 | https://yekaifrank.com/products/plastic-handle-hand-brushes/ | 通过 |
| https://yekaifrank.com/products/red-knotted-wire-cup-brush/ | 48 | 127 | https://yekaifrank.com/products/red-knotted-wire-cup-brush/ | 通过 |
| https://yekaifrank.com/products/shaft-mounted-wire-wheels/ | 51 | 134 | https://yekaifrank.com/products/shaft-mounted-wire-wheels/ | 通过 |
| https://yekaifrank.com/products/stringer-knotted-wheels/ | 49 | 136 | https://yekaifrank.com/products/stringer-knotted-wheels/ | 通过 |
| https://yekaifrank.com/products/twisted-wire-grass-trimmer-heads/ | 58 | 135 | https://yekaifrank.com/products/twisted-wire-grass-trimmer-heads/ | 通过 |
| https://yekaifrank.com/products/twisted-wire-wheels/ | 45 | 139 | https://yekaifrank.com/products/twisted-wire-wheels/ | 通过 |
| https://yekaifrank.com/products/wide-crimped-wire-wheels/ | 50 | 123 | https://yekaifrank.com/products/wide-crimped-wire-wheels/ | 通过 |
| https://yekaifrank.com/steel-wire-wheel-brush/ | 53 | 151 | https://yekaifrank.com/steel-wire-wheel-brush/ | 通过 |
| https://yekaifrank.com/wire-grass-trimmer-head/ | 53 | 149 | https://yekaifrank.com/wire-grass-trimmer-head/ | 通过 |

## 未验证

- 浏览器渲染及交互。
- JavaScript运行时动态URL/请求。
- 外部链接可达性。
- 线上Netlify重定向及HTTP响应。
- Google实际收录及富媒体资格。

资源检查覆盖HTML href/src/srcset/poster和CSS url；JavaScript动态生成链接与浏览器实际网络请求未执行。不把静态检查等同于线上HTTP检查或Google富媒体验证。既有Product缺少offers/review/aggregateRating问题不在本次修复范围，未伪造报价、评价。

## 二次复查补充

新增检查单个H1/main/title、唯一SEO标签、标题与OG一致、重复ID、重复主分类导航及产品关键区块完整性。`python scripts/check_regeneration.py`在临时目录连续生成两次：第二次0个文件变化；88个受保护文件哈希不变；44页的语言链接、H1、图片与URL保持不变。Node VM模拟32页、194个配置，290个询盘场景全部通过；此为模拟测试，不是浏览器点击验证。详见recheck-2026-11-10.md。
