# YEKAI 2026-11-13 增量修改报告

本次以现有 2026-11-11-r2 网站为基础修改，没有重建网站，也没有部署。西语仍位于 `/es/`，英文仍位于 `/`，没有 IP 自动语言跳转。

## 一、故障修复

- `app.js` 固定资源前缀为 `/`，避免西语动态产品图请求 `/es/images/…`。动态产品链接按语言明确指向 `/products/…/` 或 `/es/products/…/`。
- HTML 图片、CSS、JS 和普通站内链接统一根路径。canonical、hreflang、JSON-LD 继续使用绝对正式网址。
- 新增 `site-refinements.css`：首页内容使用相同容器和间距；页头设置为 64px；移除重复顶部制造商横条；分类栏保留为可滚动的一层；修正通用手机导航定位对其他 nav 的影响。
- 首页标题减小、恢复正常字距，保留两行结构。其他标题使用平衡换行并放宽产品标题容器。实际是否出现标点孤行仍需浏览器确认。
- 目录图片保留原比例，使用 contain；图片文件本身没有修改。

## 二、首屏与转化

- 双语制造商短句、明确副标题及 OEM／小单样品／墨西哥 DDP 三项卖点。
- WhatsApp 成为首屏和导航主要按钮，预填询盘；产品和目录入口保留为文字链接。EN / ES 入口扩大。
- 32 个产品详情页新增侧栏和底部含产品名的 WhatsApp 链接，原有底部配置询盘及 quote.js 不变。
- 保留原包装和印版费信息，补充 DDP 与样品说明。西语首页表单示例和提交按钮使用西语。
- 保留 frank@yekaifrank.com 和现有四个联系渠道。每个渠道在两个首页各有两处可见入口，产品/分类/About 未新增联系方式。
- PDF 按钮已显示，但保持 disabled，并明确 PDF 待发布；没有伪造下载地址。
- 证书卡片已加说明。专利卡片按既有文件名称说明，CE/RoHS/UL 只提示确认适用产品，不能在未核实前写成覆盖所有钢丝轮。
- 首屏原图片未改变；当前无法依据原始产品实拍确认钢丝、螺母和铭文完全一致，这项仍待提供真实原片。

## 三、SEO

- 保留 44 个可索引 URL（英文 22、西语 22），无重定向源网址及 noindex 页面混入 sitemap。
- 44 页均具有自引用 canonical 和 en/es/x-default 互指；x-default 保留英文，因为现有根目录仍为英文。西语广告仍可直接投放 `/es/`。
- 44 页 title 和 meta description 各自唯一，每页一个 H1，描述长度符合已有英 155／西 160 上限；逐页数据见 CSV。
- 16 个西语产品页现有实质正文已达到要求：排除导航、表单、表格、脚本和链接后为 386–633 词。保留真实资料，缺失 MOQ、材质或适配参数继续请客户向 Frank 确认，没有凑字添加虚构参数。
- 首页提供全部 16 个系列的静态链接（与 products.json 顺序一致），产品页保留相关产品内链；没有依赖“加载更多”才能被发现的唯一入口。
- Organization 和 Product 结构化数据沿用现有真实数据，86 段 JSON-LD 可解析。解析成功不等于 Google 产品富媒体资格通过；没有为消除 Product 提示编造 offers、review 或 aggregateRating。
- 截图中的三个重定向来源为 `http://www.yekaifrank.com/`、`http://yekaifrank.com/`、`https://www.yekaifrank.com/`，属于协议/主机别名，未改动规则。本次线上访问失败，实际跳转链和状态码未验证。

## 四、验证结果与边界

| 检查 | 结果 |
|---|---|
| 可索引页面与 sitemap | 44 / 44，通过 |
| canonical、hreflang 互指 | 44 页通过 |
| title / description 唯一性 | 44 / 44，通过 |
| JSON-LD JSON 解析 | 86 段，通过 |
| HTML/CSS 本站引用 | 1,514 次，无缺失文件和锚点 |
| python -m http.server 本地访问 | 98 个不同页面/资源，全部 HTTP 200 |
| 生成脚本连续运行 | 2 次，第二次文件变化为 0 |
| WhatsApp 配置询盘模拟 | 32 页、194 组配置、290 用例，0 失败 |
| 产品数据、图片、quote.js、_redirects | 与原版本哈希一致 |
| 桌面/手机真实渲染及按钮点击 | 未验证：Chromium 因 socket 权限限制无法启动 |
| 线上 Netlify、外部链接、GSC 提交 | 未验证／未提交 |

本地 HTTP 测试使用真实 HTTP 服务，不是 file://。HTTP 200 证明资源可读取，不代表浏览器实际布局和 JavaScript 全流程已完成视觉验收。WhatsApp 检查使用 Node 模拟 DOM，没有向任何人发送消息。旧版本 reports 中的历史结果不代表本次结论，本次以 reports/2026-11-13 为准。

## 五、待提供与待决定

1. 完整目录 PDF 文件。
2. 各证书/报告的覆盖产品、型号与适用范围；不提供则保留确认提示。
3. 未修饰的首屏产品原片，用于核对钢丝、螺母、印字；当前未做生成式改图。
4. Twisted wire wheels / bevel brush 命名由工厂确认，数据未改。
5. 域名邮箱已更新为 frank@yekaifrank.com。
6. 部署前在本机浏览器以 HTTP 打开，检查桌面和手机导航、标题换行、图片和 WhatsApp。当前包不声称视觉验收已通过。

## 六、Search Console 手动操作（正式部署之后）

1. 在“站点地图”确认 `https://yekaifrank.com/sitemap.xml` 提交成功；若已有成功条目，无需每天重复提交。
2. 检查 `/es/` 和最重要的西语产品页，先“测试实际网址”，确认内容与图片可访问，再对新增或实质更新的重点页面请求编入索引。
3. 三个 http/www 别名保持重定向，检查最终目标 `https://yekaifrank.com/` 的索引状态；不要为让旧别名被收录而取消重定向。
4. 对“已发现－尚未编入索引”中的重要产品页观察抓取状态；本站地图和正文更新不能保证收录或排名。
5. Product 富媒体错误须等真实报价/评论数据或结构化数据策略确认后再处理，不能用假价格或假评分消除。

## 七、重新生成

安装 `scripts/requirements.txt`，运行现有 `scripts/build-products.py`；`maintain_seo.py` 会自动执行 `refine_site_20261113.py`。可分别运行 `validate_seo.py`、`check_regeneration.py` 和 `check_nov13.py` 复核。不要跳过维护步骤直接发布中间生成结果。

完整改动文件清单见 `reports/2026-11-13/changed-files.txt`。
