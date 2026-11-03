# tools

Regenerates every logo SVG in `../logos/svg` from code, so the marks are exact and reproducible.

```bash
pip install fonttools uharfbuzz brotli
python3 gen_assets.py
```

- `gen_assets.py`: the mark geometry (56×40 grid, balanced moments) and all lockups. Text is shaped with HarfBuzz (correct Arabic joining) and outlined, so the SVGs need no fonts.
- `textpath.py`: text → SVG path helper.
- `src-fonts/`: the TTF masters used for outlining (SIL OFL, see `../fonts/`).
