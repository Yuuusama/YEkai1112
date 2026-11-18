# 2026-11-16 西语 SEO（墨西哥）修改清单 —— 未部署

背景：GSC 显示 24 页"已发现 - 尚未编入索引"（Google 从未抓取，属新站常见情况）。西语页没有使用墨西哥买家的搜索词 carda / esmeril / pulidora。

## 做了什么
- 18 个西语页面的 title、H1、meta/og description，以及 JSON-LD 中 WebPage/Product 的 name/description，还有面包屑，改为墨西哥常用说法（carda、carda copa、carda circular、para esmeril / pulidora / taladro、desbrozadora）。尺寸、丝径等数字都沿用原页面，没有新增。
- 西语首页 H1：Cepillos de alambre → Cardas y cepillos de alambre。
- 新增 4 个西语页面：/es/guias/（索引页）和 3 篇采购指南（carda 的选择、尺寸/螺纹、从中国进口到墨西哥）。只用了现有页面已有的条款（RMB 300 版费、5,000 件减免、试单、EXW/FOB/CIF、DDP 需报价），没写价格和运输时效。附 Article 及 BreadcrumbList 结构化数据，只有 hreflang=es。
- 内部链接：英西首页 About 区块加入独立 About 页链接；西语首页加"Guías"区块；西语分类页、产品页、页脚加上指南链接；指南正文链接到对应产品页。
- 新增 guides.css。sitemap 由 44 条增加到 48 条，改动过的页面 lastmod 设为 2026-11-16。
- 把 validate_seo.py 和 maintain_seo.py 里写死的"44 页、固定日期"改为"至少 44 页、日期格式校验"。

## 没做什么
- 没有改 products.json 等 4 个产品数据文件、app.js、quote.js、图片和英文页文案。首页产品网格和相关产品链接的文字仍沿用原名（如 Discos de alambre trenzado）。
- 没有部署，没有提交 GSC。

## 怎么维护
跑完其他生成脚本以后，最后执行：`python3 scripts/seo_mx_20261116.py`（重复执行结果不变）。

## 验证
validate_seo.py：48 页 0 错误，JSON-LD 共 93 段全部可解析，本地引用无缺失；validate_contact_channels.py 通过；check_nov13.py 通过（48 个标题、48 条描述都不重复）；脚本连续执行两次结果一致。已用本地 Chrome 截图检查指南页、西语首页和产品页的显示。

# 2026-11-16（二）合并重复尺寸 —— 未部署
- 问题：2026-11-09 新增毫米尺寸时保留了原来的英寸选项，并注明"不是精确对应"，结果同一个尺寸出现两次（例如 3 in 和 75 mm）。
- 处理：同一尺寸只保留一个选项，标成 英寸 (毫米)，例如 3" (75 mm)。对应关系：2.5"=65、3"=75、3.5"=90、4"=100、4.5"=115、5"=125、6"=150、7"=178、8"=200、10"=250、12"=300 mm。没有对应英寸的保留毫米，如 80、85、110 mm。
  - 编织碗刷（id 8）：13 → 8 个选项
  - 波浪丝碗刷（id 10）：11 → 6 个选项
  - 宽面轮刷（id 7）：13 → 7 个选项
  - 斜角刷（id 2）：6 → 3 个选项
- 同步修改：product-configurations.json、product-specs.json 的"系列外径"；4 个产品英西页面的配置选项、configuration-data、规格表；删除单独的"毫米直径"区块。
- 脚本：scripts/merge_sizes_20261116.py（可重复执行）。没有重跑旧的 build_configurations.py，因为它会改动其他 28 个产品页。
- 验证：在浏览器里点选尺寸，规格表和 WhatsApp 预填内容显示正常，页面无 JS 报错；validate_seo 0 错误。

