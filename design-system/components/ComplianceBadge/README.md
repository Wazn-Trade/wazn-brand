# ComplianceBadge

The Sharia status of a security, shown everywhere a ticker appears in a decision context.

| State | Class | Meaning | Shape |
| --- | --- | --- | --- |
| متوافق · Compliant | `wz-badge--compliant` | In the current EGX33 Shariah snapshot and passes the AAOIFI screen. Buyable. | circle |
| تحت المراقبة · Watchlist | `wz-badge--watch` | In EGX33 but our AAOIFI early-warning screen flags it. Hold, no new buys. | diamond |
| مستبعد · Excluded | `wz-badge--excluded` | Not in EGX33 or a banned class. Sell-only. | dash |

- Each state has its own shape as well as its own colour, so it reads in greyscale and for colour-blind users.
- The label is always text. Never show the dot alone.
- Badge text is the status only. Reasons go in a tooltip or the row detail, quoting the rule that fired.
- The consumer provides the state; never compute compliance in the UI.
