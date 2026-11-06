# Wazn

**وزن — استثمار حلال… بوزن دقيق.**
*Halal capital, precisely weighted.*

Wazn (وزن) is a Sharia-compliant, multi-strategy quant system for the Egyptian Exchange. It trades only EGX33 Shariah constituents, through the EFG Hermes Younit API, and grows into a family of products: screening, purification, the engine and a white-label agent. This file is the brand book. Every page, deck, dashboard and agent output in the Wazn name starts here.

---

## 1. The idea

**وزن** means *weight*. In a quant portfolio the final output of every model is a set of weights. In the Qur'an the word comes with a command: «وَأَقِيمُوا الْوَزْنَ بِالْقِسْطِ وَلَا تُخْسِرُوا الْمِيزَانَ» (Ar-Raḥmān 55:9), *establish the weight with justice and do not skimp the balance*. The brand sits exactly where those two meanings meet: rigorous numbers, held to a standard.

**The mark** is that idea drawn: three weights of different sizes standing on one beam, balanced on a single fulcrum. They are not equal, but they are in balance. That is risk parity, and it is the promise: *different weights, balanced risk*. (The moments really do balance: 12 × 20.5 + 22 × 8.5 ≈ 21 × 20.5.)

### What Wazn is

- **Disciplined:** rules decide, the AI advises, the owner approves. Nothing moves money on a hunch.
- **Transparent:** every number shows where it came from, every order shows why it exists.
- **Compliant by construction:** the Sharia rules are code that fails closed, not a disclaimer.
- **Bilingual by default:** Arabic first, English always available, numbers always readable.

### What Wazn is not

Not a get-rich app, not a signals channel, not a mosque-and-crescent cliché. No green-and-gold Islamic décor, no stock-ticker rockets, no 🚀.

---

## 2. Voice

| We say | We don't say |
| --- | --- |
| «النموذج بيقترح ٣ أوامر، ومحتاجة موافقتك» | «فرصة ذهبية! اشتري دلوقتي» |
| «العائد الحقيقي بعد التضخم: +4.1%» | «أرباح مضمونة» |
| «السهم ده خرج من EGX33، فهيتباع على مدار ٥ أيام» | «تم بيع السهم» (without the reason) |
| "Compliant · Watchlist · Excluded" | "Halal ✅ / Haram ❌" |

- **Direct, senior, calm.** Short sentences. Facts first, then the reason, then what happens next.
- **Arabic:** clear Modern Standard Arabic for product UI, reports and anything public. Egyptian Arabic is fine in community posts and chat with the owner. Never mix the two in one sentence.
- **Numbers carry their unit and their benchmark:** «+2.3% مقابل EGX33 +1.1%», never a bare «+2.3%».
- **Never promise returns.** Every performance figure carries its period and the line «الأداء السابق لا يضمن النتائج المستقبلية» in reports.
- **Fiqh terms are used exactly:** متوافق، تحت المراقبة، مستبعد، تطهير، زكاة. We don't issue rulings; we cite the standard (EGX33 methodology, AAOIFI No. 21).
- **Product names:** "Wazn" + a product word: Wazn Screen, Wazn Purify, Wazn Engine, Wazn Agent. In Arabic: «وزن» + the noun: وزن الفلترة، وزن التطهير، وزن المحرك، وزن الوكيل.

---

## 3. Logo

Files are in **Assets → Logos** (outlined SVG, no font needed).

| Asset | When |
| --- | --- |
| `wazn-logo-en` / `-reverse` | English or bilingual pages where reading starts left. Mark leads. |
| `wazn-logo-ar` / `-reverse` | Arabic-first surfaces. Mark sits on the right, where Arabic reading starts. |
| `wazn-logo-stacked` / `-reverse` | Square spaces: covers, social avatars, the first slide of a deck. |
| `wazn-mark` and mono versions | Under 24px tall, favicons, watermarks, chart corners. |
| `wazn-app-icon`, `wazn-favicon` | App stores, browser tabs, MCP server icons. |

**Colour:** weights in `--ink`, beam and fulcrum in `--brass`. Reverse: weights in `--on-brand`, beam in dark-theme `--brass`. Single-colour versions for print, embossing and fax-grade PDFs.

**Clear space:** the height of the beam-plus-fulcrum (≈ 45% of the mark height) on every side. **Minimum size:** mark 16px tall on screen (favicon version), 24px for lockups, 8mm in print.

**Never:** recolour the weights brass or the beam ink; rotate or tilt the beam (it is level on purpose); make the weights equal; add a crescent, a dome, a coin or a chart line; set "Wazn" in another font; put the logo on a photo without a solid `--brand-ink` or `--surface-0` panel behind it.

