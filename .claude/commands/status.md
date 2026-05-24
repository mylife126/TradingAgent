Show a unified portfolio dashboard — the single source of truth for all progress.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

Usage: /status

This command presents ONE consolidated view of everything:
- Financial goal progress (am I on track for $1M?)
- All holdings with adjusted cost basis (including option income)
- Accumulation goals progress (% toward each target)
- Active swing cycles (open/completed, shares gained)
- Position builds (GTC orders, how close to filling)
- Adjusted cost basis per stock (original cost - option income - swing profits)
- Next actions (what to do today)

Steps:
1. Read state/progress/financial_goal.yaml — goal status
2. Read state/holdings/current.yaml — all positions
3. Read state/holdings/goals.yaml — accumulation targets
4. Read state/progress/tracker.yaml — swing cycles, builds, cash flow
5. Read state/cost_basis/adjusted_costs.yaml — option income, adjusted costs
6. Run `python3 scripts/fetch_price_data.py` on key holdings for current prices
7. Calculate and present the unified dashboard

Output format:

```
═══ PORTFOLIO DASHBOARD — [DATE] ═══

🎯 FINANCIAL GOAL
$[current] / $1,000,000 | [X]% complete | [AHEAD/BEHIND] by $[X]
Required: 23.4% CAGR | Actual so far: [X]%

📊 HOLDINGS OVERVIEW (by adjusted cost)
| Ticker | Shares | Orig Cost | Option Income | Adj Cost/sh | Current | True P&L% |
[sorted by position size]

🎯 ACCUMULATION PROGRESS
| Ticker | Have | Target | Progress | Strategy | Next Action |
[progress bars]

🔄 SWING CYCLES
| Cycle | Status | Trimmed | Rebought | Shares Gained | Cash Generated |
[active and completed cycles]

🏗️ POSITION BUILDS  
| Ticker | GTC Order | Current Price | Gap | Fill Probability |
[all pending orders]

💰 CASH & COST STRATEGY
| Ticker | Monthly Option Income | Months to Zero Cost | Current Adj Cost |
[which stocks you're running wheel/options on]

⚡ NEXT ACTIONS (Top 3 Priority)
1. [Most urgent action]
2. [Second priority]
3. [Third priority]
```

This is the "one command to rule them all" — run it anytime to see where you stand.
