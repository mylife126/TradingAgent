Show all position builds: GTC orders, entry levels, gap to fill, and manage adjustments.
ALL actions serve the FINANCIAL GOAL.

Usage:
  /positions              — Show all GTC orders with current gap analysis
  /positions adjust       — Recommend which orders to raise/lower/cancel based on price movement
  /positions add TICKER   — Add a new position build with entry plan

This is the MASTER VIEW for all pending orders and position builds across all accounts.

Steps:
1. Read state/holdings/goals.yaml — all accumulation targets
2. Read state/progress/tracker.yaml — pending orders, cash flow, position builds
3. Read state/actions/position_build_plan_2026-05-18.md — the master allocation plan
4. Run `python3 scripts/fetch_price_data.py` on ALL tickers with pending GTC orders
5. Calculate for each order: current price, gap to limit, RSI, probability of fill
6. Flag orders that need attention:
   - STALE: price moved >15% away from limit (unlikely to fill, wasting commitment)
   - APPROACHING: price within 5% of limit (about to fill!)
   - FILLED: price at or below limit (check if actually filled in broker)
   - ADJUST: MA shifted significantly, original level no longer makes technical sense
7. Show cash impact: total committed, free cash, what happens if multiple fill simultaneously

Output format:
```markdown
## Position Builds Dashboard — [DATE]

### Cash Situation
| Total Cash | Committed (GTC) | Options Margin | Free | Alert |
[one-line summary]

### All GTC Orders (sorted by proximity to fill)
| # | Ticker | Shares | Limit | Current | Gap% | RSI | 20-MA | Status | Account |
[every pending order]

### Alerts
⚠️ APPROACHING: [orders within 5%]
🔴 STALE: [orders >15% away — consider cancel or adjust]
✅ LIKELY FILLED: [check broker]

### Recommendations
- Adjust: [which orders to raise/lower and why]
- Cancel: [which to free up cash]
- Add: [new orders suggested based on today's prices]

### Position Build Progress Summary
| Ticker | Goal | Have | GTC Pending | If All Fill | Progress |
[accumulation goal tracker]
```

When user says "/positions adjust":
- For each STALE order: suggest new level based on current 20-MA or 50-MA
- For each order where stock rallied away: calculate cost of raising limit vs waiting
- Always consider: does adjusting free up cash for higher-priority builds?

When user says "/positions add TICKER":
- Run quick technical scan on TICKER
- Suggest entry tranches based on support levels (20-MA, 50-MA, 200-MA)
- Check cash availability
- Present order suggestion and ask for confirmation

## Tracking
- After any adjustment: update tracker.yaml pending_orders section
- After any fill confirmation: update accumulation_goals, position_builds, cash_flow
- After adding new position: update goals.yaml and watchlist.yaml