# 2026-11-16（三）文案不再只针对墨西哥 —— 未部署
- 指南改成面向所有西语地区：第三篇改名为 /es/guias/importar-cardas-de-china/（原来的 a-mexico 版本没上线过，直接替换）；补充了 grata、amoladora 这些其他国家的叫法；"墨西哥目的城市"改成"国家和城市"；DDP 写成"按目的国报价，例如墨西哥"。
- 原网站文案：16 个产品页英西两版"……supplying Mexico / en México"那句改为通用说法；About 描述删掉"en México"；西语首屏卖点改为"Exportación a todo el mundo · DDP a México bajo cotización"；西语首页 WhatsApp 预填删掉"en México"。
- 保留：DDP 到墨西哥的说明（这是实际能做的服务），以及询价表单里"目的国"的示例 placeholder。
- 改动都在 seo_mx_20261116.py 的 neutral_copy() 里，同时改了 build-products.py、refine_site_20261113.py、seo-copy.json 的源文案，以后重新生成也不会改回去。

# 2026-11-16（四）产品页加"也叫 / Also known as"——未部署
- 16 个产品页的英西两版（共 32 页），在 H1 下面第一段后加一行常见叫法，把各国说法写进正文（carda、grata、cepillo、pulidora、amoladora、esmeril、taladro、desbrozadora、desmalezadora、guadaña 等）。英文页对应写 angle grinder、bench grinder、drill、brush cutter 等。
- 没用 meta keywords（Google 不看这个），也没有隐藏文字。
- 代码在 seo_mx_20261116.py 的 also_known()；样式加在 guides.css 的 .also-known。

# 2026-11-16（五）宽面轮改为 4–12 寸 + 修结构化数据尺寸 —— 未部署
- 宽面波浪丝轮（id 7）：确认 4 到 12 寸都做。介绍、meta 描述、产品数据文件（products.json、product-specs.json）、首页产品卡、分类页、西语指南里的"4–10 寸"全部改为"4、5、6、7、8、10、12 寸"。选项仍是 4/5/6/7/8/10/12（没有 9、11 寸，如果也做请告诉我）。
- 修了上一版的遗漏：4 个产品页（id 8、10、7、2）JSON-LD 里的"系列外径"原来只有旧的英寸列表（缺 3.5"、80/85/110 mm、12"），现在和页面上的选项一致。
- 代码在 merge_sizes_20261116.py（可重复执行）；seo-copy.json、seo_mx_20261116.py 的源文案也同步改了。
- 验证：validate_seo 0 错误；从原始包重建两次结果一致；没有残留"8 or 10 in"字样。

# 2026-11-16（六）新增 5 篇西语指南 + FAQ —— 未部署，待 Frank 确认内容
- 新增指南（scripts/guides_es_20261116.py）：carda-para-soldadura、carda-para-quitar-oxido-y-pintura、cepillo-para-desbrozadora、cepillo-de-nylon-abrasivo、cardas-con-tu-marca。指南共 8 篇 + 目录页，sitemap 53 条。
- 8 篇指南每篇末尾加 3 个常见问题（页面可见 + FAQPage 结构化数据）。
- 只用产品页已有的数据（尺寸、丝径、束数、粒度 80–320、300 RMB 版费、5,000 件减免）；没有写价格、交期、RPM 数值。
- 产品页底部的指南链接改为每个产品只放最相关的 3 篇。
- 修复：13 个改过名字的西语产品页，WhatsApp 预填消息里的产品名还是旧名字，现在和页面标题一致（check_nov13 之前因此报错，现已 0 错误）。
- 尺寸换算统一：7" = 178 mm。
- 验证：validate_seo 0 错误（53 页、111 段 JSON-LD）；check_nov13 0 错误；validate_contact_channels 通过；指南内部链接无死链；重复构建结果一致。

# 2026-11-16（七）按 Frank 确认修正 —— 未部署
- 磨料丝：80 目最常订（指南正文 + FAQ）。
- 3/6 束除草头：小孔=锂电机，大孔=汽油机。改了指南、FAQ，以及该产品英西页面和 product-specs.json 的采购说明（原文写"不保证适配汽油机"）。具体孔径 mm 待 Frank 提供。
- 碗刷螺纹：常做 M14、M10；5/8"-11 可定制（尺寸指南正文、描述、FAQ）。
- 80/85/110 mm、300 mm 的来源：size-reference-review.json，取自 gb.nipb.com 产品页的尺寸，记录为"Frank 2026-11-09 确认同尺寸可生产"。是否保留待 Frank 决定。

