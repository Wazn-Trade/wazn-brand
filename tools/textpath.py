"""Shape text with HarfBuzz and outline it with fontTools -> SVG path data (y-down)."""
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

_cache = {}

def _load(path):
    if path not in _cache:
        blob = hb.Blob.from_file_path(path)
        _cache[path] = (TTFont(path), hb.Face(blob))
    return _cache[path]

def text_path(path, text, size, x=0.0, baseline=0.0, wght=None, tracking=0.0, rtl=None):
    tt, face = _load(path)
    font = hb.Font(face)
    loc = {}
    if wght is not None and "fvar" in tt:
        loc = {"wght": wght}
        font.set_variations(loc)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    upem = tt["head"].unitsPerEm
    s = size / upem
    gs = tt.getGlyphSet(location=loc) if loc else tt.getGlyphSet()
    order = tt.getGlyphOrder()
    pen = SVGPathPen(gs, lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    bp = BoundsPen(gs)
    cx = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        ox = x + (cx + pos.x_offset) * s
        oy = baseline - pos.y_offset * s
        tp = TransformPen(pen, (s, 0, 0, -s, ox, oy))
        gs[name].draw(tp)
        gs[name].draw(TransformPen(bp, (s, 0, 0, -s, ox, oy)))
        cx += pos.x_advance + tracking * upem
    width = (cx - tracking * upem) * s
    return pen.getCommands(), width, bp.bounds

def metrics(path, size):
    tt, _ = _load(path)
    s = size / tt["head"].unitsPerEm
    os2 = tt["OS/2"]
    return {"cap": getattr(os2, "sCapHeight", 0) * s, "x": getattr(os2, "sxHeight", 0) * s,
            "asc": os2.sTypoAscender * s, "desc": -os2.sTypoDescender * s}
