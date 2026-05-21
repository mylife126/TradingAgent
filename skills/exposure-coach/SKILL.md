---
name: exposure-coach
description: Determines how much capital to commit to equities RIGHT NOW based on market regime, breadth, and risk signals. Answers "should I be aggressive, normal, or defensive?" before any individual stock analysis. Produces an exposure ceiling (0-100%) and action mode.
---

# Exposure Coach

## Purpose

Before asking "which stock should I buy?", answer: "Should I be BUYING AT ALL right now?"
This skill synthesizes market signals into a single posture decision.

## Action Modes

| Mode | Meaning | Trading Implications |
|------|---------|---------------------|
| NEW_ENTRY_ALLOWED | Healthy market, proceed with buys | Execute accumulation plans, place GTC orders |
| REDUCE_ONLY | Deteriorating conditions | No new entries. Trim on strength. Tighten stops. |
| CASH_PRIORITY | Danger zone | Raise cash aggressively. Cancel GTC buy orders. Preserve capital. |

## Exposure Ceiling (Quick Assessment)

Based on regime + breadth indicators:

| Market Condition | Exposure Ceiling | Cash Floor |
|-----------------|-----------------|------------|
| Strong uptrend, broad participation | 90-100% | 0-10% |
| Uptrend, narrowing breadth | 75-90% | 10-25% |
| Choppy / transitional | 60-75% | 25-40% |
| Correction, distribution | 40-60% | 40-60% |
| Downtrend / bear | 25-40% | 60-75% |

## Input Signals (Quick Version)

Score each 0-2 points:

1. **SPY vs 20/50 MA**: Above both = 2, mixed = 1, below both = 0
2. **VIX level**: <18 = 2, 18-25 = 1, >25 = 0
3. **Breadth**: >60% stocks above 200MA = 2, 40-60% = 1, <40% = 0
4. **Yield curve / credit**: Stable = 2, tightening = 1, inverting/stress = 0
5. **Sector rotation**: Offensive sectors leading = 2, mixed = 1, defensive leading = 0

**Total 0-10:**
- 8-10: NEW_ENTRY_ALLOWED (go aggressive)
- 5-7: Normal operations (execute plans as designed)
- 3-4: REDUCE_ONLY (tighten, no new entries)
- 0-2: CASH_PRIORITY (raise cash, protect capital)

## Integration with Financial Goal

- If BEHIND on goal milestones + NEW_ENTRY_ALLOWED → be more aggressive on entries
- If AHEAD on goal + REDUCE_ONLY → take profits, lock in gains, stay ahead
- If BEHIND + CASH_PRIORITY → DO NOT try to catch up by being reckless. Preservation first.

## When to Run

- At the start of every /daily
- Before every /evaluate or /plan decision
- At the start of /weekly review
