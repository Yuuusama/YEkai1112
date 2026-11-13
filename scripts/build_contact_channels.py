"""Maintain the approved contacts on the two homepages only; no hosting calls.

Contact data and translated accessible labels live in contact-channels.json.
Inline monochrome icon paths below need no external files, fonts or requests.
The shared SEO finalizer calls build(), so every normal page-generation entry
point restores these homepage additions. Existing WhatsApp markup is untouched.
"""
from pathlib import Path
import html
import json
import re

ICONS = {
    "email": '<path fill="currentColor" fill-rule="evenodd" d="M4 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h16a3 3 0 0 0 3-3V6a3 3 0 0 0-3-3H4Zm-.1 3.2a1 1 0 0 0-1.2 1.6l8.7 6.5a1 1 0 0 0 1.2 0l8.7-6.5a1 1 0 0 0-1.2-1.6L12 12.25 3.9 6.2Z"/>',
    "facebook": '<path fill="currentColor" d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073C0 18.1 4.388 23.094 10.125 24v-8.437H7.078v-3.49h3.047v-2.66c0-3.025 1.792-4.697 4.533-4.697 1.312 0 2.686.236 2.686.236v2.972h-1.513c-1.49 0-1.956.931-1.956 1.887v2.262h3.328l-.532 3.49h-2.796V24C19.612 23.094 24 18.1 24 12.073Z"/>',
    "messenger": '<path fill="currentColor" fill-rule="evenodd" d="M12 0C5.24 0 0 4.952 0 11.64c0 3.498 1.433 6.52 3.768 8.608.196.175.314.42.322.683l.065 2.135a.96.96 0 0 0 1.348.849l2.382-1.052a.959.959 0 0 1 .64-.047c1.095.301 2.26.465 3.475.465 6.76 0 12-4.952 12-11.64C24 4.952 18.76 0 12 0Zm-7.206 15.044 3.525-5.592a1.8 1.8 0 0 1 2.602-.48l2.803 2.102a.72.72 0 0 0 .867-.003l3.785-2.873c.505-.383 1.164.221.826.758l-3.525 5.592a1.8 1.8 0 0 1-2.602.48l-2.803-2.102a.72.72 0 0 0-.867.003L5.62 15.802c-.505.383-1.164-.221-.826-.758Z"/>',
    "instagram": '<path fill="currentColor" d="M12 0C8.74 0 8.333.014 7.053.072 5.775.13 4.905.333 4.142.63a5.876 5.876 0 0 0-2.126 1.386A5.876 5.876 0 0 0 .63 4.142C.333 4.905.13 5.775.072 7.053.014 8.333 0 8.74 0 12s.014 3.667.072 4.947c.058 1.278.261 2.148.558 2.911a5.876 5.876 0 0 0 1.386 2.126 5.876 5.876 0 0 0 2.126 1.386c.763.297 1.633.5 2.911.558C8.333 23.986 8.74 24 12 24s3.667-.014 4.947-.072c1.278-.058 2.148-.261 2.911-.558a5.876 5.876 0 0 0 2.126-1.386 5.876 5.876 0 0 0 1.386-2.126c.297-.763.5-1.633.558-2.911C23.986 15.667 24 15.26 24 12s-.014-3.667-.072-4.947c-.058-1.278-.261-2.148-.558-2.911a5.876 5.876 0 0 0-1.386-2.126A5.876 5.876 0 0 0 19.858.63c-.763-.297-1.633-.5-2.911-.558C15.667.014 15.26 0 12 0Zm0 2.162c3.204 0 3.584.012 4.849.07 1.17.053 1.805.249 2.227.413a3.715 3.715 0 0 1 1.379.897 3.715 3.715 0 0 1 .897 1.379c.164.422.36 1.057.413 2.227.058 1.265.07 1.645.07 4.849s-.012 3.584-.07 4.849c-.053 1.17-.249 1.805-.413 2.227a3.715 3.715 0 0 1-.897 1.379 3.715 3.715 0 0 1-1.379.897c-.422.164-1.057.36-2.227.413-1.265.058-1.645.07-4.849.07s-3.584-.012-4.849-.07c-1.17-.053-1.805-.249-2.227-.413a3.715 3.715 0 0 1-1.379-.897 3.715 3.715 0 0 1-.897-1.379c-.164-.422-.36-1.057-.413-2.227-.058-1.265-.07-1.645-.07-4.849s.012-3.584.07-4.849c.053-1.17.249-1.805.413-2.227a3.715 3.715 0 0 1 .897-1.379 3.715 3.715 0 0 1 1.379-.897c.422-.164 1.057-.36 2.227-.413 1.265-.058 1.645-.07 4.849-.07Zm0 3.676a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324ZM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm6.406-11.845a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88Z"/>',
}


