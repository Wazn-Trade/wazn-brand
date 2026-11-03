# WeightBar

Wazn's signature component: each holding's actual portfolio weight against its target, the idea the brand is named after.

- Fill = actual weight, `--brand-ink`. Target = a 2px `--brass` tick. Over the cap = fill turns `--brass` (`wz-weight--over`).
- Scale is the portfolio cap (15% per stock), not 100%: a full bar means "at the cap".
- Cash is shown last, fill `--line-strong`, no target tick.
- Bars always run left-to-right (`dir="ltr"` on `.wz-weights`) even on Arabic pages: the numbers and the scale are LTR; headings stay RTL.
- Tickers in `code` style, values in `figure` style.
- The consumer provides symbol, actual %, target % and the cap; it computes the widths.
- Watch out: the example tickers in the preview are illustrative, not a recommendation or an EGX33 list.
