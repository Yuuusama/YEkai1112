# YEKAI SEO 改进记录 | 2026-11-08

基线：Library 中 `yekai-seo-deploy.zip`，对原有代码增量修改，不是重建。

## 已执行
- 处理了 44 个真实 HTML 页面（英文+西班牙语），对非首页加入 BreadcrumbList JSON-LD。
- 为 8 个英文/西语产品分类页补充了原创采购指南，涵盖选型对比、询盘需要的参数、机器兼容提醒。
- 保留 Product 数据、现有参数表、WhatsApp 询盘、图片、网站结构、语言切换以及现有 robots、sitemap。
- 未编造尺寸、转速、材质、认证或产品性能，待工厂核实参数继续保留原样。

## 竞品页面参考（人工审阅，不等于证实其关键词排名）
1. WORKPRO / GreatStar：`https://www.workprotool.com/pta/grinding-tools/wheel-brush/knotted-wire-brush.html`：产品型号、规格、包装、用途；但页面有 knotted/crimped 描述混用，烨凯不能照抄。
2. Abtex：`https://www.abtex.com/our-products/abrasive-filament-brushes/`：针对实际应用、丝材和磨粒的解释以及相关资料链接。
3. Newtech：`https://newtech-sources.com/products/standard-heavy-duty-knotted-twist-wire-wheel-brush`：结构化型号、规格、询价入口，但具体数字不能用于烨凯。

## 需要进一步验证（未在本次声称完成）
- Netlify 线上真实页面 HTTP 状态和 GSC 索引状态；外部访问 yekaifrank.com 本次受限。
- 竞争对手搜索排名、反向链接权重、AI 推荐出现次数：需要专业工具或重复测试，不能从单次页面审阅推断。
- 2026 年 5 月 Google 已取消 FAQ 富媒体搜索结果；保留有用的 FAQ 正文，但不批量堆 FAQ Schema。
- 目前网站 B2B 不公开价格：Product JSON-LD 不虚构 Offer、价格、评分或库存。
- 发布前用 Google Rich Results Test、Search Console、Netlify Deploy Preview 检查；上线后看自然展示/点击/WhatsApp 实际线索质量。

## 后续建议
优先把重点产品页面中的参数待核实项由工厂确认，建立每个系列明确的 SKU/图片/用途/安全转速资料，然后再补更深入的对比表。
