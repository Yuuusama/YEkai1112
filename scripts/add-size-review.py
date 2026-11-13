from pathlib import Path
import json,re,html,sys
R=Path(__file__).resolve().parents[1]
load=lambda f:json.loads((R/f).read_text())
configs=load('product-configurations.json'); specs=load('product-specs.json');products=load('products.json');mapping=load('product-map.json')
# Diameter only: Frank confirmed supply capability, 2026-11-09. No competitor RPM/SKU imported.
groups=[('10','曲丝杯刷','Crimped cup brush','Copa de alambre ondulado',[65,75,85,100,125,150],[45,46]),('8','扭结杯刷','Knotted cup brush','Copa de alambre trenzado',[65,75,80,90,100,110,125,150],[49,50,51]),('2','扭结斜角刷','Knotted bevel brush','Cepillo cónico trenzado',[100,115,125],[53]),('7','台式轮刷系列','Crimped bench wheel brush','Cepillo circular ondulado',[100,125,150,178,200,250,300],[44]),('5','扭结端刷','Knotted end brush','Cepillo de punta trenzado',[19,22,25,30],[52]),('5','曲丝端刷','Crimped end brush','Cepillo de punta ondulado',[16,19,22,25,30],[52])]
records=[]
for pid,cn,en,es,sizes,src in groups:
 configs[pid]=[c for c in configs.get(pid,[]) if c.get('sizeSource')!=en]
 for d in sizes:
  rows=[{'en':['Brush form',en],'es':['Forma',es]},{'en':['Outside diameter',f'{d} mm'],'es':['Diámetro exterior',f'{d} mm']}]
  for a,b in [('Wire material / diameter','Material / diámetro del alambre'),('Bore / thread / shank','Orificio / rosca / vástago'),('Maximum safe RPM','RPM máximas seguras'),('Pieces / pack','Piezas / empaque')]:rows.append({'en':[a,'Ask Frank.'],'es':[b,'Consulta a Frank.']})
  configs[pid].append({'en':f'{en} · {d} mm','es':f'{es} · {d} mm','rows':rows,'sizeSource':en})
 records.append({'productId':int(pid),'form':cn,'diameters_mm':sizes,'sources':[f'http://gb.nipb.com/product_detail/{x}.html' for x in src],'confirmation':'Frank confirmed same-size production capability on 2026-11-09; other specifications not imported.'})
for f,d in [('product-configurations.json',configs),('size-reference-review.json',records)]: (R/f).write_text(json.dumps(d,ensure_ascii=False,indent=2))
# Rebuild only configurators; preserve existing SEO, URLs and customized pages.
sys.path.insert(0,str(R/'scripts'))
from build_configurations import build
build(R)
for p in products:
 pid=str(p['id'])
 for lang in ['en','es']:
  path=R/('es' if lang=='es' else '')/'products'/mapping[pid]['slug']/'index.html';t=path.read_text();e=lang=='es'
  t=re.sub(r'<section id="available-diameters">.*?</section>','',t,flags=re.S)
  relevant=[g for g in groups if g[0]==pid]
  if relevant:
   block='<section id="available-diameters"><h2>'+('Diámetros disponibles en milímetros' if e else 'Available metric diameters')+'</h2>'
   for _,cn,en,es,sizes,src in relevant:block+='<h3>'+html.escape(es if e else en)+'</h3><p>'+', '.join(map(str,sizes))+' mm</p>'
   block+='<p>'+('Las opciones en milímetros y pulgadas se indican por separado; no son equivalencias exactas. Confirma el diámetro final, montaje y RPM con Frank. Las fotografías muestran la serie.' if e else 'Metric and inch options are listed separately; they are not exact equivalents. Confirm final diameter, mounting and safe RPM with Frank. Photographs represent the series.')+'</p></section>'
   t=t.replace('<section id="buying-notes">',block+'<section id="buying-notes">')
  path.write_text(t)
# Add meaningful family navigation on both wire category pages.
for lang in ['en','es']:
 e=lang=='es';path=R/('es' if e else '')/'steel-wire-wheel-brush/index.html';t=path.read_text()
 t=re.sub(r'<nav id="brush-family-links".*?</nav>','',t,flags=re.S)
 labels=[('10','Crimped cup brushes','Copas onduladas'),('8','Knotted cup brushes','Copas trenzadas'),('2','Bevel brushes','Cepillos cónicos'),('7','Wheel brushes','Cepillos circulares'),('5','Shank and end brushes','Cepillos con vástago y de punta')]
 nav='<nav id="brush-family-links" aria-label="'+('Formas de cepillo' if e else 'Brush shapes')+'" class="category-navigation">'+''.join('<a href="../products/'+mapping[i]['slug']+'/">'+(b if e else a)+'</a>' for i,a,b in labels)+'</nav>'
 t=t.replace('<div class="range-grid">',nav+'<div class="range-grid">');path.write_text(t)
# Private review landing page excluded from sitemap and search indexing.
rows=''.join('<tr><th>'+g[1]+'</th><td>'+', '.join(map(str,g[4]))+' mm</td><td><a href="products/'+mapping[g[0]]['slug']+'/">英文预览</a> · <a href="es/products/'+mapping[g[0]]['slug']+'/">西语预览</a></td><td>'+''.join('<a href="http://gb.nipb.com/product_detail/'+str(n)+'.html">来源'+str(n)+'</a> ' for n in g[5])+'</td></tr>' for g in groups)
review='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>烨凯尺寸检查表 · 2026-11-09</title><style>body{font:16px/1.7 system-ui;margin:40px auto;padding:0 24px;max-width:1100px;color:#17232c}h1{font-size:30px}table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:18px 12px;border-bottom:1px solid #ddd}a{color:#a52d25}header{border-top:6px solid #a52d25}small{color:#58636c} @media(max-width:700px){table{font-size:13px}td,th{padding:10px 5px}}</style></head><body><header><p>YEKAI · 内部检查版 · 未部署</p><h1>产品尺寸与选项检查表</h1></header><p>根据Frank确认的生产能力，补充下面的毫米尺寸。原有16款产品、图片、排序、英西语网址均保留。现有英寸选项继续保留，不宣称与毫米尺寸精确等同。</p><table><thead><tr><th>产品类型</th><th>本次新增选项</th><th>检查页面</th><th>尺寸来源</th></tr></thead><tbody>'''+rows+'''</tbody></table><h2>请重点检查</h2><ol><li>产品类型和对应图片是否一致，尤其是台式轮刷及端刷。</li><li>尺寸是否都能接单；英寸与毫米选项是否需要合并。</li><li>后续补充各尺寸的丝径、材质、接口、包装及安全转速。</li></ol><p>新增选项中的未确认参数显示“Ask Frank / Consulta a Frank”。没有复制对方货号、转速、认证、照片或报价。其余未明确对应的产品尺寸暂不混入现有型号。</p><p><a href="index.html">查看完整英文首页</a> · <a href="es/index.html">查看完整西语首页</a></p><small>解压文件包后打开本页，可点击预览；如浏览器限制本地脚本，请用本地HTTP预览。正式部署前删除此内部检查页及size-reference-review.json。</small></body></html>'''
(R/'REVIEW-SIZES.html').write_text(review)
print('Updated 32 bilingual product configurators; added',sum(len(g[4]) for g in groups),'metric choices across 5 product pages.')
