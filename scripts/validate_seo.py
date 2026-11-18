"""Read-only static validation. Usage: python scripts/validate_seo.py"""
from pathlib import Path
from urllib.parse import urljoin,urlsplit,unquote
import sys,json,re,html,xml.etree.ElementTree as ET
from collections import Counter
from maintain_seo import Tags,meta,canonical,BASE,REDIRECTS
R=Path(__file__).resolve().parents[1]
def resolve(url):
 p=R/unquote(urlsplit(url).path).lstrip('/')
 if p.is_dir():p=p/'index.html'
 return p
pages={f: f.read_text() for f in R.rglob('*.html')}
issues=[]; rows=[];badlinks=[];anchorissues=[];jsoncount=0;references=0
for f,t in pages.items():
 rel=f.relative_to(R).as_posix();url=BASE+'/'+rel.removesuffix('index.html');tags=Tags(t).tags
 for m in re.finditer(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
  jsoncount+=1
  try:json.loads(m[1])
  except Exception as e:issues.append(f'{rel}: invalid JSON-LD: {e}')
 if canonical(t) and 'noindex' not in meta(t,'robots').lower():
  ids=Counter(a['id'] for k,a in tags if a.get('id'))
  if any(v>1 for v in ids.values()):issues.append(f'{rel}: duplicate element IDs')
  for element in ('title','h1','main'):
   if sum(k==element for k,a in tags)!=1:issues.append(f'{rel}: expected one {element}')
  navs=[a for k,a in tags if k=='nav' and 'category-navigation' in a.get('class','').split() and a.get('id')!='brush-family-links']
  if len(navs)!=1:issues.append(f'{rel}: expected one main category nav, got {len(navs)}')
  for kind,key in [('name','description'),('property','og:title'),('property','og:description')]:
   found=[a for k,a in tags if k=='meta' and a.get(kind)==key]
   if len(found)!=1:issues.append(f'{rel}: expected one {key} tag')
  c=canonical(t);title=html.unescape(re.search(r'<title>(.*?)</title>',t,re.S)[1]);desc=meta(t,'description');alts={a.get('hreflang'):a.get('href') for k,a in tags if k=='link' and a.get('hreflang')}
  if meta(t,'og:title','property')!=title:issues.append(f'{rel}: title and og:title differ')
  if meta(t,'og:description','property')!=desc:issues.append(f'{rel}: meta and og:description differ')
  okc=c==url;okh=True
  en=url.replace(BASE+'/es/',BASE+'/');es=en.replace(BASE+'/',BASE+'/es/',1)
  if '/es/guias/' in url or '/guides/' in url:okh=(set(alts)=={'en','es','x-default'} or set(alts)=={'en','x-default'}) and alts.get('es' if '/es/' in url else 'en')==url
  elif alts!={'en':en,'es':es,'x-default':en}:okh=False
  for lang,target in alts.items():
   dest=resolve(target)
   if not dest.exists():okh=False;continue
   other={a.get('hreflang'):a.get('href') for k,a in Tags(dest.read_text()).tags if k=='link' and a.get('hreflang')}
   if other!=alts:okh=False
  limit=160 if rel.startswith('es/') else 155
  if not okc or not okh or len(desc)>limit:issues.append(f'{rel}: canonical={okc}, hreflang={okh}, description={len(desc)}/{limit}')
  rows.append({'url':url,'title':title,'title_length':len(title),'description_length':len(desc),'canonical':c,'canonical_ok':okc,'hreflang_ok':okh,'title_over_60':len(title)>60})
  if '/products/' in url:
   for section in ('product-configurator','product-specifications','product-buying-question','buying-notes','buyer-links','product-inquiry','configuration-data'):
    if ids[section]!=1:issues.append(f'{rel}: missing/repeated {section}')
   vals=[meta(t,'og:description','property')]
   for m in re.finditer(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
    data=json.loads(m[1]);vals.extend(n.get('description') for n in data.get('@graph',[data]) if n.get('@type') in ['Product','WebPage'])
   if len(vals)!=3 or any(v!=desc for v in vals):issues.append(rel+': inconsistent descriptions')
 for tag,a in tags:
  refs=[]
  if a.get('href') and tag in ['a','link']:refs.append(a['href'])
  for key in ['src','poster']:
   if a.get(key):refs.append(a[key])
  if a.get('srcset'):refs += [v.strip().split()[0] for v in a['srcset'].split(',') if v.strip()]
  for ref in refs:
   u=urlsplit(urljoin(url,ref))
   if u.netloc!='yekaifrank.com' or u.scheme not in ['http','https']:continue
   references+=1;dest=resolve(u.geturl())
   if not dest.exists():badlinks.append([rel,ref])
   if u.path.removesuffix('index.html') in REDIRECTS:issues.append(f'{rel}: old redirect link {ref}')
   if u.fragment and dest.suffix=='.html' and dest.exists():
    ids={a.get('id') for k,a in Tags(dest.read_text()).tags}|{a.get('name') for k,a in Tags(dest.read_text()).tags if k=='a'}
    if unquote(u.fragment) not in ids:anchorissues.append([rel,ref])
for f in R.rglob('*.css'):
 for ref in re.findall(r'url\(\s*[\"\']?([^\)\"\']+)',f.read_text()):
  u=urlsplit(urljoin(BASE+'/'+f.relative_to(R).as_posix(),ref))
  if u.netloc=='yekaifrank.com' and u.scheme in ['http','https']:
   references+=1
   if not resolve(u.geturl()).exists():badlinks.append([str(f.relative_to(R)),ref])
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'};tree=ET.parse(R/'sitemap.xml');nodes=tree.findall('s:url',ns);urls=[]
for node in nodes:
 url=node.findtext('s:loc',namespaces=ns);urls.append(url);p=resolve(url)
 if not p.exists() or 'noindex' in meta(p.read_text(),'robots') or canonical(p.read_text())!=url:issues.append('Invalid sitemap URL '+url)
 if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',node.findtext('s:lastmod',namespaces=ns) or ''):issues.append('Wrong lastmod '+url)
if len(urls)<44 or set(urls)!={x['url'] for x in rows}:issues.append('Sitemap URL set mismatch')
for old in REDIRECTS:
 if (R/old.strip('/')/'index.html').exists():issues.append('Redirect shadow file '+old)
result={'indexable_pages':len(rows),'sitemap_urls':len(urls),'json_ld_blocks_parsed':jsoncount,'local_html_css_references':references,'errors':issues,'missing_files':badlinks,'missing_fragments':anchorissues,'pages':rows,'unverified':['浏览器渲染及交互','JavaScript运行时动态URL/请求','外部链接可达性','线上Netlify重定向及HTTP响应','Google实际收录及富媒体资格']}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(bool(issues or badlinks or anchorissues))
