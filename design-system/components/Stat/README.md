# Stat

A single headline figure with its label and change, for dashboards and reports.

- `wz-stat__label` (13px, `--ink-muted`) names the figure and its unit: «قيمة المحفظة (ج.م)».
- `wz-stat__value` uses the `figure-l` style: IBM Plex Mono, tabular, always LTR even inside RTL layouts, so digits never reorder. It sits at the reading start (right in Arabic, left in English).
- `wz-stat__delta` is sans text; wrap the number in `wz-num` (`▲ <span class="wz-num">+2.31%</span> منذ بداية الشهر`).
- `wz-stat__delta--up` / `--down` always carry ▲ / ▼ as well as colour.
- Use Western digits (0–9) for all money and percentages; Arabic-Indic digits are fine in prose dates.
- Minus sign is U+2212 (−), not a hyphen.
- The consumer provides the formatted string; the component does no maths.