def channel_block(data, lang, location):
    labels = data["labels"][lang]
    modifier = " contact-channels--footer" if location == "footer" else ""
    links = []
    for channel in ("email", "facebook", "messenger", "instagram"):
        href = "mailto:" + data[channel] if channel == "email" else data[channel]
        label = data[channel] if channel == "email" else channel.capitalize()
        links.append(
            f'<a class="secondary-contact-link secondary-contact-link--{channel}" '
            f'href="{html.escape(href, quote=True)}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="{html.escape(labels[channel], quote=True)}">'
            '<svg class="channel-icon" xmlns="http://www.w3.org/2000/svg" '
            'viewBox="0 0 24 24" width="22" height="22" fill="currentColor" '
            f'aria-hidden="true" focusable="false">{ICONS[channel]}</svg>'
            f'<span>{html.escape(label)}</span></a>'
        )
    return (
        f'<!-- YEKAI {location} channels:start -->'
        f'<div id="{location}-channels" class="contact-channels{modifier}" '
        f'role="group" aria-label="{html.escape(labels["group"], quote=True)}">'
        + "".join(links) + f'</div><!-- YEKAI {location} channels:end -->'
    )


def apply_block(text, data, lang, location):
    block = channel_block(data, lang, location)
    existing = rf'<!-- YEKAI {location} channels:start -->.*?<!-- YEKAI {location} channels:end -->'
    text, count = re.subn(existing, lambda m: block, text, flags=re.S)
    if count:
        if count != 1:
            raise ValueError(f"Duplicate {location} contacts block")
        return text
    if location == "contact":
        section = re.search(r'<section\b(?=[^>]*\bid="contact")[^>]*>.*?</section>', text, re.S)
        if not section:
            raise ValueError("Homepage contact section not found")
        content, count = re.subn(r'<a\b(?=[^>]*\bclass="phone")[^>]*>.*?</a>',
                                lambda m: m[0] + block, section[0], flags=re.S)
        if count != 1:
            raise ValueError("Expected one existing WhatsApp phone link")
        return text[:section.start()] + content + text[section.end():]
    footer = re.search(r'<footer\b[^>]*>.*?</footer>', text, re.S)
    if not footer:
        raise ValueError("Homepage footer not found")
    content, count = re.subn(r'<div\b(?=[^>]*\bclass="footer-bottom")[^>]*>',
                            lambda m: block + m[0], footer[0], count=1)
    if count != 1:
        raise ValueError("Homepage footer-bottom not found")
    return text[:footer.start()] + content + text[footer.end():]


def add_organization_contacts(text, data):
    updated = 0

    def update(node):
        nonlocal updated
        if isinstance(node, list):
            for item in node:
                update(item)
        elif isinstance(node, dict):
            if node.get("@type") == "Organization":
                if not node.get("telephone"):
                    raise ValueError("Existing Organization telephone is required")
                node["email"] = data["email"]
                node["sameAs"] = [data["facebook"], data["instagram"]]
                node["contactPoint"] = {
                    "@type": "ContactPoint", "contactType": "sales",
                    "email": data["email"], "telephone": node["telephone"],
                    "availableLanguage": ["English", "Spanish"],
                }
                updated += 1
            for value in node.values():
                if isinstance(value, (list, dict)):
                    update(value)

    def schema(match):
        node = json.loads(match[2])
        before = updated
        update(node)
        if before == updated:
            return match[0]
        return match[1] + json.dumps(node, ensure_ascii=False, separators=(",", ":")) + match[3]

    text = re.sub(r'(<script\b[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',
                  schema, text, flags=re.S)
    if updated != 1:
        raise ValueError(f"Expected one homepage Organization, got {updated}")
    return text


def build(root):
    root = Path(root)
    data = json.loads((root / "scripts/contact-channels.json").read_text())
    if not (root / "contact-channels.css").is_file():
        raise ValueError("Local contact-channels.css is required")
    for lang, rel, prefix in (("en", "index.html", ""), ("es", "es/index.html", "../")):
        file = root / rel
        original = file.read_text()
        text = apply_block(original, data, lang, "contact")
        text = apply_block(text, data, lang, "footer")
        css = f'<link rel="stylesheet" href="{prefix}contact-channels.css">'
        text, count = re.subn(r'<link\b[^>]*\bhref="(?:\.\./)?contact-channels\.css"[^>]*>',
                              lambda m: css, text)
        if count > 1:
            raise ValueError("Duplicate contact stylesheet")
        if not count:
            text = text.replace("</head>", css + "\n</head>", 1)
        text = add_organization_contacts(text, data)
        if text != original:
            file.write_text(text)


if __name__ == "__main__":
    build(Path(__file__).resolve().parents[1])
