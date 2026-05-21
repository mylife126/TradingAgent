---
name: technical-analyst
description: Analyze candlestick charts (weekly or daily) to identify trend, support/resistance, and probabilistic scenarios. Requires chart image input. Trigger when user provides a chart screenshot or asks for technical analysis on a specific ticker.
---

# Technical Analyst

## Purpose

Provide objective, chart-based technical analysis using candlestick patterns, moving averages, volume, and support/resistance levels. All analysis is probabilistic — no predictions, only scenarios with probabilities.

## Prerequisites

- Chart image (screenshot of daily or weekly candlestick chart)
- Preferred: Chart includes volume bars, 20/50/200 MA overlays
- No API required — analysis is visual

## Analysis Framework

### Step 1: Trend Identification
- **Primary trend** (200 MA direction): Up / Down / Flat
- **Intermediate trend** (50 MA direction): Up / Down / Flat
- **Short-term trend** (20 MA direction): Up / Down / Flat
- **MA alignment**: Bullish stack (20>50>200) / Bearish stack / Mixed

### Step 2: Support & Resistance
Identify levels by priority:
1. Horizontal S/R from price history (multiple touches)
2. Moving averages acting as dynamic S/R
3. Trendlines (ascending/descending)
4. Round numbers (psychological levels)
5. Gap fills
6. Fibonacci retracements (38.2%, 50%, 61.8% of major swings)

### Step 3: Volume Analysis
- Is volume confirming price moves? (up on high vol = bullish)
- Distribution days (down on high vol) — count in last 5 weeks
- Volume dry-up (often precedes breakout)
- Climax volume (exhaustion signal)

### Step 4: Pattern Recognition
Look for:
- **Bases**: Cup-with-handle, flat base, double bottom, ascending base
- **Breakouts**: Volume confirmation, follow-through
- **Reversals**: Head & shoulders, double top, bearish engulfing
- **Continuation**: Bull flags, pennants, tight closes

### Step 5: Scenario Development

Develop 2-4 scenarios, probabilities must sum to 100%:

| Scenario | Typical Probability | Conditions |
|----------|-------------------|------------|
| Bull case | 20-40% | What needs to happen for upside |
| Base case | 40-60% | Most likely path |
| Bear case | 20-40% | What triggers downside |
| Wild card | 5-15% | Low probability but high impact |

### Step 6: Actionable Levels

For each scenario, define:
- **Entry/add level**: Where to buy if scenario plays out
- **Target**: Price objective
- **Invalidation**: Where the scenario is proven wrong

## Integration with Swing Accumulator

When analyzing stocks the user already holds, additionally assess:
- Is current price in a trim zone? (overextended from MAs)
- Is current price in a rebuy zone? (at support)
- What's the next likely swing (for accumulator timing)?

## Output Format

```markdown
## Technical Analysis: [TICKER] — [DATE]

### Trend Summary
- Primary (200 MA): [UP/DOWN/FLAT]
- Intermediate (50 MA): [UP/DOWN/FLAT]
- Short-term (20 MA): [UP/DOWN/FLAT]
- MA Alignment: [Bullish/Bearish/Mixed]

### Key Levels
| Level | Price | Type | Strength |
|-------|-------|------|----------|
| R3    | $XX   | [type] | [strong/moderate/weak] |
| R2    | $XX   | [type] | [strong/moderate/weak] |
| R1    | $XX   | [type] | [strong/moderate/weak] |
| Current | $XX | — | — |
| S1    | $XX   | [type] | [strong/moderate/weak] |
| S2    | $XX   | [type] | [strong/moderate/weak] |
| S3    | $XX   | [type] | [strong/moderate/weak] |

### Volume Assessment
- [Volume observation and implication]

### Pattern
- [Current pattern if any, stage of formation]

### Scenarios
| # | Name | Probability | Target | Invalidation |
|---|------|-------------|--------|--------------|
| 1 | [Bull] | XX% | $XX | $XX |
| 2 | [Base] | XX% | $XX | $XX |
| 3 | [Bear] | XX% | $XX | $XX |

### Swing Accumulator Context
- Trim zone: [Yes/No — if yes, at what level]
- Rebuy zone: [Yes/No — if yes, what level]
- Next expected swing: [description]

### Bottom Line
[1-2 sentence summary of the technical picture and recommended action]
```

## Quality Standards

- Never use directional language without probability ("it WILL go up")
- Always present both bull and bear cases
- Specific price levels, not vague ranges
- Acknowledge when the picture is unclear — "no clear edge" is a valid conclusion
- Chart patterns must be confirmed by volume to be high-conviction
