import json,re,html
def build(R):
 esc=lambda s:html.escape(str(s),quote=True)
 products=json.loads((R/'products.json').read_text()); configs=json.loads((R/'product-configurations.json').read_text()); mapping=json.loads((R/'product-map.json').read_text())
 for p in products:
  for lang in ['en','es']:
   es=lang=='es';root='../../../' if es else '../../';path=R/('es' if es else '')/'products'/mapping[str(p['id'])]['slug']/'index.html';t=path.read_text()
   t=re.sub(r'<section id="product-configurator">.*?</section>','',t,flags=re.S)
   t=re.sub(r'<script id="configuration-data" type="application/json">.*?</script>','',t,flags=re.S)
   m=re.search(r'<section id="product-specifications">.*?</section>',t,re.S);spec=m[0];t=t[:m.start()]+t[m.end():]
   catalog_match=re.search(r'<section id="catalog-models">.*?</section>',t,re.S)
   catalog=catalog_match[0] if catalog_match else ''
   if catalog_match:t=t[:catalog_match.start()]+t[catalog_match.end():]
   choices=configs.get(str(p['id']),[])
   options=''.join('<label class="configuration-card"><input type="radio" name="configuration" value="'+str(i)+'"><span>'+esc(c[lang])+'</span></label>' for i,c in enumerate(choices))
   options+='<label class="configuration-card"><input type="radio" name="configuration" value="custom"><span>'+('Otra medida / consulta a Frank' if es else 'Other size / ask Frank')+'</span></label>'
   block='<section id="product-configurator"><h2>'+('Selecciona tu configuración' if es else 'Select your configuration')+'</h2><p class="fine">'+('Selecciona una opción para cotizar. Confirma montaje y compatibilidad con Frank; la foto muestra la serie.' if es else 'Select an option for your quote. Confirm mounting and compatibility with Frank; the photo represents the series.')+'</p><fieldset class="configuration-options"><legend class="visually-hidden">'+('Opciones del producto' if es else 'Product options')+'</legend>'+options+'</fieldset><div class="selected-specifications" aria-live="polite"><p>'+('Elige una opción para ver sus datos.' if es else 'Choose an option to view its details.')+'</p></div><label class="custom-configuration">'+('Tu medida o modelo (opcional)' if es else 'Your size or model (optional)')+'<input id="custom-configuration" type="text" maxlength="180" placeholder="'+('Consulta a Frank' if es else 'Ask Frank')+'"></label><a class="btn configuration-quote" href="https://wa.me/8619883954016" target="_blank" rel="noopener">'+('Cotizar con Frank por WhatsApp ↗' if es else 'Ask Frank for a quote ↗')+'</a></section>'
   t=re.sub(r'(<section class="product-intro">.*?)(</div>\s*</section>)',lambda m:m[1]+block+spec+m[2]+catalog,t,count=1,flags=re.S)
   data=json.dumps(choices,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
   t=t.replace('</body>','<script id="configuration-data" type="application/json">'+data+'</script></body>')
   if 'configuration.css' not in t:t=t.replace('</head>','<link rel="stylesheet" href="'+root+'configuration.css"></head>')
   path.write_text(t)
