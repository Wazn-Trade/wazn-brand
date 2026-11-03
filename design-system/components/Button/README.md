# Button

Buttons trigger one clear action; Wazn has four kinds and one of them is reserved for stopping things.

| Kind | Class | Use |
| --- | --- | --- |
| Primary | `wz-btn wz-btn--primary` | The one action the screen exists for: approve a rebalance, confirm an order batch. One per view. |
| Accent | `wz-btn wz-btn--accent` | Research and analysis actions (run backtest, generate report). Never for money-moving actions. |
| Secondary | `wz-btn wz-btn--secondary` | Everything else: review, export, cancel a dialog. |
| Danger | `wz-btn wz-btn--danger` | Kill switch, cancel all open orders. Outline only, never a filled red slab. Always followed by a confirmation. |

- Size: 40px default, `wz-btn--sm` (32px) inside tables and approval rows.
- Labels are verbs in the user's language: «اعتماد», «تشغيل», «مراجعة». No «OK».
- Focus ring: 2px `--focus` at 2px offset. Never remove it.
- The consumer provides the `<button>` element, its label and handler; the classes give everything else.
