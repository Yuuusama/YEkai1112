"""Read-only contact audit. Optional --baseline compares the preceding site tree.

Usage: python scripts/validate_contact_channels.py [--baseline /path/to/old/site]
Static checks cannot verify rendered layout, network traffic or live accounts.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import json
import re
import sys
from maintain_seo import Tags


class Contacts(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.stack = []
        self.links = []
        self.current = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a":
            self.current = {"attrs": a, "parents": list(self.stack), "text": "", "icons": [], "paths": []}
            self.links.append(self.current)
        elif self.current and tag in ("svg", "path"):
            self.current["icons" if tag == "svg" else "paths"].append(a)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append((tag, a))

    def handle_endtag(self, tag):
        if tag == "a":
            self.current = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        if self.current:
            self.current["text"] += data


def walk(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from walk(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk(value)


def external_assets(root):
    found = Counter()
    for file in root.rglob("*"):
        if not file.is_file() or file.suffix not in {".html", ".css"}:
            continue
        text = file.read_text()
        refs = []
        if file.suffix == ".html":
            for tag, a in Tags(text).tags:
                if tag in {"script", "img", "source", "iframe", "video", "audio", "embed"}:
                    refs.extend(a[k] for k in ("src", "poster") if a.get(k))
                    refs.extend(x.strip().split()[0] for x in a.get("srcset", "").split(",") if x.strip())
                if tag == "link" and any(x in a.get("rel", "").split() for x in ("stylesheet", "preload", "modulepreload", "prefetch", "preconnect", "dns-prefetch", "icon")):
                    if a.get("href"):
                        refs.append(a["href"])
                if tag in {"image", "use"}:
                    refs.extend(a[k] for k in ("href", "xlink:href") if a.get(k))
        refs.extend(re.findall(r'url\(\s*[\"\']?([^\)\"\']+)', text))
        refs.extend(re.findall(r'@import\s+[\"\']([^\"\']+)', text))
        for ref in refs:
            parsed = urlsplit(ref)
            if parsed.netloc and parsed.netloc != "yekaifrank.com":
                found[(file.relative_to(root).as_posix(), ref)] += 1
    return found


def remove_new_home_content(text):
    text = re.sub(r'<!-- YEKAI (contact|footer) channels:start -->.*?<!-- YEKAI \1 channels:end -->', '', text, flags=re.S)
    text = re.sub(r'<link\b[^>]*\bhref="(?:\.\./)?contact-channels\.css"[^>]*>\n?', '', text)

    def schema(m):
        node = json.loads(m[2])
        changed = False
        for item in walk(node):
            if item.get("@type") == "Organization":
                for key in ("email", "sameAs", "contactPoint"):
                    item.pop(key, None)
                changed = True
        return m[1] + json.dumps(node, ensure_ascii=False, separators=(",", ":")) + m[3] if changed else m[0]

    return re.sub(r'(<script\b[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)', schema, text, flags=re.S)


def audit(root, baseline=None):
    data = json.loads((root / "scripts/contact-channels.json").read_text())
    targets = {k: ("mailto:" + data[k] if k == "email" else data[k]) for k in ("email", "facebook", "messenger", "instagram")}
    homes = {"index.html": "en", "es/index.html": "es"}
    errors, rows, found_pages = [], [], []
    json_count = icon_count = 0
    for file in sorted(root.rglob("*.html")):
        rel, text = file.relative_to(root).as_posix(), file.read_text()
        parser = Contacts(text)
        contacts = [a for a in parser.links if a["attrs"].get("href") in targets.values()]
        if contacts:
            found_pages.append(rel)
        if rel not in homes:
            if any(data[k] in text for k in targets):
                errors.append(rel + ": contact data outside homepages")
        else:
            lang = homes[rel]
            row = {"page": "/es/" if lang == "es" else "/", "visible_links": {}, "literal_occurrences_in_html": {}, "json_ld": {}}
            for channel, href in targets.items():
                links = [a for a in contacts if a["attrs"].get("href") == href]
                row["visible_links"][channel] = len(links)
                row["literal_occurrences_in_html"][channel] = text.count(data[channel])
                locations = Counter("contact" if any(t == "section" and a.get("id") == "contact" for t, a in link["parents"]) else "footer" if any(t == "footer" for t, a in link["parents"]) else "other" for link in links)
                if locations != Counter({"contact": 1, "footer": 1}):
                    errors.append(f"{rel}: {channel} locations {dict(locations)}")
                for link in links:
                    a = link["attrs"]
                    if a.get("target") != "_blank" or set(a.get("rel", "").split()) != {"noopener", "noreferrer"} or a.get("aria-label") != data["labels"][lang][channel]:
                        errors.append(f"{rel}: unsafe/inaccessible {channel} link")
                    label = data[channel] if channel == "email" else channel.capitalize()
                    if link["text"] != label:
                        errors.append(f"{rel}: wrong visible {channel} label")
                    if len(link["icons"]) != 1 or not link["paths"]:
                        errors.append(f"{rel}: missing inline {channel} icon")
                    for svg in link["icons"]:
                        icon_count += 1
                        if any(svg.get(k) != v for k, v in {"viewbox": "0 0 24 24", "width": "22", "height": "22", "fill": "currentColor", "aria-hidden": "true", "focusable": "false"}.items()):
                            errors.append(f"{rel}: invalid {channel} SVG attributes")
                    if any(p.get("fill") != "currentColor" or not p.get("d") for p in link["paths"]):
                        errors.append(f"{rel}: invalid {channel} SVG path")
            rows.append(row)
        for match in re.finditer(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', text, re.S):
            try:
                node = json.loads(match[1])
                json_count += 1
            except ValueError as e:
                errors.append(f"{rel}: invalid JSON-LD {e}")
                continue
            if rel in homes:
                for org in walk(node):
                    if org.get("@type") != "Organization":
                        continue
                    expected_point = {"@type": "ContactPoint", "contactType": "sales", "email": data["email"], "telephone": org.get("telephone"), "availableLanguage": ["English", "Spanish"]}
                    if org.get("email") != data["email"] or org.get("sameAs") != [data["facebook"], data["instagram"]] or org.get("contactPoint") != expected_point or not org.get("telephone") or "logo" in org:
                        errors.append(rel + ": wrong Organization contacts")
                    row["json_ld"] = {"organization_email": 1, "sales_email": 1, "facebook_sameAs": 1, "instagram_sameAs": 1, "messenger_sameAs": 0, "telephone": org["telephone"]}
        if rel in homes and not row["json_ld"]:
            errors.append(rel + ": missing Organization contacts")
    if set(found_pages) != set(homes):
        errors.append("Contact page set mismatch")
    # Keep the obsolete account identifier itself out of the website package.
    obsolete = ("6159439" + "2821285").encode()
    old_hits = [f.relative_to(root).as_posix() for f in root.rglob("*") if f.is_file() and f.suffix != ".pyc" and obsolete in f.read_bytes()]
    if old_hits:
        errors.append("Obsolete Facebook identifier found")
    css = (root / "contact-channels.css").read_text()
    sized = all(re.search(rf"{key}\s*:\s*{value}", css) for key, value in (("min-width", "44px"), ("min-height", "44px"), ("width", "22px"), ("height", "22px")))
    if not sized:
        errors.append("CSS target/icon sizing missing")
    assets = external_assets(root)
    added_assets = None
    scope = "not compared"
    if baseline:
        added_assets = assets - external_assets(baseline)
        if added_assets:
            errors.append("New external asset references found")
        for f in baseline.rglob("*"):
            if not f.is_file() or "__pycache__" in f.parts:
                continue
            rel = f.relative_to(baseline).as_posix()
            new = root / rel
            if rel in homes:
                if remove_new_home_content(new.read_text()) != remove_new_home_content(f.read_text()):
                    errors.append(rel + ": changes outside approved contact additions")
            elif rel not in {"scripts/maintain_seo.py", "scripts/check_regeneration.py", "REVIEW-NOTES.txt"} and (not new.exists() or new.read_bytes() != f.read_bytes()):
                errors.append(rel + ": unrelated file changed")
        scope = "homepage additions and generator/audit notes only; all other existing files byte-identical"
    return {"homepage_contacts": rows, "html_pages_with_contacts": found_pages, "inline_icons": icon_count,
            "json_ld_blocks_parsed": json_count, "obsolete_facebook_id_files": old_hits,
            "dist": "included in recursive scan" if (root / "dist").exists() else "not present; Netlify publishes the site root",
            "external_asset_references": [{"page_or_css": k[0], "url": k[1], "count": v} for k, v in assets.items()],
            "new_external_asset_references": None if added_assets is None else sum(added_assets.values()),
            "baseline_scope_check": scope if not errors else "see errors", "css_declares_44px_targets_and_22px_icons": sized,
            "errors": errors, "unverified": ["浏览器渲染", "手机显示及实际触控区域", "图标实际渲染样子", "运行时网络请求", "外链账号可达性", "线上部署"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()
    result = audit(Path(__file__).resolve().parents[1], args.baseline)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result["errors"]))
