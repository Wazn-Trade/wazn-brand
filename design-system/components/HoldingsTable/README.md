# HoldingsTable

The positions table: one row per holding with its Sharia status, size and P&L.

- Columns in this order (start → end): ticker, status, quantity, average cost, price, P&L. Add columns at the end.
- Header row on `--surface-2`, hairlines `--line`, no zebra and no vertical rules.
- Number cells use `wz-num`: mono, tabular, end-aligned, LTR. Text cells follow the page direction.
- P&L carries ▲/▼ and `wz-up` / `wz-down`; never colour alone.
- An excluded holding stays in the table until it's sold: the badge is the call to action.
- The consumer provides formatted strings and the status; the table does no maths.
