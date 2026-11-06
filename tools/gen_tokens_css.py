"""Generate ``design-system/tokens.css`` from ``design-system/tokens.json``.

This is a safety net, not a build step. Both files stay committed; the generator
exists so drift between them is visible and fixable.

    uv run python tools/gen_tokens_css.py                    # print to stdout
    uv run python tools/gen_tokens_css.py --write            # overwrite tokens.css
    uv run python tools/gen_tokens_css.py --check            # exit 1 on drift

Token JSON ↔ CSS mapping (compact, single-line selectors to match the hand-authored style):

- ``color.tokens[].value.{light,dark}`` → ``:root,[data-theme="light"]{...}`` and
  ``[data-theme="dark"]{...}`` blocks. ``{token-name}`` references resolve to
  ``var(--token-name)``.
- ``spacing.tokens[] + radius.tokens[] + type.families + motion.tokens[]`` →
  one ``:root{...}`` block of theme-independent custom properties.
- ``type.fonts[]`` → one ``@font-face`` block per entry.
- ``motion`` emits a ``prefers-reduced-motion`` block that zeros the three
  durations (keeps eases — their shape is fine when duration is 0).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS_JSON = ROOT / "design-system/tokens.json"
TOKENS_CSS = ROOT / "design-system/tokens.css"

_REF = re.compile(r"\{([a-z0-9-]+)\}")


def _resolve(value: str) -> str:
    return _REF.sub(lambda m: f"var(--{m.group(1)})", value)


def _decl(name: str, value: str) -> str:
    return f"--{name}:{_resolve(value)};"


def generate(tokens: dict) -> str:
    color_light: list[str] = []
    color_dark: list[str] = []
    for t in tokens.get("color", {}).get("tokens", []):
        val = t["value"]
        if isinstance(val, dict):
            color_light.append(_decl(t["name"], val["light"]))
            color_dark.append(_decl(t["name"], val["dark"]))
        else:
            color_light.append(_decl(t["name"], val))

    shadow_light: list[str] = []
    shadow_dark: list[str] = []
    for t in tokens.get("shadow", {}).get("tokens", []):
        val = t["value"]
        if isinstance(val, dict):
            shadow_light.append(_decl(t["name"], val["light"]))
            shadow_dark.append(_decl(t["name"], val["dark"]))
        else:
            shadow_light.append(_decl(t["name"], val))

    root: list[str] = []
    for section in ("spacing", "radius"):
        for t in tokens.get(section, {}).get("tokens", []):
            root.append(_decl(t["name"], t["value"]))
    for key, value in tokens.get("type", {}).get("families", {}).items():
        root.append(f"--font-{key}:{value};")
    for t in tokens.get("motion", {}).get("tokens", []):
        root.append(_decl(t["name"], t["value"]))

    out: list[str] = []
    out.append(
        ':root, [data-theme="light"]{'
        + "".join(color_light + shadow_light)
        + "}"
    )
    out.append(
        '[data-theme="dark"]{'
        + "".join(color_dark + shadow_dark)
        + "}"
    )
    out.append(":root{" + "".join(root) + "}")
    # Zero durations under prefers-reduced-motion — eases keep their shape.
    reduced = [t["name"] for t in tokens.get("motion", {}).get("tokens", [])
               if t["name"].startswith("anim-")]
    if reduced:
        decls = "".join(f"--{n}:0ms;" for n in reduced)
        out.append("@media (prefers-reduced-motion: reduce){:root{" + decls + "}}")
    for f in tokens.get("type", {}).get("fonts", []):
        family = f["family"].replace("'", "\\'")
        out.append(
            "@font-face{"
            f"font-family:'{family}';"
            f"src:url('../{f['file']}');"
            f"font-weight:{f['weight']};"
            "}"
        )
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true", help="overwrite tokens.css")
    group.add_argument("--check", action="store_true",
                       help="exit 1 if generated output differs from tokens.css")
    parser.add_argument("--json", type=Path, default=TOKENS_JSON)
    parser.add_argument("--css", type=Path, default=TOKENS_CSS)
    args = parser.parse_args(argv)

    tokens = json.loads(args.json.read_text(encoding="utf-8"))
    generated = generate(tokens)

    if args.write:
        args.css.write_text(generated, encoding="utf-8")
        print(f"wrote {args.css}")
        return 0
    if args.check:
        current = args.css.read_text(encoding="utf-8") if args.css.exists() else ""
        if current.strip() != generated.strip():
            print(f"DRIFT: {args.css} differs from `{args.json} → generated`.")
            print("Run `uv run python tools/gen_tokens_css.py --write` to update, "
                  "or reconcile tokens.json.")
            return 1
        print("ok: tokens.css matches tokens.json")
        return 0
    sys.stdout.write(generated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
