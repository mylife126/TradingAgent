---
name: position-sizer
description: Calculate risk-based position sizes for new entries. Ensures no single trade risks more than 1-2% of portfolio. Uses fixed-fractional, ATR-based, and portfolio constraint methods to determine exact share counts.
---

# Position Sizer

## Purpose

Answer: "How many shares should I buy?" — based on risk, not gut feeling.

## Three Methods (use the TIGHTEST constraint)

### 1. Fixed Fractional (Risk per Trade)
```
Risk % = 1% of portfolio (never exceed 2%)
Dollar risk = Portfolio × Risk%
Shares = Dollar risk ÷ (Entry price - Stop loss price)
```

Example: Portfolio $656K, Entry $195, Stop $170
- Dollar risk = $656K × 1% = $6,560
- Per-share risk = $195 - $170 = $25
- Max shares = $6,560 ÷ $25 = **262 shares**

### 2. Portfolio Concentration Limit
```
Max single position = 15% of portfolio
Max sector = 30% of portfolio
Starter position = 2-3%
Target position = 5-10%
```

Example: Portfolio $656K, IONQ @ $52
- Max (15%) = $98K ÷ $52 = 1,884 shares
- Target (5%) = $33K ÷ $52 = 634 shares
- Starter (2%) = $13K ÷ $52 = 250 shares

### 3. Cash Constraint
```
Never invest more than available free cash
Account for pending GTC orders (already committed)
Shares = Free cash × allocation% ÷ price
```

## Decision Rule

**Final position size = MINIMUM of all three methods**

## Portfolio Heat (Total Open Risk)

Total open risk should stay within 6-8% of portfolio:
```
Portfolio heat = Sum of (shares × per-share risk) for all positions
If heat > 8%: Do NOT add new positions until heat decreases
```

## Integration with Financial Goal

- If goal requires 23.4% CAGR: can afford 1.5% risk per trade (slightly aggressive)
- If goal is conservative: stay at 1% risk per trade
- Asymmetric bets (EUV, IONQ): limit to 1-2% of portfolio each regardless

## When to Use

- Before every /evaluate BUY recommendation (size the entry plan)
- In /plan (size the rebuy tranches)
- In /cleanup (assess if position is oversized or undersized)