# 2026-11-16（八）删掉不做的尺寸 + 西语产品名统一 —— 未部署
- 删除 80 mm、110 mm（编织碗刷 id 8）和 85 mm（波浪丝碗刷 id 10）。Frank 确认不做。id 8 的 3.5" (90 mm) 保留，待确认。
- 13 个产品的西语名统一成产品页标题的叫法（如 Discos de alambre trenzado → Carda cónica de alambre trenzado），涉及 products.json、首页产品卡、分类页、相关产品链接、图片 alt、WhatsApp 预填。代码在 seo_mx_20261116.py 的 rename_products()。
- 验证：validate_seo、check_nov13、validate_contact_channels 均 0 错误；重复构建结果一致；西语首页产品卡和尺寸选项在浏览器里显示正常。

# 2026-11-17（九）除草头产品页加"是什么 / 哪里买"问答 —— 未部署（计划 11-26 上传）
- 起因：Search Console 里有人搜"… qué es y dónde comprar"并看到了编织除草头页面，但页面没有回答这两个问题。
- 3 个除草头产品页（编织款、3/6 束款、尼龙款）的英西两版，各加 2 个问答：这是什么、批发去哪里买。页面可见，同时加了 FAQPage 结构化数据；西语版附除草刷指南链接。
- "哪里买"的回答不限墨西哥：EXW/FOB/CIF 发任何国家，墨西哥另有 DDP 可报价。
- 代码在 seo_mx_20261116.py 的 product_faq()。验证：validate_seo、check_nov13、validate_contact_channels 均 0 错误；重复构建结果一致。

# 2026-11-17（十）英文全面优化 + Frank 确认的参数 —— 未部署
- 英文指南：新增 /guides/ 目录页 + 8 篇英文指南（scripts/guides_en_20261117.py），每篇 3 个 FAQ（页面可见 + FAQPage）。和西语指南一一配对，hreflang 互相指向，页头 EN/ES 切换跳到对应语言的同一篇。
- 英文标题/H1/描述：首页、4 个分类页、16 个产品页按买家搜索词重写（wire cup brush、angle grinder、bench grinder、stringer bead、drill、brush cutter、weed brush、nylon filament 等）。8 个产品的英文名随 H1 统一（首页产品卡、链接、WhatsApp 预填）。
- 英文内部链接：首页加 Buyer guides 区块；分类页、产品页（每个产品 3 篇最相关指南）、页脚加指南链接。
- 3/6 束除草头孔径：5.5 mm（锂电）、25.4 mm（汽油割灌机），写进产品页说明、描述、FAQ、英西指南。
- 编织碗刷 3.5" (90 mm)：非常规，从尺寸选项里移除，规格表注明"可定制 / on request / bajo pedido"。
- validate_seo.py：指南页的 hreflang 规则改为英西配对。
- 验证：validate_seo 0 错误（62 页、142 段 JSON-LD）；check_nov13 0 错误（62 个标题和描述都不重复）；validate_contact_channels 通过；全站内部链接 0 死链；重复构建结果一致；英文首页、指南页已在浏览器里看过。

# 2026-11-17（十一）全部产品页问答 + About 页扩充 —— 未部署
- 其余 13 个产品页（英西两版）各加 2 个问答："这是什么" 和 "批发去哪里买"，页面可见 + FAQPage。现在 16 个产品页全部都有。问答下面附 3 篇最相关的指南链接。代码数据在 scripts/product_faq_20261117.py。
- About 页（英西）扩充：20 多年制造经验、约 50 名工人、主要产品线、贴牌包装、出口市场（墨西哥、印度、俄罗斯、日本，并通过外贸公司销往各地）、展会（上海五金展、义乌博览会、近两年广交会、每年计划海外展如印尼），加 2 张展会照片（网站原有图片）。标题和描述同步更新。
- 没有写进页面的：年产值（Frank 说不一定全写，销售额一般不公开）、具体建厂年份（只写"20 多年"，以后不用每年改）。
- 西语分类名 "Discos y copas de alambre" → "Cardas y copas de alambre"。
- 验证：validate_seo 0 错误（62 页、168 段 JSON-LD）；check_nov13、validate_contact_channels 通过；重复构建结果一致；About 页已在浏览器里看过。

