---
name: stock-evaluator
description: Evaluate whether a new stock is worth building a position in, and if so, design an accumulation strategy. Trigger when user asks "should I buy [TICKER]", "evaluate [TICKER]", "is [TICKER] a good stock", or wants to start building a new holding.
---

# Stock Evaluator

## Purpose

Provide a comprehensive evaluation of a stock the user is considering, then design a position-building strategy if the stock passes evaluation criteria.

## Evaluation Framework

### Phase 1: Quick Screen (Go/No-Go)

Answer these 5 questions. If 3+ are "No", the stock fails the screen.

1. **Is revenue growing?** (>10% YoY for growth, stable for value)
2. **Is institutional ownership increasing?** (smart money accumulation)
3. **Is the stock above its 200-day MA?** (long-term uptrend intact)
4. **Is the sector/theme favorable?** (tailwinds vs headwinds)
5. **Is there a clear catalyst in next 6 months?** (earnings inflection, product launch, regulatory change)

### Phase 2: Deep Analysis

If the stock passes Phase 1:

**Fundamentals:**
- Revenue growth rate and trajectory
- Earnings growth / path to profitability
- Margins (gross, operating, net) — expanding or contracting?
- Balance sheet health (debt/equity, cash position)
- Free cash flow generation
- Valuation vs peers (P/E, P/S, EV/EBITDA)

**Technicals:**
- Current trend (uptrend, downtrend, consolidation)
- Key support and resistance levels
- Volume profile (accumulation vs distribution)
- Relative strength vs S&P 500
- Chart pattern (base building, breakout, extended)

**Sentiment & Flow (Institutional Flow Framework):**
- Institutional ownership changes (13F filings — filed mid-Feb/May/Aug/Nov):
  - Strong Bullish: Ownership up >15% QoQ, institution count up >10%, quality investors adding
  - Moderate Bullish: Ownership up 5-15% QoQ, net positive
  - Neutral: <5% change
  - Moderate Bearish: Down 5-15%, more sellers than buyers
  - Strong Bearish: Down >15%, quality investors exiting → THESIS WARNING
- Insider buying/selling (openinsider.com):
  - Cluster insider buying = very bullish (they know the company best)
  - Institutional + insider buying aligned = strongest confirmation
- Short interest and days to cover (>20% short = squeeze potential OR thesis risk)
- Analyst consensus and price targets
- Options flow (unusual activity — large call sweeps = bullish institutional positioning)

**Risk Assessment:**
- Maximum historical drawdown
- Beta / volatility profile
- Concentration risk (single customer, product, geography)
- Competitive moat assessment
- Regulatory/political risk

### Phase 3: Verdict

Rate the stock:
- **STRONG BUY**: Exceptional setup, start building immediately
- **BUY**: Good stock, build position on pullbacks
- **WATCH**: Interesting but not ready yet, set alerts
- **PASS**: Doesn't meet criteria, skip

## Position Building Strategy

If verdict is STRONG BUY or BUY, design the accumulation plan:

### Entry Strategy Options

**Option A: Dollar-Cost Average (Conservative)**
- Divide total target investment into 4-6 tranches
- Buy one tranche every [1-2 weeks]
- Regardless of price (removes timing anxiety)
- Best for: Stocks in clear uptrend you don't want to miss

**Option B: Technical Entry (Moderate)**
- Wait for specific technical setups:
  - Pullback to 20-day MA
  - Test of breakout level (now support)
  - Volume dry-up in consolidation
- Buy 1/3 at first signal, 1/3 at confirmation, 1/3 on strength
- Best for: Stocks that are extended but high quality

**Option C: Staged Accumulation (Aggressive)**
- Initial pilot position: 25% of target size
- Add on first pullback to support: +25%
- Add on breakout confirmation: +25%
- Add on earnings confirmation: +25%
- Best for: Higher-conviction plays with clear technical levels

### Position Sizing

Based on portfolio context:
- Max single position: 15% of portfolio (hard cap)
- Target position: 5-10% of portfolio (normal)
- Starter position: 2-3% of portfolio (pilot)
- Stop loss: Define BEFORE entry (typically -15% to -20% from avg cost)

## Output Format

```markdown
## Stock Evaluation: [TICKER] — [DATE]

### Quick Screen
| Question | Answer | Detail |
|----------|--------|--------|
| Revenue growing? | Yes/No | [specifics] |
| Institutional accumulation? | Yes/No | [specifics] |
| Above 200-MA? | Yes/No | [price vs MA] |
| Favorable sector? | Yes/No | [sector context] |
| Near-term catalyst? | Yes/No | [what and when] |

**Screen Result: [PASS / FAIL] ([X/5])**

### Deep Analysis Summary
- **Bull Case**: [2-3 sentences]
- **Bear Case**: [2-3 sentences]
- **Base Case**: [most likely outcome]

### Verdict: [STRONG BUY / BUY / WATCH / PASS]
**Confidence**: [High / Medium / Low]
**Time Horizon**: [6mo / 1yr / 2yr+]

### Accumulation Plan (if BUY+)
- Strategy: [A / B / C]
- Target position size: [shares] ($[value], [%] of portfolio)
- Entry plan:
  - Tranche 1: [N] shares at $[X] (condition: [X])
  - Tranche 2: [N] shares at $[X] (condition: [X])
  - Tranche 3: [N] shares at $[X] (condition: [X])
- Stop loss: $[X] (-[%] from avg entry)
- First target: $[X] (+[%])
- Timeline: [weeks/months to full position]

### Key Levels to Watch
- Entry zone: $[X] - $[Y]
- Stop loss: $[X]
- First resistance: $[X]
- Breakout target: $[X]

### Risks
1. [Primary risk and mitigation]
2. [Secondary risk]
3. [What would invalidate the thesis]
```
