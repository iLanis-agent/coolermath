# Cooler Math

The ice retention honesty tool. The 5-day sticker is a lab at 75 F with
the lid closed and the cooler pre-chilled. Cooler Math audits the
sticker against your weather and your lid habit, counts the ice the 2:1
rule really wants, and tells the block-versus-cubes truth.

- Live app: https://ilanis-agent.github.io/coolermath/app.html
- Landing: https://ilanis-agent.github.io/coolermath/

## What it does

1. **The sticker audit** - 8% off per 5 F above 75 (floor 40% kept),
   2% of a sticker day per lid open.
2. **The 2:1 rule** - twice the ice as contents by weight; the rule
   counts the beer too.
3. **The block truth** - a solid block outlasts the same pounds of
   cubes by half again.

## Files

- `engine.js` - pure functions (`icePlan`, `loadPlan`, `blockPlan`) plus renderers
- `app.html` - the app; `index.html` - the landing page
- `oracle.py` - independent Python mirror of the engine
- `test.js` + `expected.json` - 23 oracle cases, `node test.js` runs green

The derates are labeled norms; your meltwater keeps the honest ledger.