# 2026-11-17（十二）About 出口市场改写 —— 未部署
- Frank 确认：印度做得很多，墨西哥还在开发。About 页改为"印度是最大市场之一，还有俄罗斯、日本；正在开发墨西哥和拉美"，描述同步。

# 2026-11-17（十三）第二批指南 + 螺纹修正 + 机平实拍图 —— 未部署，待 Frank 审核
- 新增指南（scripts/guides_batch2_20261117.py）：9 个选题英西各一篇 + 印度专题英文 1 篇，共 19 页，每篇 3 个 FAQ。选题：角磨机碗刷怎么选、台式砂轮机钢丝轮、电钻带杆刷、木材拉丝做旧、不锈钢和铝件用什么丝、钢丝刷和百叶片、五金店配货、怎么看质量、安全与转速、印度 4 寸角磨机 M10。
- 原计划的"从中国工厂订货流程"没有单独写，并入现有的进口指南（英西）：加了"30% 定金、发货前付清；大货通常约 30 天，按订单确认；动平衡检测 + 每批抽检"。
- 螺纹修正：M14 螺距 2.0；M10 有 1.5（粗牙）和 1.25（细牙）两种，互不通用，很多 4 寸角磨机是细牙。写进尺寸指南（英西）、FAQ 和新指南。
- 材质（Frank 确认）：碳钢丝、镀铜钢丝、不锈钢丝 304/201、黄铜丝。写进不锈钢/铝指南、质量指南、About 页。
- 机平（台式机用厚款，带变径套）：3 张实拍图做了抠图换底/裁剪（images/bench-wheel-*.webp），放进宽面波浪丝轮产品页（英西），并说明比孔平厚、价格高、多用于台式砂轮机。第 4 张图（桌面拍的那张）背景有别家店的电话和二维码，没用。
- 产品页相关指南改为优先链接新指南。指南总数：英文 18 篇，西语 17 篇。
- 验证：validate_seo 0 错误（81 页、225 段 JSON-LD）；check_nov13、validate_contact_channels 通过；全站链接和图片 0 缺失；重复构建结果一致。

# 2026-11-17（十四）按 Frank 审核意见修改 —— 未部署
- 平面轮对应关系（Frank 确认）：扭平 = Stringer knotted wheels 页；孔平 = 宽面波浪丝轮页（4–12 寸）；机平 = 同页的"台式机厚款"区块，尺寸与孔平相同（4、5、6、7、8、10、12 寸），已补上介绍和尺寸。台式机指南（英西）的产品链接按此调整。
- 印度指南：M10×1.5 为常规，M10×1.25 可定制。
- 碗刷指南、台式机钢丝轮指南（英西）加"使用建议"：轻压、新刷先空转约一分钟、碗刷端面贴平、台式轮定期翻面、磨短或抖动就更换。

# 2026-11-18（十五）参考同行网站：证书区块 + PDF 目录下载 —— 未部署
- 参考 nipb.com（宁波兴宝华）：对方的强项是规格表详细、资质展示和 PDF 下载。只借鉴做法，没有用对方的数据、图片和文字。
- About 页（英西）加"证书、检测报告和专利"区块：CE、RoHS、UL 62841-1 检测报告，以及钢丝轮实用新型、除草头外观设计两项专利，都是网站原有文件。另加 PDF 目录下载按钮。
- 新增 downloads/yekai-wire-brush-catalog.pdf：用网站原有的 14 页目录图合成。首页原来那个灰色、点不了的"Download full catalog (PDF)"按钮改成可以下载。
- 规格表：从自家目录第 1–9 页抄出 131 行（型号、外径、B、L、孔径或杆径、最高转速、丝径、装箱数、外箱尺寸），做成 YEKAI_产品规格表_核对.xlsx 给 Frank 核对。核对后再做进网站，这一版网站还没改规格表。
- 验证：validate_seo、check_nov13、validate_contact_channels 均 0 错误；PDF 返回 200 application/pdf；About 页已在浏览器里看过。

