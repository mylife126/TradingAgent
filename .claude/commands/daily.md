Run the daily market scan and swing accumulator workflow.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

0. ALWAYS read state/progress/financial_goal.yaml FIRST — understand the target ($1M in 2 years, 23.4% CAGR required). Every recommendation must be evaluated against: "Does this help reach the goal?" Frame the daily summary with a brief goal status note.
1. ALWAYS read state/holdings/current.yaml first to get all positions with exact shares, avg cost, and accounts
2. ALWAYS read state/holdings/goals.yaml to get accumulation targets and strategy for each holding
3. ALWAYS read state/progress/tracker.yaml to check:
   - Open swing cycles and their rebuy targets (did any fill overnight?)
   - Pending orders (still active or expired?)
   - Position builds in progress
   - Cash flow state
4. ALWAYS check state/theses/ for any thesis files. Read them to understand WHY the user holds each position. If today's news/price action invalidates a thesis, flag it prominently.
5. Check state/actions/ for the most recent action tracker file. If there are SUGGESTED actions still pending, remind the user.
6. Read skills/market-scanner/SKILL.md for the market scanning framework
7. Read skills/swing-accumulator/SKILL.md for scoring interpretation and trim/rebuy logic
8. Read skills/news-catalyst-analyst/SKILL.md for news/catalyst reasoning framework
9. Use web search to check today's market-moving news: major political events (Trump posts, executive orders, trade negotiations), geopolitical developments, sector catalysts, earnings reports. Apply second-order logical reasoning (e.g., "Trump visits China with Boeing CEO -> 2017 precedent -> aerospace deal likely")
10. Run `python3 scripts/fetch_price_data.py` on the individual stock tickers from holdings (skip index funds like QQQ, VTSAX, FSKAX, SOXX unless user asks)
11. For each holding, calculate swing score AND catalyst modifier. Final action = technical signal adjusted by catalyst context
12. Present a consolidated daily action plan with specific prices, share counts, and recommendations (HOLD / TRIM X% / REBUY ZONE)
13. If any score is >= 6 (after catalyst adjustment), generate specific limit order instructions: ticker, buy/sell, share count, limit price, order type (GTC)
14. If any catalyst is STRONG_POSITIVE or STRONG_NEGATIVE, highlight it prominently even if the technical score alone wouldn't trigger action

The output MUST use real position data -- never give generic advice. Keep concise: market regime + catalyst summary + holdings signal table + specific action items.

## Position Building Scan (REQUIRED)

15. ALWAYS read state/actions/position_build_plan_2026-05-18.md (or most recent position build plan) to get all active position builds and their buy alert conditions.
16. Run `python3 scripts/fetch_price_data.py` on ALL position build tickers (GOOGL, COHR, RKLB, MSTR, and any others in the build plan) even if not currently held.
17. Check each ticker against its BUY ALERT condition from the build plan:
    - GOOGL: RSI <55 AND price ≤$380 → "BUY ALERT: GOOGL entering buy zone"
    - COHR: RSI <50 AND price ≤$345 → "BUY ALERT: COHR photonics ambush"
    - RKLB: RSI <50 AND price ≤$100 → "BUY ALERT: RKLB pullback zone"
    - MSTR: Price ≤$158 AND context (BTC stable) → "BUY ALERT: MSTR dip"
    - APP: Price ≤$465 → "BUY ALERT: APP near GTC level"
    - NBIS: Price ≤$185 → "BUY ALERT: NBIS additional accumulation zone"
18. Present a "Position Build Status" section after the holdings scan:
    - Show each build target with current price vs entry price and % gap
    - If ANY alert fires: highlight with ⚠️ and specific action instruction
    - If price is within 5% of trigger: flag as "APPROACHING — be ready"

## Action Tracking (REQUIRED)

15. After presenting the daily plan, ALWAYS write suggested actions to `state/actions/daily_YYYY-MM-DD.md`:

```markdown
# Daily Action Tracker — YYYY-MM-DD

## Market Context
- Regime: [BULL/BEAR/NEUTRAL]
- Key catalysts: [brief summary]

## Suggested Actions
| # | Action | Ticker | Shares | Price | Type | Status | Updated |
|---|--------|--------|--------|-------|------|--------|---------|
| 1 | TRIM/BUY/HOLD | XXXX | NN | $XXX | GTC | SUGGESTED | YYYY-MM-DD |

## Pending Order Updates
| Ticker | Order | Current Price | Gap to Fill | Notes |
|--------|-------|---------------|-------------|-------|
| NBIS | BUY 19@$195 | $XXX | X% | Still valid / Cancel / Adjust |
```

16. Update state/progress/tracker.yaml if any pending orders filled or swing cycle status changed.

## Tracking User Confirmations

When the user says they executed an action (e.g., "I trimmed NBIS", "I placed the META order"):
1. Read the most recent daily action tracker from state/actions/
2. Update the matching action's Status to EXECUTED or SKIPPED
3. Update state/progress/tracker.yaml accordingly (shares, cash flow, cycle status)
4. Save both files
