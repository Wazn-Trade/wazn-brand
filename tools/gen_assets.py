"""Generate every Wazn logo asset as outlined SVG (no font dependency)."""
from pathlib import Path
from textpath import text_path

OUT = Path(__file__).resolve().parents[1] / "logos" / "svg"
READEX = str(Path(__file__).resolve().parent / "src-fonts/ReadexPro.ttf")
PLEX = str(Path(__file__).resolve().parent / "src-fonts/IBMPlexSansArabic-Medium.ttf")

INK, NAVY, BRASS, IVORY, BRASS_DARK = "#0A0A0A", "#2E2B26", "#B08A50", "#FBFAF7", "#C4A070"

# ---- the mark: weights of different sizes, balanced on one fulcrum -------------------
# Grid 56 x 40 (units). Beam y=22..26, bars stand on the beam, fulcrum below.
# Moments about x=28 balance: left 12*(-20.5) + 22*(-8.5) ~= right 21*(+20.5)
MARK_W, MARK_H = 56, 40
def mark(bars, beam, x=0, y=0, s=1.0):
    def r(rx, ry, w, h, fill):
        return (f'<rect x="{x+rx*s:.2f}" y="{y+ry*s:.2f}" width="{w*s:.2f}" '
                f'height="{h*s:.2f}" fill="{fill}"/>')
    parts = [
        r(3, 10, 9, 12, bars),   # weight A (short)
        r(15, 0, 9, 22, bars),   # weight B (tall)
        r(44, 1, 9, 21, bars),   # weight C (far right)
        r(0, 22, 56, 4, beam),   # beam
        f'<path d="M{x+28*s:.2f} {y+26*s:.2f} L{x+19*s:.2f} {y+40*s:.2f} '
        f'L{x+37*s:.2f} {y+40*s:.2f} Z" fill="{beam}"/>',  # fulcrum
    ]
    return "".join(parts)

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
            f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')

def word(text, size, wght=600, font=READEX, tracking=0.0):
    d, adv, (x0, y0, x1, y1) = text_path(font, text, size, wght=wght, tracking=tracking)
    return d, (x0, y0, x1, y1)

def placed(d, bounds, x, y, fill):
    x0, y0, _, _ = bounds
    return f'<path transform="translate({x - x0:.2f} {y - y0:.2f})" d="{d}" fill="{fill}"/>'

def size_of(b):
    return b[2] - b[0], b[3] - b[1]

assets = {}

# 1. Marks
for name, bars, beam, bg in [
    ("wazn-mark", INK, BRASS, None),
    ("wazn-mark-reverse", IVORY, BRASS_DARK, None),
    ("wazn-mark-mono-ink", INK, INK, None),
    ("wazn-mark-mono-ivory", IVORY, IVORY, None),
]:
    pad = 4
    assets[f"Logos/{name}.svg"] = svg(MARK_W + 2*pad, MARK_H + 2*pad,
                                      mark(bars, beam, pad, pad), "Wazn mark")

# 2. Lockups. Cap-height of the Latin word = 0.7 * size; mark height ~ 1.25 cap.
def lockup(lang, bars, beam, text_fill, name):
    if lang == "en":
        d, b = word("Wazn", 100)
    else:
        d, b = word("وزن", 120)
    ww, wh = size_of(b)
    mh = 74.0 if lang == "en" else wh * 0.82
    s = mh / MARK_H
    mw = MARK_W * s
    gap = mh * 0.42
    pad = 12
    H = max(mh, wh) + 2 * pad
    if lang == "en":   # LTR: mark then word; word baseline aligned to beam-bottom-ish
        mx, my = pad, pad + (H - 2*pad - mh) / 2
        body = mark(bars, beam, mx, my, s)
        body += placed(d, b, mx + mw + gap, pad + (H - 2*pad - wh) / 2, text_fill)
        W = pad + mw + gap + ww + pad
    else:              # RTL: word then mark on the right (reading starts with the mark)
        body = placed(d, b, pad, pad + (H - 2*pad - wh) / 2, text_fill)
        mx = pad + ww + gap
        body += mark(bars, beam, mx, pad + (H - 2*pad - mh) / 2, s)
        W = mx + mw + pad
    assets[f"Logos/{name}.svg"] = svg(W, H, body, "Wazn وزن")

