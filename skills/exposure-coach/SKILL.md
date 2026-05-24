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

## Distribution Day Monitor (IBD Method — Daily Go/No-Go Gate)

A Distribution Day = index closes down ≥0.2% on volume higher than previous day.
Track count in rolling windows: d5 (5 sessions), d15 (15 sessions), d25 (25 sessions).

| Risk Level | Condition | Action on Swing Buys |
|-----------|-----------|---------------------|
| NORMAL | d25 ≤ 2 | Full-size buys OK |
| CAUTION | d25 ≥ 3 | Reduce buy size by 25% |
| HIGH | d25 ≥ 5 OR d15 ≥ 3 OR d5 ≥ 2 | **PAUSE all buys.** Tighten stops. |
| SEVERE | d25 ≥ 6 OR (index below 50MA AND d25 ≥ 5) | **Actively reduce exposure.** Sell weakest. |

Rules:
- A DD "heals" when index rises 5% from that day's close, or 25 sessions pass
- QQQ at HIGH = overall HIGH (it leads growth stocks)
- 2 distribution days within 5 sessions = immediately HIGH → stop buying
- This prevents accumulating into a declining market (user's known weakness)

## Market Top Detection (6-Component Composite)

Beyond daily distribution days, assess weekly for broader top signals:

| Component | Weight | What to Check |
|-----------|--------|---------------|
| Distribution Day Count | 25% | d25 count on SPY + QQQ |
| Leading Stock Health | 20% | Are high-growth leaders (NBIS, APP, IONQ) breaking down while indices hold? |
| Defensive Rotation | 15% | Is money flowing into XLU/XLP/XLV away from XLK/XLY? |
| Breadth Divergence | 15% | Are fewer stocks making new highs while index makes new highs? |
| Index Technical | 15% | Index vs 50MA/200MA, RSI, volume |
| Sentiment/Speculation | 10% | VIX complacency, IPO frenzy, margin levels |

Score 0-100 → Risk zones:
- 0-20: Normal (full aggression)
- 21-40: Tighten (reduce new entries to 80%)
- 41-60: Caution (profit-take weak positions, 60% sizing)
- 61-80: Defensive (aggressive trimming, 40% sizing)
- 81-100: Maximum defense (hedging, cash priority)

## When to Run

- At the start of every /daily (distribution day check)
- Before every /evaluate or /plan decision
- At the start of /weekly review (full top detection scan)
