Generate a detailed swing accumulation plan for a stock the user already holds.

Usage: /plan TICKER (e.g., /plan NBIS)

Steps:
0. Run `python3 scripts/distribution_days.py` — check market health BEFORE planning rebuys.
   If HIGH/SEVERE: warn user that rebuy orders may need to be paused or reduced in size.
   If NORMAL/CAUTION: proceed normally.
1. ALWAYS read state/holdings/current.yaml to get the user's EXACT position: shares, avg cost, account(s), and current value
2. ALWAYS read state/holdings/goals.yaml to get the accumulation target and shares gained so far
3. ALWAYS read state/progress/tracker.yaml to check:
   - Current accumulation progress and history for this ticker
   - Any open swing cycles (avoid overlapping cycles)
   - Pending orders already placed
   - Cash available (free_cash_after_commitments)
   - Previous cycle results (learn from what worked)
4. Check state/theses/ for a thesis file on this ticker. If found, read it and factor the original thesis reasoning into the plan (e.g., don't trim a "wave ambush" position the same way you'd trim a mature holding).
5. Read skills/swing-accumulator/SKILL.md for the full framework (trim thresholds, rebuy logic, core/swing split rules)
6. Read skills/news-catalyst-analyst/SKILL.md for catalyst reasoning framework
7. Run `python3 scripts/fetch_price_data.py $ARGUMENTS` for current price, RSI, MAs, volume, swing score
8. Use web search to check for upcoming catalysts, earnings dates, political/geopolitical events, and news that could affect this stock's near-term trajectory. Apply second-order reasoning and historical precedent matching.
9. Produce a catalyst modifier (STRONG_POSITIVE to STRONG_NEGATIVE) and factor it into the plan timing:
   - If STRONG_POSITIVE catalyst upcoming: recommend waiting to trim until after catalyst plays out (potential higher trim price)
   - If NEGATIVE catalyst: recommend trimming sooner or at lower threshold
   - If NEUTRAL: proceed with pure technical levels
10. Calculate using REAL numbers from the holdings file:
   - Core position (50% of actual shares, untouchable)
   - Swingable portion (remaining shares)
   - If in trim zone: exact shares to sell = swingable x trim% , at what limit price
   - Rebuy Level 1: 60% of trim proceeds / L1 price = exact share count
   - Rebuy Level 2: 40% of trim proceeds / L2 price = exact share count
   - Expected net share gain from full cycle
   - Progress toward accumulation goal after cycle completes
11. Present specific limit order instructions: ticker, direction, share count, limit price, order type (GTC)
12. Include risk section: what if stock doesn't pull back, what if it drops too far
13. Include catalyst timing note: any reason to wait or accelerate the plan based on upcoming events

Every number in the output must come from real position data. The user wants to see the math and place orders directly from this output.

## Action Tracking (REQUIRED)

14. ALWAYS write the plan's action items to `state/actions/plan_TICKER_YYYY-MM-DD.md`:

```markdown
# Accumulation Plan — TICKER — YYYY-MM-DD

## Plan Summary
- Current shares: XXX
- Target shares: XXX
- This cycle expected gain: +XX shares
- Progress after cycle: XX% of goal

## Actions
| # | Action | Shares | Price | Type | Status | Updated |
|---|--------|--------|-------|------|--------|---------|
| 1 | TRIM | XX | $XXX | LIMIT GTC | SUGGESTED | YYYY-MM-DD |
| 2 | REBUY L1 | XX | $XXX | LIMIT GTC | SUGGESTED | YYYY-MM-DD |
| 3 | REBUY L2 | XX | $XXX | LIMIT GTC | SUGGESTED | YYYY-MM-DD |
```

15. Register the new swing cycle in state/progress/tracker.yaml under swing_cycles (if a trim is suggested).
16. Update pending_orders in tracker.yaml with any new suggested orders.
17. Tell the user: "Plan saved to state/actions/plan_TICKER_YYYY-MM-DD.md. Tell me when you place orders and I'll update the tracker."

## Tracking User Confirmations

When the user says they placed orders or executed part of the plan:
1. Update the plan action tracker status (SUGGESTED -> EXECUTED)
2. Update state/progress/tracker.yaml:
   - Add/update swing_cycles entry
   - Update pending_orders
   - Update cash_flow committed amounts
   - Add history entry to accumulation_goals
