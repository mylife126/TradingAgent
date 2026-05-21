Run the weekly portfolio review workflow.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

0. ALWAYS read state/progress/financial_goal.yaml FIRST. Calculate current portfolio value vs. milestone schedule. Report: ON TRACK / AHEAD / BEHIND / CRITICAL. If BEHIND, the weekly review must prioritize actions that close the gap (accelerate swing cycles, cleanup dead money, concentrate into winners). If AHEAD, note it and maintain discipline.
1. Check data/fidelity/ and data/robinhood/ for new CSV files
2. If CSVs found: run `python3 scripts/import_holdings.py` to parse and update state
3. If no CSVs found: use existing state/holdings/current.yaml
4. ALWAYS read state/holdings/current.yaml and state/holdings/goals.yaml for full position context
5. ALWAYS read all files in state/theses/ to understand investment theses. Flag any thesis that is being validated (good) or invalidated (bad) by this week's price action or news.
6. ALWAYS read state/progress/tracker.yaml for the full progress picture:
   - Accumulation goal progress
   - Open swing cycles
   - Position builds
   - Pending orders
   - Cash flow state
7. Read all files in state/actions/ from the past week to review what was suggested vs. executed vs. skipped
8. Run `python3 scripts/generate_report.py` to update the portfolio spreadsheet and weekly report
9. Run `python3 scripts/fetch_price_data.py` on individual stock holdings for current prices and swing scores
10. Read skills/swing-accumulator/SKILL.md for trim/rebuy logic
11. Read skills/news-catalyst-analyst/SKILL.md for catalyst reasoning
12. Use web search to check: major news/events for the upcoming week (earnings calendar for holdings, Fed meetings, political events, trade negotiations, sector catalysts). Flag any that could affect holdings.
13. Present: portfolio summary, top/bottom performers, accumulation progress vs goals.yaml, swing signals with catalyst context, and recommended actions for next week
14. For any holding with upcoming catalyst: note it explicitly (e.g., "NBIS: AI summit next Tuesday -- hold trim until after")

Ask me to drop CSVs first if state/holdings/current.yaml doesn't exist yet.

## Position Building Review (REQUIRED)

14b. ALWAYS read state/actions/position_build_plan_2026-05-18.md (or most recent position build plan).
14c. Run `python3 scripts/fetch_price_data.py` on ALL position build tickers (GOOGL, COHR, RKLB, MSTR, and any others in plan) — even if not currently held.
14d. For each position build, report:
    - Current price vs target entry price → % gap → is it getting closer or further?
    - Has the 20-MA or 50-MA shifted? Should limit prices be adjusted?
    - Any new catalysts that change the timing or urgency?
    - Status: FILLING / APPROACHING / STALLED / NEEDS ADJUSTMENT
14e. If any build target moved MORE than 10% away from limit price (stock rallied, limit too low):
    - Flag: "Consider raising limit or placing capitulation order"
14f. If any build target moved WITHIN 3% of limit price:
    - Flag: "⚠️ ABOUT TO FILL — confirm order is still active in broker"
14g. Present a "Position Build Progress" table:
    ```
    | Ticker | Target | Entry | Current | Gap | MA Shift | Status |
    |--------|--------|-------|---------|-----|----------|--------|
    | GOOGL  | 25sh   | $370  | $396    | -7% | 20MA→$376 | Approaching |
    ```

## Discrepancy Check (REQUIRED)

15. After importing new holdings data, COMPARE actual holdings (from current.yaml) against expected state (from tracker.yaml):
    - For each ticker in tracker.yaml accumulation_goals and position_builds:
      a. Look up actual shares in current.yaml
      b. Compare to tracker.yaml expected shares (current_shares or total_filled)
      c. If delta > 0.5 shares, flag a discrepancy
    - Check if any pending_orders appear to have filled (shares increased) or expired (no change after extended time)
    - Write discrepancy alerts to tracker.yaml discrepancy_alerts section

    Present discrepancies clearly:
    ```
    DISCREPANCY DETECTED:
    NBIS: Tracker expects 158.248 shares, actual 177.248 (+19)
    Likely: Rebuy L1 filled at $195. Confirm? (I'll update tracker)
    ```

16. Update state/progress/tracker.yaml with:
    - New current_shares for all accumulation goals
    - Updated cash_flow estimates
    - Closed swing cycles (if rebuys filled)
    - Filled position build tranches
    - Resolved discrepancy alerts (after user confirms)

## Action Tracking (REQUIRED)

17. Write weekly action suggestions to `state/actions/weekly_YYYY-MM-DD.md` with the same format as cleanup actions.
18. Review action tracker files from the past week — summarize execution rate:
    ```
    This week's action execution: 8/12 suggested actions executed, 2 skipped, 2 still pending
    ```

## Tracking User Confirmations

When the user confirms a discrepancy or reports an action:
1. Update state/progress/tracker.yaml (shares, cycles, cash flow, resolve discrepancy alert)
2. Update the relevant action tracker in state/actions/
3. Add a history entry to the appropriate accumulation_goals or position_builds section