lockup("en", INK, BRASS, INK, "wazn-logo-en")
lockup("en", IVORY, BRASS_DARK, IVORY, "wazn-logo-en-reverse")
lockup("ar", INK, BRASS, INK, "wazn-logo-ar")
lockup("ar", IVORY, BRASS_DARK, IVORY, "wazn-logo-ar-reverse")

# 3. Bilingual stacked: mark / وزن / WAZN
def stacked(bars, beam, fill, sub, name):
    da, ba = word("وزن", 96)
    de, be = word("WAZN", 30, wght=500, tracking=0.32)
    aw, ah = size_of(ba); ew, eh = size_of(be)
    s = 2.0; mw, mh = MARK_W * s, MARK_H * s
    pad = 16
    W = max(mw, aw, ew) + 2 * pad
    y = pad
    body = mark(bars, beam, (W - mw) / 2, y, s); y += mh + 22
    body += placed(da, ba, (W - aw) / 2, y, fill); y += ah + 18
    body += placed(de, be, (W - ew) / 2, y, sub); y += eh + pad
    assets[f"Logos/{name}.svg"] = svg(W, y, body, "Wazn وزن")

stacked(INK, BRASS, INK, BRASS, "wazn-logo-stacked")
stacked(IVORY, BRASS_DARK, IVORY, BRASS_DARK, "wazn-logo-stacked-reverse")

# 4. App icon (1024 grid, ink tile, radius 22.5%)
S = 1024
s = 600 / MARK_W
body = f'<rect width="{S}" height="{S}" rx="{S*0.225:.0f}" fill="{INK}"/>'
body += mark(IVORY, BRASS_DARK, (S - MARK_W*s)/2, (S - MARK_H*s)/2 + 10, s)
assets["Logos/wazn-app-icon.svg"] = svg(S, S, body, "Wazn app icon")

# Favicon: simplified (no fulcrum detail lost at 16px: same mark, tighter padding)
s16 = 26 / MARK_W
fav = f'<rect width="32" height="32" rx="6" fill="{INK}"/>' + mark(IVORY, BRASS_DARK, 3, 16 - MARK_H*s16/2, s16)
assets["Logos/wazn-favicon.svg"] = svg(32, 32, fav, "Wazn")

# 5. Product family lockups: mark + "Wazn" (600) + product (300, brass) on ONE baseline,
#    Arabic product name under it, right-aligned.
PRODUCTS = [("Screen", "الفلترة"), ("Purify", "التطهير"), ("Engine", "المحرك"), ("Agent", "الوكيل")]
for en, ar in PRODUCTS:
    size = 64; cap = 0.70 * size
    pad = 10; gap = 18
    s = (cap * 1.25) / MARK_H; mw, mh = MARK_W * s, MARK_H * s
    base = pad + size * 0.80          # baseline of the Latin line
    x = pad + mw + gap
    d1, a1, _ = text_path(READEX, "Wazn", size, x=x, baseline=base, wght=600)
    d2, a2, b2 = text_path(READEX, en, size, x=x + a1 + size * 0.22, baseline=base, wght=300)
    right = x + a1 + size * 0.22 + a2
    # mark sits on the baseline: its fulcrum bottom = baseline
    body = mark(INK, BRASS, pad, base - mh, s)
    body += f'<path d="{d1}" fill="{INK}"/><path d="{d2}" fill="{BRASS}"/>'
    sub = 28
    _, a3, _ = text_path(PLEX, f"وزن {ar}", sub)
    base2 = max(base + size * 0.22, b2[3]) + sub * 1.15
    d3, _, b3 = text_path(PLEX, f"وزن {ar}", sub, x=right - a3, baseline=base2)
    body += f'<path d="{d3}" fill="#6E6B64"/>'
    H = b3[3] + pad
    assets[f"Products/wazn-{en.lower()}.svg"] = svg(right + pad, H, body, f"Wazn {en}")

for rel, text in assets.items():
    p = OUT / Path(rel).name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print(f"{rel:40} {len(text):>7} bytes")
