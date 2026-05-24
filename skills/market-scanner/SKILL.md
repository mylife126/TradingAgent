---
name: market-scanner
description: Quick daily market context scan covering major indices, sector rotation, market regime, and news that could affect holdings. Run this first before checking individual positions. Trigger on "market scan", "daily check", "what's happening today", or at start of daily workflow.
---

# Market Scanner

## Purpose

Provide a 2-minute market context briefing before diving into individual positions. Answers: "Is today a day to be aggressive, defensive, or do nothing?"

## Daily Scan Components

### 1. Index Health (30 seconds)
Check major indices:
- S&P 500 (SPY): Price, % change, vs 20/50/200 MA
- Nasdaq 100 (QQQ): Price, % change, vs 20/50/200 MA
- Russell 2000 (IWM): Price, % change (breadth indicator)
- VIX: Level and direction (fear gauge)

### 2. Market Regime Classification
Based on index health, classify current regime:

| Regime | Condition | Implication |
|--------|-----------|-------------|
| **Strong Uptrend** | All indices above 20/50 MA, VIX <18 | Be aggressive on entries, tight trims |
| **Uptrend** | Indices above 50 MA, some above 20 MA | Normal operations |
| **Choppy** | Mixed signals, indices between 20 and 50 MA | Reduce position sizes, wider stops |
| **Correction** | Indices below 50 MA but above 200 MA | Defensive, focus on trimming |
| **Downtrend** | Indices below 200 MA, VIX >25 | Cash preservation, no new entries |

### 3. Sector Rotation (30 seconds)
- Which sectors leading today/this week?
- Which sectors lagging?
- Any rotation relevant to user's holdings?

### 4. Key News/Events
- Earnings reports affecting holdings
- Fed/economic data releases
- Sector-specific news
- Geopolitical events

### 5. Holdings Heat Check
Quick scan of user's top positions:
- Any gap up/down >3% pre-market?
- Any at swing accumulator signal levels?
- Any earnings this week?

## Output Format

```markdown
## Market Scan — [DATE] [Pre-Market/After Hours]

### Regime: [STRONG UPTREND / UPTREND / CHOPPY / CORRECTION / DOWNTREND]

### Indices
| Index | Price | Change | vs 20MA | vs 50MA | vs 200MA |
|-------|-------|--------|---------|---------|----------|
| SPY   | $XXX  | +X.X%  | Above   | Above   | Above    |
| QQQ   | $XXX  | +X.X%  | Above   | Above   | Above    |
| IWM   | $XXX  | +X.X%  | Below   | Above   | Above    |
| VIX   | XX.X  | +X.X   | —       | —       | —        |

### Sector Leaders/Laggards
- Leading: [Sector1] (+X%), [Sector2] (+X%)
- Lagging: [Sector1] (-X%), [Sector2] (-X%)

### News & Events
- [Relevant item 1]
- [Relevant item 2]

### Holdings Alert
- [TICKER]: [alert if any — gap, earnings, signal level]

### Today's Bias
**[AGGRESSIVE / NORMAL / CAUTIOUS / DEFENSIVE]**
- [One sentence on what this means for today's operations]
```

## Breadth & Uptrend Health (Uptrend Analyzer)

Beyond index prices, assess market BREADTH (participation):

| Score Range | Label | Meaning | Exposure Multiplier |
|-------------|-------|---------|-------------------|
| 80-100 | Strong Bull | Broad participation, most sectors up | 100% — be aggressive |
| 60-79 | Bull | Healthy, minor divergences | 75-100% — normal ops |
| 40-59 | Neutral | Mixed signals, narrowing | 50-75% — reduce size |
| 20-39 | Cautious | Few sectors advancing, defensive rotation | 25-50% — defensive |
| 0-19 | Bear | Broad decline | 0-25% — cash priority |

Key breadth signals:
- Advance/Decline ratio (more stocks going up than down?)
- % of stocks above 200-MA (healthy market: >60%)
- Sector spread (if best sector +15% and worst -10% = narrow/unhealthy)
- Late cycle warning: commodities outperforming both cyclical AND defensive

How to check (simplified): compare SPY vs IWM (small cap). If SPY up but IWM flat/down = narrow rally = less healthy.

## Data Sources & Scripts

- **`python3 scripts/fetch_price_data.py TICKER`** — individual stock: price, RSI, MAs, swing score
- **`python3 scripts/distribution_days.py`** — market-level: distribution day counts, risk level, exposure gate
- Yahoo Finance (yfinance) for price/MA data
- Market news via web search
- Pre-market data for gap detection
- Economic calendar for event awareness
