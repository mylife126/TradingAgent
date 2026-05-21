---
name: financial-goal-planner
description: Set and track long-term financial goals (e.g., $1M in 2 years, $2M in 5 years). All other skills and commands serve this goal as their core purpose. Produces growth plans, milestone tracking, and adjusts strategies when off-track.
---

# Financial Goal Planner

## Purpose

This is the MASTER skill that all other skills serve. It defines the user's ultimate financial goal and ensures every action (daily trades, weekly reviews, evaluations, cleanups) contributes toward it.

## Goal Framework

### Goal Definition
```yaml
ultimate_goal:
  current_portfolio_value: $X
  target_value: $Y
  timeline: N years
  required_cagr: ((Y/X)^(1/N) - 1) * 100
  start_date: YYYY-MM-DD
  target_date: YYYY-MM-DD
```

### Growth Sources (How to Get There)

1. **Market Appreciation** (passive, ~10-15% annually for growth portfolio)
   - Hold quality stocks that compound (NVDA, META, GOOGL, APP)
   - This alone won't hit aggressive goals

2. **Swing Accumulation** (active, +5-15% additional annually)
   - Trim/rebuy cycles grow share count on winners
   - Each cycle adds 2-5% more shares without new capital
   - Over time: more shares × rising price = exponential growth

3. **Capital Rotation** (active, variable)
   - Sell dead money → buy compounders (today: MSTU→MSTR, QBTS→IONQ)
   - Tax-loss harvesting improves after-tax returns
   - Eliminate losers early, concentrate on winners

4. **New Cash Deployment** (if applicable)
   - 401(k) contributions, bonuses, savings
   - Deploy into highest-conviction positions during pullbacks

5. **Asymmetric Bets / Ambushes** (speculative, potential 3-10x)
   - EUV (photonics wave), IONQ (quantum), ONDS (defense drones)
   - Small positions ($2-5K each) with potential to become the next NBIS
   - 80% may fail, 20% may 5-10x — portfolio impact if one hits

## Milestone System

Break the goal into annual/quarterly checkpoints:

```
Year 0 (now):     $656K (baseline)
Year 0.5:         $730K (required: +11% in 6 months)
Year 1:           $820K (required: +25% from start)
Year 1.5:         $910K
Year 2:           $1,000K (TARGET if 2-year goal)
Year 3:           $1,250K
Year 5:           $2,000K (TARGET if 5-year goal)
```

### Required CAGR Calculations

| Goal | Timeline | Required CAGR | Achievable? |
|------|----------|---------------|-------------|
| $1M | 2 years | 23.4% | Aggressive but possible with swing + market |
| $1.5M | 3 years | 31.7% | Very aggressive — needs concentration + luck |
| $2M | 5 years | 25.0% | Achievable with disciplined compounding |

## How Every Command Serves This Goal

### /daily
- Check: "Are today's signals moving me TOWARD or AWAY from the goal?"
- Trim signals on winners → grow shares → accelerate compounding
- Market context → adjust aggression level based on goal progress

### /weekly
- Track: portfolio value vs. milestone schedule
- Am I on track? Ahead? Behind?
- If behind: identify what's dragging — sell it, redeploy to winners
- If ahead: stay disciplined, don't get reckless

### /cleanup
- Purpose reframed: "Which holdings are NOT contributing to the goal?"
- Dead money actively hurts because of opportunity cost
- Every $1 in a non-performer is $1 not compounding at 25%

### /plan (swing)
- Core growth engine: each cycle adds shares
- More shares on winners × time × price appreciation = goal achievement
- Priority: swing your BIGGEST winners (NBIS, NVDA) not small positions

### /evaluate
- Question becomes: "Does this stock help me reach $1M/$2M?"
- Only buy if: expected return > portfolio CAGR requirement
- Reject: anything that dilutes concentration in winners

### /check
- Intraday decisions filtered through: "Does this action help the goal?"
- Avoid impulsive moves that don't contribute

## Progress Tracking

Every /weekly adds to the goal tracker:

```markdown
## Financial Goal Progress

| Date | Portfolio Value | Target (on schedule) | Delta | Status |
|------|----------------|---------------------|-------|--------|
| 2026-05-15 | $656,244 | $656,244 (start) | $0 | ON TRACK |
| 2026-06-15 | ??? | $672,000 | ??? | ??? |
| 2026-12-15 | ??? | $730,000 | ??? | ??? |
```

Status: ON TRACK / AHEAD / BEHIND / CRITICAL

## Strategy Adjustment Rules

### If AHEAD of schedule (+5% or more above milestone):
- Stay the course, don't get aggressive
- Consider taking some risk off (lock in gains)
- Maybe widen swing trim thresholds (let winners run longer)

### If ON TRACK (within ±5% of milestone):
- Normal operations
- Execute swing cycles as planned
- Continue accumulation on dips

### If BEHIND schedule (-5% to -15%):
- Increase trim/rebuy frequency (swing more actively)
- Accelerate cleanup of dead money → redeploy to winners
- Consider slightly larger position sizes on high-conviction entries
- Do NOT chase or take excessive risk

### If CRITICAL (-15%+ below milestone):
- Reassess: is the timeline realistic given market conditions?
- Focus on capital preservation first, growth second
- Reduce speculative positions, increase quality/safety
- Consider extending timeline rather than taking desperate risks

## Key Principle

**The goal is achieved through DISCIPLINE, not heroics.** 

- 25% CAGR = ~2% per month on average
- Some months will be -5% (market corrections)
- Some months will be +10% (rallies)
- The system (swing cycles + rotation + patience) delivers over time
- One lucky NBIS-style 5x covers years of missed targets