---

## 4. Colour

Two themes: **Paper** (light, default) and **Graphite** (dark). Values and contrast are on every token in the Colors view.

- **The core trio:** `--brand-ink` (Wazn Ink `#111111`), `--brass` (Wazn Brass `#B88A3E`), `--surface-0` (Paper `#FFFFFF`). Roughly 70 / 5 / 25 on any brand surface: paper ground, ink type and blocks, brass as the single accent — used sparingly.
- **Monochrome by default.** If a colour is not carrying meaning (compliance state, gain/loss, warning), it is not brass. The palette is deliberately narrow; restraint is the brand.
- **Brass is an accent, never body text.** For readable brass use `--brass-text`.
- **Status colours are earned:** `--positive`, `--negative` and `--warning` only ever mean gain/loss or compliance state, and are always paired with ▲/▼ or a word. Positive and negative also differ in lightness, so they hold up in greyscale and for colour-blind readers.
- **Charts:** series 1 `--ink`, series 2 `--brass`, series 3 `--line-strong`, benchmark dashed in `--ink-muted`. More than 3 series means the chart needs splitting.
- **No gradients, no shadows on cards.** Flat fields separated by hairlines. `shadow-float` exists only for things that genuinely float (menus, the approval sheet).

### Measured contrast (WCAG 2.1)

Computed from the token hex values (WCAG relative-luminance formula). Targets: **4.5:1 for small text (<24px / <19px bold)**, **3:1 for large text and non-text UI (SC 1.4.3 / 1.4.11)**. Values rounded to two decimals.

| Pair                                 | Paper (light) | Graphite (dark) | Verdict                      | Allowed use                                            |
| ------------------------------------ | ------------: | --------------: | ---------------------------- | ------------------------------------------------------ |
| `ink` on `surface-0`                 |     **18.88** |       **17.47** | AAA                          | All body text, headings, chart series 1                |
| `ink-muted` on `surface-0`           |      **7.46** |        **8.04** | AAA                          | Labels, captions, axis ticks                           |
| `ink-muted` on `surface-1`           |      **7.46** |        **7.43** | AAA                          | Card secondary text                                    |
| `ink-muted` on `surface-2`           |      **6.90** |        **6.85** | AAA                          | Zebra rows, code blocks                                |
| `brass` on `surface-0`               |      **3.11** |        **8.31** | AA Large / AAA               | Fills and 24px+ type only — **never body text**        |
| `brass-text` on `surface-0`          |      **7.50** |       **10.49** | AAA                          | Readable brass: links, small accent labels, focus ring |
| `on-brand` on `brand-ink`            |     **18.88** |       **15.55** | AAA                          | Text on primary brand surfaces                         |
| `on-brass` on `brass`                |      **6.06** |        **8.31** | AAA                          | Text on brass fills                                    |
| `positive` on `surface-0`            |      **6.24** |        **9.84** | AAA                          | Gain labels, compliant badges                          |
| `negative` on `surface-0`            |      **7.35** |        **6.49** | AAA                          | Loss labels, excluded badges                           |
| `warning` on `surface-0`             |      **4.97** |        **8.91** | AA / AAA                     | Watchlist state                                        |
| `line-strong` on `surface-0`         |      **2.05** |        **2.21** | **fails 3:1** non-text       | See note below                                         |

**Rules that follow from the table:**

- `brass` on light paper is **3.11:1** — fine for 24px+ display, logo accents, icons; **never** for body copy. For small brass text use `brass-text` (7.50:1 light / 10.49:1 dark).
- All text-ink pairs comfortably clear AAA on both themes; this is by design — brand voice is calm and dense, so readability is the headline property.
- Status colours differ in lightness as well as hue, so they still read in greyscale and for colour-vision deficiencies. Always pair with ▲/▼ or a word.
- Focus rings use `brass-text` at 1.5px with 2–3px offset: contrast against `surface-0` is **7.50:1** (light) / **10.49:1** (dark), well over the 3:1 non-text minimum.
- **Known issue — `line-strong` fails 3:1 against `surface-0`** on both themes. It is used for control borders (inputs, secondary buttons). Options: darken the light-theme value toward `#8A8A8A` (≈3.3:1) and lift the dark value toward `#6A6A6A` (≈3.0:1), or rely on `focus-visible` + hover state for perceivable boundaries. Decide before the brand version ships to a second consumer (tracked under brand roadmap).

---

## 5. Typography