# 2026-11-18（十六）撤掉 PDF 目录下载 —— 未部署
- Frank 说印刷目录和现在的产品对不上，所以撤掉 r15 加的 PDF 下载（首页按钮恢复成原来的"待发布"状态，About 页的下载按钮也删掉了），downloads/ 文件夹删除。证书区块保留。
- 网站首页"目录"栏里展示的目录图片还是旧目录，等规格表核对完再一起处理。

# 2026-11-18（十七）按价目表更正规格 —— 未部署
- 新脚本 scripts/price_list_20261118.py（在 merge_sizes 之后运行）。不公布价格。
- 11 个产品页（曲丝碗、扭丝碗、扭杯、孔平/机平、扭平、扭盘/曲盘、除草轮、3/6 股、尼龙、磨料、杆刷）：配置选项改成价目表里的尺寸，规格表后加"尺寸、重量和包装"表（单只重量、装箱数、箱规）；价目表里没有的数据写"Ask Frank"。
- 7 寸统一为 175 mm；扭平改为 4–8 寸（115 无包装数据）；扭杯 3.5 寸 = 85 mm；扭盘加曲盘款；8 寸除草轮加 24 股；尼龙孔径 24.5 mm；磨料改为新尺寸（6 mm 六角柄）；杆刷改为 38–100 mm 轮/碗、10–30 mm 笔刷。
- 磨料页删掉旧目录型号表；这 11 页的"查看原目录"链接删掉。
- 全站：交期 10–30 天；螺纹只有 M10×1.5 是常规，M10×1.25、M14、5/8"-11 写定制；定制印刷插卡每款起订 3000 只，以下用标准卡；版费仍 300 元/版。
- 未加新产品（手刷、迷你套装、吸塑套装等先不加）。
- 首页"购买指南"区块：原来 17 条红色链接的清单，改成 6 张精选指南卡片（标题＋一句简介）＋"查看全部 18 篇指南"按钮；其余指南都在指南页。
- 钢丝直径（Frank 确认）：曲丝（波浪丝）全部 0.3 mm，扭丝全部 0.5 mm。规格表去掉"按型号确认"，配置选项和包装表都加上钢丝直径。
- 西语用墨西哥常用叫法：钢丝直径写 calibre（diámetro del alambre），中心孔写 barreno（orificio central）。
- 3/6 股除草头也是扭丝 0.5 mm；带杆刷按丝的种类：曲丝 0.3 mm / 扭丝 0.5 mm。
- 磨料尼龙刷：标准 80 目、1.3 mm 磨料丝；60 目、120 目和更软/更硬的丝可定制。全站原"80–320 目"的说法都改掉了。
- 扭丝除草轮、尼龙除草刷孔径改为 25.4 mm（之前误写 24.5）；尼龙除草刷保持"普通尼龙扁丝，无磨料"。
- 带杆刷（轮、碗、笔刷）看图都是曲丝，统一写 0.3 mm。
- 新指南（英西各一篇）："钢丝刷尺寸、重量、装箱表"——11 个产品所有有数据的尺寸，加每箱体积 m³、约每立方米只数、每箱钢丝刷重量（按价目表计算，不含价格）。11 个产品页的包装表下面都链接到这篇。
- 首页公司结构化数据加建厂年份（2002）和员工数（约 50）。
- 两张大图压缩（展会照片 458→205 KB，台式机轮合照 411→281 KB）。
- products.json 等数据文件里的旧目录文字也一起更正。
