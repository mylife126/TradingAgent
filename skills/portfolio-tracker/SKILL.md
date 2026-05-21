---
name: portfolio-tracker
description: Import holdings from Fidelity and Robinhood CSV exports, reconcile positions, calculate performance metrics, and maintain a master spreadsheet. Trigger when user provides brokerage exports, asks about portfolio performance, or requests holdings update.
---

# Portfolio Tracker

## Purpose

Maintain a single source of truth for all holdings across Fidelity and Robinhood accounts. Track cost basis, current value, P&L, and share count changes over time.

## Data Import

### Fidelity CSV Format
Expected columns (from Fidelity Positions export):
- Account Name/Number
- Symbol
- Description
- Quantity
- Last Price
- Current Value
- Today's Gain/Loss Dollar
- Today's Gain/Loss Percent
- Total Gain/Loss Dollar
- Total Gain/Loss Percent
- Cost Basis Per Share
- Cost Basis Total
- Type (Cash, Margin, Short)

### Robinhood CSV Format
Expected columns (from Robinhood account statement):
- Symbol (Instrument)
- Quantity
- Average Cost
- Total Cost
- Current Price
- Market Value
- Unrealized P&L
- Unrealized P&L %

### Import Process
1. User places CSV files in `data/fidelity/` or `data/robinhood/`
2. Script parses and normalizes to common format
3. Reconcile: detect new positions, closed positions, share count changes
4. Update master holdings state in `state/holdings/`
5. Generate change report showing what's different from last import

## Master Holdings State

File: `state/holdings/current.yaml`

```yaml
last_updated: "2026-05-14"
accounts:
  fidelity:
    - ticker: NBIS
      shares: 175
      avg_cost: 42.50
      current_price: 58.00
      market_value: 10150.00
      unrealized_pnl: 2712.50
      unrealized_pnl_pct: 36.47
      sector: Technology
      first_purchased: "2025-08-15"
  robinhood:
    - ticker: NBIS
      shares: 50
      avg_cost: 45.00
      # ... etc
consolidated:
  - ticker: NBIS
    total_shares: 225
    weighted_avg_cost: 43.06
    total_value: 13050.00
    total_pnl: 3361.50
    total_pnl_pct: 34.69
    goal: accumulate
    target_shares: 500
    progress_pct: 45.0
```

## Performance Tracking

### Metrics Calculated
- Per-position: P&L ($, %), daily/weekly/monthly change, share count delta
- Portfolio-level: Total value, total P&L, allocation %, concentration risk
- Goal tracking: Current shares vs target shares, progress %
- Share growth: Shares gained through swing trading (not new cash)

### Spreadsheet Output

Generate/update `reports/portfolio_summary.csv` with columns:
- Ticker, Account, Shares, Avg Cost, Current Price, Market Value
- Unrealized P&L ($), Unrealized P&L (%)
- Weight (% of portfolio), Sector
- Goal, Target Shares, Progress %
- Shares Gained (swing), Swing P&L

## Workflow

1. **Import**: Parse new CSV files from data/ directories
2. **Reconcile**: Compare with previous state, flag changes
3. **Calculate**: Update all performance metrics
4. **Report**: Generate summary report with highlights
5. **Archive**: Move processed CSVs to data/{broker}/archive/

## Change Detection Report

When new data is imported, highlight:
- New positions (didn't exist before)
- Closed positions (existed before, now gone)
- Share count changes (buys or sells detected)
- Significant price moves (>5% since last import)
- Cost basis changes (additional purchases)

## Output

```markdown
## Portfolio Update — [DATE]

### Summary
- Total Portfolio Value: $[X]
- Total Unrealized P&L: $[X] ([%])
- Positions: [N] across [N] accounts
- Changes since last update: [N] modifications

### Top Performers
1. [TICKER]: +[%] ($[X])
2. ...

### Underperformers
1. [TICKER]: -[%] ($[X])
2. ...

### Accumulation Progress
| Ticker | Current | Target | Progress | Shares Gained (Swing) |
|--------|---------|--------|----------|-----------------------|
| NBIS   | 175     | 500    | 35%      | +12                   |

### Alerts
- [Any concentration risks, goal milestones, significant moves]
```
