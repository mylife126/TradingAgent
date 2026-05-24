Evaluate a new stock candidate for potential position building.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

Usage: /evaluate TICKER (e.g., /evaluate PLTR)

Steps:
0. ALWAYS read state/progress/financial_goal.yaml — ask: "Does this stock help reach $1M in 2 years?" Only recommend BUY if expected return exceeds the 23.4% CAGR requirement. Reject anything that dilutes concentration in proven winners.
1. ALWAYS read state/holdings/current.yaml to understand user's current portfolio context (concentration, cash available, existing exposure to same sector)
2. ALWAYS read state/holdings/goals.yaml to check if this stock already has a target or conflicts with existing goals
3. ALWAYS read state/progress/tracker.yaml to check:
   - Cash available (free_cash_after_commitments) for sizing the position
   - Existing position builds in progress (avoid overcommitting)
   - Total committed to pending orders
4. Read skills/stock-evaluator/SKILL.md for the full evaluation framework
5. Read skills/news-catalyst-analyst/SKILL.md for news/catalyst reasoning framework
6. Read skills/exposure-coach/SKILL.md — determine current market posture (NEW_ENTRY_ALLOWED / REDUCE_ONLY / CASH_PRIORITY). If CASH_PRIORITY, verdict is automatically WATCH regardless of stock quality.
6b. Run `python3 scripts/distribution_days.py` — if overall risk is HIGH or SEVERE, add a WARNING to the verdict: "Market distribution elevated. Consider WATCH even if stock is good. Timing entry for after distribution clears."
7. Read skills/position-sizer/SKILL.md — if BUY verdict, size the position using risk-based methods (1% risk per trade, max 15% concentration, respect cash constraints). Apply exposure multiplier from distribution day risk (100%/75%/50%/25%).
6. Run `python3 scripts/fetch_price_data.py $ARGUMENTS` for technical data
7. Use web search to gather: recent earnings, revenue growth, institutional ownership changes, analyst consensus, upcoming catalysts, political/geopolitical factors, Trump posts or executive signals about this company/sector
8. Apply second-order logical reasoning from the catalyst skill: identify events -> implications -> who benefits -> expected move. Match historical precedents where applicable.
9. Run the 5-question quick screen (Phase 1)
10. If it passes (3+ Yes): do the deep analysis and produce a verdict (STRONG BUY / BUY / WATCH / PASS)
11. Include a Catalyst Assessment section: what news/events/political signals support or threaten this stock, and how they affect entry timing
12. If BUY+: design an accumulation plan with specific entry tranches, position size relative to user's actual portfolio value, and stop loss
13. Format output per the template in the SKILL.md

This is the most thorough workflow -- take your time, use web search for fundamentals AND catalysts/news/geopolitics.

## Action Tracking (REQUIRED for BUY+ verdicts)

14. If the verdict is BUY or STRONG BUY, ALWAYS write to `state/actions/evaluate_TICKER_YYYY-MM-DD.md`:

```markdown
# Evaluation Action Tracker — TICKER — YYYY-MM-DD

## Verdict: [STRONG BUY / BUY / WATCH / PASS]

## Suggested Entry Plan
| # | Action | Shares | Price | Type | Status | Updated |
|---|--------|--------|-------|------|--------|---------|
| 1 | BUY tranche 1 | XX | $XXX | LIMIT GTC | SUGGESTED | YYYY-MM-DD |
| 2 | BUY tranche 2 | XX | $XXX | LIMIT GTC | SUGGESTED | YYYY-MM-DD |
| 3 | SET STOP | -- | $XXX | STOP LOSS | SUGGESTED | YYYY-MM-DD |
```

15. If verdict is BUY+, add a new entry to state/progress/tracker.yaml:
    - Under position_builds with status PLANNING
    - Under accumulation_goals if long-term accumulation is recommended
    - Update cash_flow to reflect the new commitment
16. If verdict is WATCH, note it but don't add to tracker yet.
17. Tell the user: "Evaluation saved. If you decide to build this position, tell me and I'll activate it in the tracker."

## Tracking User Confirmations

When the user says they started building the position:
1. Update evaluate action tracker status
2. Move position_builds entry from PLANNING to BUILDING in tracker.yaml
3. Update pending_orders and cash_flow
