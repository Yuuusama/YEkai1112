"""Repeatable offline polish. Never publishes or contacts hosting."""
import html
import json
import re
from urllib.parse import quote, urlsplit, unquote
from PIL import Image

def build(root):
    products = json.loads((root/'products.json').read_text())
    mapping = json.loads((root/'product-map.json').read_text())
    for p in products:
        for lang in ('en','es'):
            base = root/'es' if lang=='es' else root
            file = base/'products'/mapping[str(p['id'])]['slug']/'index.html'
            text = file.read_text()
            # The curated buyer-links block supersedes the older duplicate block.
            text = re.sub(r'<section id="related-products">.*?</section>', '', text, flags=re.S)
            message = ('Hola Frank, quisiera cotizar: ' if lang=='es' else 'Hello Frank, please quote: ') + p[lang]
            url = 'https://wa.me/8619883954016?text=' + quote(message, safe='')
            text = re.sub(r'(<a\b[^>]*id="sticky-quote"[^>]*href=")[^"]*', lambda m:m[1]+url, text)
            file.write_text(text)
    for file in root.rglob('*.html'):
        text = file.read_text()
        def image(match):
            tag = match[0]
            src = re.search(r'\bsrc="([^"]+)"',tag)
            if not src or urlsplit(src[1]).scheme: return tag
            path = (root/src[1].lstrip('/') if src[1].startswith('/') else file.parent/unquote(src[1])).resolve()
            if not path.is_file(): return tag
            try:
                with Image.open(path) as im: width,height=im.size
            except (OSError,ValueError): return tag
            for key,val in [('width',width),('height',height)]:
                if not re.search(r'\b'+key+r'=',tag): tag=tag[:-1]+f' {key}="{val}">'
            return tag
        file.write_text(re.sub(r'<img\b[^>]*>',image,text))

    from maintain_seo import build as maintain_seo
    maintain_seo(root)
