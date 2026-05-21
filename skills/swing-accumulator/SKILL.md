---
name: swing-accumulator
description: Generate daily/weekly swing trading signals designed to GROW share count on conviction holdings. Uses technical levels to identify trim/rebuy zones. Trigger when user says "accumulate", "grow shares", "swing plan", "trim and rebuy", or asks about selling high and buying back lower.
---

# Swing Accumulator

## Purpose

Help the user grow their share count on conviction holdings WITHOUT deploying new cash. This skill identifies opportunities to:
1. Trim a portion at technical resistance/overextension
2. Set rebuy targets at support/pullback levels
3. Net result: same dollar exposure, MORE shares

## Core Strategy: The Share Growth Swing

### The Problem This Solves
User holds 175 shares of NBIS at (cost basis). Stock rallies 25%. User doesn't sell because "it might go higher." Stock pulls back 15%. User still holds. Net result: 0 additional shares gained.

### The Solution
Define rules BEFORE the move happens:
- At +20-25% from swing low: trim 20-30% of position
- Wait for pullback to defined support level
- Rebuy with proceeds → now own MORE shares at a LOWER average cost

## Decision Framework

### When to Trim (Sell Signal)
Score each factor (0-2 points):
1. **Price vs 20-day MA**: >10% above = 2pts, 5-10% = 1pt
2. **RSI(14)**: >70 = 2pts, 60-70 = 1pt
3. **Volume climax**: 2x+ avg volume on up day = 2pts
4. **Distance from resistance**: Within 2% of major resistance = 2pts
5. **Rally duration**: 5+ consecutive green days = 2pts

**Action thresholds:**
- 8-10 points: Trim 30% of position
- 6-7 points: Trim 20% of position
- 4-5 points: Trim 10% of position (optional)
- 0-3 points: Hold, no action

### Trim Size Rules
- Never trim more than 30% in one transaction
- Minimum trim: 10% of position
- Keep at least 50% as "core" that never gets trimmed (long-term hold portion)
- Core portion = floor(total_shares * 0.5)

### When to Rebuy (Entry Signal)
After trimming, set rebuy targets at:
- **Level 1** (60% of trim proceeds): First support level (typically -8 to -12% from trim price)
- **Level 2** (40% of trim proceeds): Second support level (typically -15 to -20% from trim price)

Support identification priority:
1. 20-day moving average
2. 50-day moving average
3. Prior breakout level (now support)
4. Volume-weighted support zone
5. Fibonacci 38.2% / 50% retracement of recent swing

### Position Math Example
```
Starting: 175 shares @ $50 = $8,750
Trim 30%: Sell 52 shares @ $62 (+25%) = $3,224 cash, hold 123 shares
Rebuy L1: Buy 35 shares @ $55 (-11%) = $1,925
Rebuy L2: Buy 22 shares @ $51 (-18%) = $1,122
  (Remaining cash: $177 buffer)
New position: 180 shares @ lower avg cost
Net gain: +5 shares (+2.9% share growth)
```

## Catalyst Modifier (from news-catalyst-analyst skill)

Before acting on the technical score, apply a catalyst modifier from news/event analysis:

| Catalyst Rating | Modifier | Effect on Trim Threshold |
|----------------|----------|--------------------------|
| STRONG_POSITIVE | +2 | Raise threshold (harder to trim — wait for catalyst to play out) |
| POSITIVE | +1 | Slightly raise threshold |
| NEUTRAL | 0 | No change — use pure technical score |
| NEGATIVE | -1 | Lower threshold (easier to trim — exit before damage) |
| STRONG_NEGATIVE | -2 | Lower threshold significantly (trim immediately if score >= 4) |

**Adjusted action thresholds:**
```
Required score to trim = Base threshold + Catalyst modifier

Example: Score 6 normally = Trim 20%
  + STRONG_POSITIVE catalyst (AI bill passing): need score 8 → HOLD
  + NEGATIVE catalyst (Trump posts against sector): need score 5 → TRIM 20%
```

**Catalyst examples that modify signals:**
- Upcoming earnings in <5 days → POSITIVE (don't trim before potential gap up)
- Presidential visit / trade deal likely → POSITIVE for beneficiaries
- Regulatory crackdown announced → NEGATIVE for target companies
- Key executive departure → NEGATIVE
- Major product launch next week → POSITIVE (wait for reaction)
- Trump/political social media post about company → Act on direction immediately

**Critical rule:** Catalyst modifiers adjust TIMING and SIZE, never override hard stop-losses. If thesis is broken (stock -25% from cost), exit regardless of positive catalysts.

## Risk Management

### What If It Doesn't Pull Back?
- If stock continues +10% above trim price: Accept the missed upside on trimmed portion
- DO NOT chase. The core 50-70% position still captures the move.
- Set a "capitulation rebuy" at trim price + 5% to redeploy capital if trend is clearly breaking out

### What If It Drops Too Far?
- If stock drops below Level 2 by >10%: HOLD cash, do not average into breakdown
- Reassess thesis. If thesis intact: set Level 3 at major support (200-day MA or prior base)
- If thesis broken: redeploy capital elsewhere

### Stop-Loss on Core Position
- Hard stop: -25% from cost basis (thesis invalidation)
- This protects against catastrophic loss on the untrimmed core

## Output Format

For each holding analyzed, produce:

```markdown
## [TICKER] Swing Accumulator Report — [DATE]

### Current Position
- Shares: [N]
- Avg Cost: $[X]
- Current Price: $[Y]
- Unrealized P&L: [%]
- Core (untouchable): [N] shares

### Signal Score: [X/10]
- Price vs 20-MA: [score] — [detail]
- RSI(14): [score] — [value]
- Volume: [score] — [detail]
- Resistance proximity: [score] — [level]
- Rally duration: [score] — [N days]

### Recommendation
**[HOLD / TRIM X%]**

If TRIM:
- Sell [N] shares at market / limit $[X]
- Rebuy Level 1: [N] shares at $[X] (set limit order)
- Rebuy Level 2: [N] shares at $[X] (set limit order)
- Expected share gain: +[N] shares ([%] growth)

If HOLD:
- Reason: [why no action]
- Next check: [date/condition]

### Key Levels
- Resistance: $[X], $[Y]
- Support: $[X], $[Y]
- 20-MA: $[X]
- 50-MA: $[X]

### Risk
- Max downside if rebuy fails: [describe]
- Capitulation rebuy level: $[X]
```

## Execution Rules

1. Generate signals BEFORE market open (pre-market analysis)
2. Use LIMIT orders only — never market orders on the trim
3. Rebuy orders should be GTC (Good Till Cancelled) limit orders
4. Review and adjust rebuy levels weekly if not filled
5. Cancel unfilled rebuy orders if thesis changes
6. Journal every trim and rebuy in state/journal/
