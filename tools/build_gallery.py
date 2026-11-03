"""Build index.html: an offline brand gallery (logos, colours, type, components) for wazn-brand."""
import json, re, html
from pathlib import Path
R = Path(__file__).resolve().parents[1]
t = json.loads((R/"design-system/tokens.json").read_text())
comps = R/"design-system/components"
def strip_marker(s): return re.sub(r"^<!--.*?-->\n", "", s, count=1)
sw = "".join(
    f'<div class="sw"><div class="chip" style="background:var(--{c["name"]})"></div>'
    f'<b>{c["name"]}</b><code>{c["value"]["light"]} · {c["value"]["dark"]}</code><span>{html.escape(c["usage"])}</span></div>'
    for c in t["color"]["tokens"])
ty = "".join(
    f'<div class="ty"><code>{s["name"]} · {s["fontSize"]}/{s["lineHeight"]} · {s["fontWeight"]}</code>'
    f'<div style="font-family:var(--font-{g["family"]});font-size:{s["fontSize"]};line-height:{s["lineHeight"]};font-weight:{s["fontWeight"]}">{html.escape(s.get("sample",""))}</div></div>'
    for g in t["type"]["groups"] for s in g["styles"])
logos = sorted((R/"logos/svg").glob("*.svg"))
lg = "".join(
    f'<figure class="{"dark" if ("reverse" in p.name or "ivory" in p.name) else ""}"><img src="logos/svg/{p.name}" alt="{p.stem}"><figcaption>{p.name}</figcaption></figure>'
    for p in logos)
cp = "".join(
    f'<section class="comp"><h3>{d.name}</h3>{strip_marker((d/"preview.html").read_text())}</section>'
    for d in sorted(comps.iterdir()) if d.is_dir() and d.name != "Cover")
cover = strip_marker((comps/"Cover/preview.html").read_text())
page = f"""<!doctype html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wazn — Brand</title><link rel="icon" href="logos/svg/wazn-favicon.svg">
<link rel="stylesheet" href="design-system/tokens.css"><link rel="stylesheet" href="design-system/components/bundle.css">
<style>
body{{margin:0;background:var(--surface-0);color:var(--ink);font:16px/1.75 var(--font-sans)}}
main{{max-width:1040px;margin:0 auto;padding:var(--space-12) var(--space-6)}}
h2{{font:600 28px/36px var(--font-display);margin:var(--space-12) 0 var(--space-4);border-top:1px solid var(--line);padding-top:var(--space-8)}}
h3{{font:600 15px/24px var(--font-sans);color:var(--ink-muted);margin:0 0 var(--space-2)}}
.bar{{display:flex;justify-content:space-between;align-items:center}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:var(--space-4)}}
figure{{margin:0;background:#F6F3EC;border:1px solid var(--line);border-radius:var(--radius-md);padding:var(--space-6);display:grid;gap:var(--space-3);place-items:center}}
figure.dark{{background:#0E1B2C}} figure img{{max-width:100%;max-height:120px}}
figcaption{{font:12px/16px var(--font-mono);color:#8F8676}}
.sw{{display:grid;grid-template-columns:56px 1fr;column-gap:var(--space-3);font-size:13px;line-height:20px;margin-bottom:var(--space-3)}}
.chip{{grid-row:span 3;width:56px;height:56px;border-radius:var(--radius-md);border:1px solid var(--line)}}
.sw code,.ty code{{font:12px var(--font-mono);color:var(--ink-muted)}} .sw span{{color:var(--ink-muted)}}
.ty{{padding:var(--space-3) 0;border-bottom:1px solid var(--line)}}
.comp{{background:var(--surface-1);border:1px solid var(--line);border-radius:var(--radius-md);padding:var(--space-4);margin-bottom:var(--space-4);overflow:auto}}
.cover{{overflow:auto;border:1px solid var(--line);border-radius:var(--radius-md)}}
</style></head><body><main>
<div class="bar"><img src="logos/svg/wazn-logo-en.svg" height="40" alt="Wazn">
<button class="wz-btn wz-btn--secondary wz-btn--sm" onclick="const h=document.documentElement;h.dataset.theme=h.dataset.theme==='light'?'dark':'light'">Ivory / Night</button></div>
<h2>Cover</h2><div class="cover">{cover}</div>
<h2>Logos</h2><div class="grid">{lg}</div>
<h2>Colour</h2><div class="grid">{sw}</div>
<h2>Type</h2>{ty}
<h2>Components</h2>{cp}
<p style="color:var(--ink-muted);font-size:13px">Rules and rationale: BRAND_BOOK.md · Tokens: design-system/tokens.json</p>
</main></body></html>"""
(R/"index.html").write_text(page, encoding="utf-8")
print("index.html written")
