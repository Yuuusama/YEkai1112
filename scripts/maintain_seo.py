"""Scoped 2026-11-10 metadata/redirect maintenance; no product-data or inquiry edits."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
import html,json,re,xml.etree.ElementTree as ET
BASE='https://yekaifrank.com'
REDIRECTS={'/abrasive-flap-wheel/':'/abrasive-flap-disc/','/es/abrasive-flap-wheel/':'/es/abrasive-flap-disc/','/products/thin-crimped-wire-wheels/':'/products/red-knotted-wire-cup-brush/','/es/products/thin-crimped-wire-wheels/':'/es/products/red-knotted-wire-cup-brush/'}
class Tags(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True); self.tags=[];self.feed(text)
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
def attrs(tag):return Tags(tag).tags[0][1]
def meta(text,key,kind='name'):
 return next((a.get('content','') for t,a in Tags(text).tags if t=='meta' and a.get(kind)==key),'')
def canonical(text):return next((a.get('href','') for t,a in Tags(text).tags if t=='link' and a.get('rel')=='canonical'),'')
def set_attr(tag,key,value):
 pattern=r'(\b'+re.escape(key)+r'\s*=\s*)([\"\']).*?\2'
 return re.sub(pattern,lambda m:m[1]+m[2]+html.escape(value,quote=True)+m[2],tag,count=1,flags=re.S)
def set_meta(text,key,value,kind='name'):
 found=False
 def replace(m):
  nonlocal found
  if attrs(m[0]).get(kind)!=key:return m[0]
  found=True;return set_attr(m[0],'content',value)
 text=re.sub(r'<meta\b[^>]*>',replace,text,flags=re.I)
 if not found:text=text.replace('</head>',f'<meta {kind}="{key}" content="{html.escape(value,quote=True)}"/>\n</head>',1)
 return text
def write_sitemap(root):
 urls=[]
 for f in sorted(root.rglob('index.html')):
  text=f.read_text()
  if 'noindex' in meta(text,'robots').lower():continue
  url=canonical(text)
  if url:urls.append(url)
 assert len(urls)>=44 and len(set(urls))==len(urls), f'Expected at least 44 unique canonical URLs, got {len(urls)}'
 ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns)
 tree=ET.Element('{'+ns+'}urlset')
 for url in urls:
  node=ET.SubElement(tree,'{'+ns+'}url');ET.SubElement(node,'{'+ns+'}loc').text=url;ET.SubElement(node,'{'+ns+'}lastmod').text='2026-11-13'
 ET.indent(tree);ET.ElementTree(tree).write(root/'sitemap.xml',encoding='utf-8',xml_declaration=True)
def build(root):
 root=Path(root);overrides=json.loads((root/'scripts/seo-copy.json').read_text())['metadataOverrides20261110']
 for old in REDIRECTS:
  f=root/old.strip('/')/'index.html'
  if f.exists():f.unlink()
  if f.parent.exists() and not any(f.parent.iterdir()):f.parent.rmdir()
 for f in root.rglob('*.html'):
  text=f.read_text();original=text
  # Preserve the unrelated noindex legacy shells byte-for-byte.
  if 'noindex' in meta(text,'robots').lower():continue
  path='/'+f.relative_to(root).as_posix();page=path.removesuffix('index.html')
  def link(m):
   a=attrs(m[0]);href=a.get('href')
   if not href:return m[0]
   resolved=urlsplit(urljoin(BASE+page,href))
   if resolved.netloc!='yekaifrank.com':return m[0]
   old=resolved.path.removesuffix('index.html')
   if old not in REDIRECTS:return m[0]
   target=REDIRECTS[old]+(('?'+resolved.query) if resolved.query else '')+(('#'+resolved.fragment) if resolved.fragment else '')
   return set_attr(m[0],'href',target)
  text=re.sub(r'<(?:a|link)\b[^>]*>',link,text,flags=re.I)
  change=overrides.get(page,{})
  if 'title' in change:
   text=re.sub(r'<title>.*?</title>',lambda m:'<title>'+html.escape(change['title'])+'</title>',text,flags=re.S)
   text=set_meta(text,'og:title',change['title'],'property')
  if 'description' in change:
   text=set_meta(text,'description',change['description']);text=set_meta(text,'og:description',change['description'],'property')
  if change:
   def schema(m):
    data=json.loads(m[2])
    def walk(node):
     if isinstance(node,list):
      for item in node:walk(item)
     elif isinstance(node,dict):
      if node.get('@type') in ('WebPage','Product') and 'description' in change:node['description']=change['description']
      if node.get('@type')=='WebPage' and 'title' in change:node['name']=change['title']
      for item in node.values():
       if isinstance(item,(dict,list)):walk(item)
    walk(data)
    return m[1]+json.dumps(data,ensure_ascii=False,separators=(',',':'))+m[3]
   text=re.sub(r'(<script\b[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,text,flags=re.S)
  if page in ('/','/es/'):
   title=html.unescape(re.search(r'<title>(.*?)</title>',text,re.S)[1])
   for key,value in [('og:title',title),('og:description',meta(text,'description')),('og:url',BASE+page),('og:image',BASE+'/images/hero-studio.webp'),('og:type','website')]:text=set_meta(text,key,value,'property')
   text=set_meta(text,'twitter:card','summary_large_image')
  if text!=original:f.write_text(text)
 write_sitemap(root)
 from build_contact_channels import build as build_contacts
 build_contacts(root)
 from refine_site_20261113 import build as refine_site
 refine_site(root)
if __name__=='__main__':build(Path(__file__).resolve().parents[1])