| Role | Family | Why |
| --- | --- | --- |
| Display | **Readex Pro** (variable 160–700) | Geometric Arabic + Latin from one design, so «وزن» and "Wazn" feel like one word. Used for the logo, headlines, covers. |
| Text | **IBM Plex Sans Arabic** | Engineered, very legible Arabic with matching Latin. Everything users read. |
| Numbers | **IBM Plex Mono** | Tabular figures that line up in tables. Every price, weight, percentage and ticker. |

- Body leading is generous (16/28) because Arabic dots and marks need the room.
- Numbers are always LTR and Western digits (0–9) inside RTL layouts. Wrap them in `.wz-num`.
- Headings use weight, not size jumps: 600 for titles, 400 for reading, 500 for labels.
- All three families are SIL Open Font License; the files and licences are in `fonts/`.

---

## 6. Layout and shape

- **4px grid:** spacing tokens `space-1` … `space-24`; card padding `space-6`, page margins `space-16`, chapter breaks `space-24`.
- **Near-zero radii:** `radius-sm` 0px, `radius-md` 2px, `radius-lg` 4px. Wazn is a ledger, not a toy: sharp corners, straight edges.
- **Borders before shadows:** 1px hairlines in `--line`; `shadow-float` only for genuinely floating surfaces.
- **Negative space is a material.** Prefer whitespace to dividers, dividers to borders, borders to boxes. If a container has nothing to separate, it should not exist.
- **One accent per screen.** Brass appears once; everything else is monochrome.
- **RTL first:** layouts are designed in Arabic, mirrored for English. Charts, number columns and code stay LTR.

---

## 7. Iconography and imagery

- **Icons:** 1.5px stroke, square caps, 20px grid, `currentColor`. Draw from three primitives only: bar, beam, triangle (the mark's parts) plus plain geometry. Pair any icon with a label in decision contexts.
- **Status shapes:** circle = compliant, diamond = watchlist, dash = excluded (see ComplianceBadge).
- **Imagery:** real charts from real data, never stock photos of traders, skylines or coins. No people photography in the product.
- **Illustration:** compositions of the mark's geometry (bars, beams, fulcrums) in brand colours, as on the cover.

### Shipped icon set

Files are in **`logos/icons/`** (20×20 viewBox, inherit `currentColor`, no fill except on brand marks). Inline them via `<img>` with CSS `color`, or copy-paste the SVG where `currentColor` must follow theme.

| Icon           | Purpose                                                       |
| -------------- | ------------------------------------------------------------- |
| `chart`        | Reports, performance pages, series toggles                    |
| `shield-check` | Compliance verdicts, "verified" badges, audit trail entries   |
| `scale`        | Weight / allocation views; echoes the Wazn mark               |
| `check`        | Pass state in checklists and confirmation flows               |
| `cross`        | Dismiss, close, failed check                                  |
| `menu`         | Nav menu toggle on narrow viewports                           |
| `arrow`        | "Learn more", next step, directional call-to-action           |
| `info`         | Inline tooltip trigger beside a label or ratio                |
| `warning`      | Watchlist row, stale data, pending reconciliation             |
| `external`     | Links that leave the Wazn surface (docs, GitHub, email)       |
| `github`       | GitHub links and footers                                      |
| `mail`         | Email the team, email digests                                 |

**Favicon:** `logos/favicon.svg` is the primary; `logos/favicon.ico` (16/32/48) is the fallback for browsers and clients that don't fetch SVG favicons.

---

## 8. Components

Wazn's UI kit ships as CSS classes with the `wz-` prefix (`components/bundle.css`), on top of the tokens: **Button**, **ComplianceBadge**, **Stat**, **WeightBar** (the signature component) and **HoldingsTable**. Each card shows its states and lists what the consumer must provide.

---

## 9. Product family

| Product | Arabic | What it is | Asset |
| --- | --- | --- | --- |
| Wazn Screen | وزن الفلترة | Sharia screening MCP server and API (open entry point) | `wazn-screen` |
| Wazn Purify | وزن التطهير | Purification and zakat calculation | `wazn-purify` |
| Wazn Engine | وزن المحرك | The multi-strategy quant engine (internal) | `wazn-engine` |
| Wazn Agent | وزن الوكيل | White-label agent for brokers | `wazn-agent` |

Lockup rule: mark + "Wazn" (Readex 600, `--ink`) + product word (Readex 300, `--brass`) on one baseline, Arabic name beneath in IBM Plex Sans Arabic, `--ink-muted`.

---

## 10. Regulatory and naming guardrails

- Don't use «صندوق», "Fund", "Capital" or "Asset Management" in any Wazn product name or headline before the relevant FRA licence exists.
- Every public performance figure: period, benchmark, after costs, and the past-performance line.
- Example tickers in this system are illustrative only; they are not an EGX33 list or a recommendation.
