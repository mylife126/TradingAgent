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

### Step 4: Market Structure (Trend Flip Theory)

Identify the current swing structure (HH/HL/LL/LH):

**Uptrend structure:**
```
HH → HL → HH → HL (Higher Highs + Higher Lows = healthy uptrend)
  ↑ Each high is higher than previous
  ↑ Each low is higher than previous
```

**Break of Structure (BOS) — first warning:**
```
In uptrend: ... → HH → HL → FAILS to make new HH → makes LL (Lower Low!)
  = Structure broken. Uptrend is OVER. But not yet confirmed downtrend.
```

**Confirmed Downtrend:**
```
... → LL → LH → LL → LH (Lower Lows + Lower Highs)
  ↓ Each rally fails at lower level (Lower High = sellers in control)
```

**Trend Flip (downtrend → uptrend) — CRITICAL CONCEPT:**
```
In downtrend: ... → LL → LH → LL → LH → then:
  
  IF next move FAILS to break above previous LH = still downtrend (FAKE PUMP!)
  IF next move BREAKS ABOVE previous HIGH = TREND FLIP CONFIRMED! ✅
  
  Key rule: A rally that doesn't make a HIGHER HIGH is NOT a trend flip.
  It's just a Lower High in a downtrend = bear flag = fade it.
```

**Application to swing accumulator:**
- Buy at HL (Higher Low) in uptrend = buying the dip in strength
- Don't buy at LH (Lower High) in downtrend = catching a falling knife
- Wait for HH confirmation before entering after a correction
- Trim at HH when structure shows exhaustion (RSI divergence + failing volume)

**How to identify HH/HL/LL/LH programmatically:**
- Use swing highs/lows on daily chart (pivot points)
- Compare each new swing high to previous: higher = HH, lower = LH
- Compare each new swing low to previous: higher = HL, lower = LL

### Step 4b: VCP Pattern (Volatility Contraction Pattern — Minervini)

Mark Minervini's key pattern for low-risk entries in uptrending stocks:

**What is VCP:**
A stock in a Stage 2 uptrend forms progressively TIGHTER contractions as supply dries up.
Each pullback is shallower than the last → sellers exhausted → breakout imminent.

```
Example: Stock at $100
  T1 (first contraction): pulls back to $85 (-15%)
  T2 (second contraction): pulls back to $92 (-8%)  ← tighter!
  T3 (third contraction): pulls back to $96 (-4%)   ← even tighter!
  PIVOT: breakout above $100 on volume → BUY signal
```

**VCP Scoring:**
- Textbook (90+): 3+ contractions, each 30%+ tighter, volume dry-up in final squeeze
- Strong (80-89): 2-3 contractions, clear tightening
- Good (70-79): 2 contractions, moderate tightening
- Developing (60-69): Pattern forming but not complete → watchlist
- Weak (<60): Not a valid VCP

**VCP Entry Rules:**
- Buy at PIVOT (breakout above the contraction high)
- Breakout must have 1.5x+ average volume (confirmation)
- Stop: 1% below the lowest point of the final contraction
- Don't chase: if stock already 2%+ above pivot, WAIT for pullback
- Risk per trade: max 1% of portfolio (from position-sizer skill)

**Application to Swing Accumulation:**
Instead of randomly buying dips, wait for your conviction stock to form a VCP:
- NBIS at $215: if it forms a tight base $200-215 with declining volume → VCP forming
- Breakout above $215 on volume → ADD shares (offensive entry)
- This complements defensive entries (buying support/MAs)

### Step 4c: Pattern Recognition (Classic)
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
