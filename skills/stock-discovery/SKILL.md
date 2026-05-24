---
name: stock-discovery
description: Discover, analyze, rank, and track high-potential new stock candidates. Combines fundamental analysis, technical timing, catalyst reasoning, trend/wave detection, and external opinions. Produces a ranked watchlist with entry plans. Trigger when user asks "find new stocks", "what should I look at", "rank these stocks", "compare X vs Y", or provides a list of candidates to evaluate.
---

# Stock Discovery & Ranking

## Purpose

Systematically discover, analyze, compare, and TRACK potential new stock investments. Unlike /evaluate (single stock deep-dive), this skill handles:
1. Multi-stock comparison and ranking
2. Wave/theme identification (like photonics/optical → EUV)
3. Tracking past analyses for reference and evolution
4. Integrating external opinions (YouTubers, analysts, forums)

## Information Sources (Priority Order)

### Tier 1: Quantitative (always use)
- **yfinance**: Price, MAs, RSI, volume, fundamentals (revenue, PE, growth)
- **Web search**: Recent earnings, analyst targets, news
- **skills/stock-evaluator/SKILL.md**: 5-question screen + deep analysis framework
- **skills/news-catalyst-analyst/SKILL.md**: Second-order reasoning, geopolitical chains
- **skills/position-sizer/SKILL.md**: Risk-based sizing for entry plans
- **skills/exposure-coach/SKILL.md**: Market posture check (should we be buying at all?)

### Tier 2: Thematic Reasoning (use when relevant)
- **state/theses/**: User's existing investment theses (wave theories, trend reasoning)
- **Theme detection**: Identify which "wave" a stock belongs to:
  - Wave 1 (past): GPU/compute → NVDA dominated
  - Wave 2 (current): Memory/HBM → SNDK, Micron
  - Wave 3 (emerging): Optical/photonics → EUV thesis
  - Wave 4 (next?): Quantum → IONQ ambush
  - Wave 5 (speculative): Robotics, fusion, space
- **Historical precedent**: "Stock X is in the position Stock Y was 2 years ago"

### Tier 3: External Opinions (when available)
- **data/others_opinions/**: Crawled YouTube transcripts, analyst notes, forum sentiment
  - Format expected: `data/others_opinions/TICKER_source_YYYY-MM-DD.md`
  - Sources: YouTube analysts, Seeking Alpha, Twitter/X threads, Reddit DD
- If folder doesn't exist or is empty: proceed without external opinions, note "no external data available"
- When available: weight external opinions as CONFIRMATION or CONTRADICTION of quantitative analysis

## Analysis Framework

### Step 1: Candidate Gathering
Sources for new candidates:
- User provides a list ("compare RKLB, IONQ, POET")
- Theme-based discovery ("what's the next photonics play?")
- Sector screening ("best AI infrastructure stocks under $50")
- Previous analyses in state/discovery/ tracker

### Step 2: Quick Screen (per stock)
Apply the 5-question screen from stock-evaluator:
1. Revenue growing? (>10% YoY)
2. Institutional accumulation?
3. Above 200-MA?
4. Favorable sector/theme?
5. Near-term catalyst?

**Score: X/5. If <3, eliminate early.**

### Step 2b: Theme Lifecycle Assessment

Before scoring individual stocks, assess the THEME's lifecycle stage:

| Stage | Characteristics | Action |
|-------|----------------|--------|
| **Emerging** | Few ETFs, low analyst coverage, narrative building, early adopters only | AGGRESSIVE accumulate — best risk/reward |
| **Accelerating** | Growing coverage, momentum building, institutions entering | ACCUMULATE — ride the wave |
| **Trending** | Broad coverage, many ETFs launched, mainstream narrative | MODERATE — still OK but be more selective |
| **Mature** | Peak ETF count, everyone "knows the story", full analyst coverage | CAUTIOUS — only buy dips, focus on leaders |
| **Exhausting** | Declining momentum despite narrative, smart money exiting, retail heavy | REDUCE — shift to maintenance, tighten swings |

**ETF Proliferation Rule:** Many ETFs for a theme = retail crowding = late stage.
**Quality of Holders Rule:** If hedge funds shifting out but retail piling in = distribution in progress.

Your current themes:
- AI Infrastructure (GPU/compute): TRENDING → mature leaders established. Focus on LEADERS only (NVDA, NBIS).
- AI Optical/Photonics: EMERGING-ACCELERATING → still early! Aggressive on EUV/COHR.
- Quantum Computing: EMERGING → very early. IONQ ambush is correct approach.
- AI Networking: TRENDING → ANET is established leader.
- AI Advertising: ACCELERATING → APP growing fast, theme gaining momentum.

### Step 3: Deep Scoring (per stock that passes screen)

Score each dimension 1-10:

| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Growth | 25% | Revenue growth rate, acceleration, TAM |
| Profitability Path | 15% | Current margins or clear path to profit |
| Competitive Moat | 15% | Unique tech, network effects, switching costs |
| Catalyst Strength | 15% | Upcoming events that could move the stock |
| Technical Entry | 10% | Is NOW a good time to buy? RSI, MA position |
| Valuation | 10% | P/S, P/E vs growth rate (PEG), vs peers |
| Theme Alignment | 10% | Does it fit a wave thesis? Second-order reasoning? |

**Total weighted score: X/10**

### Step 4: Ranking & Comparison

Rank all candidates by weighted score. Present as:

```markdown
## Stock Discovery Ranking — [DATE]

| Rank | Ticker | Score | Growth | Moat | Catalyst | Entry | Verdict |
|------|--------|-------|--------|------|----------|-------|---------|
| 1 | XXXX | 8.2 | 9 | 7 | 9 | 8 | STRONG BUY |
| 2 | YYYY | 7.1 | 8 | 6 | 7 | 7 | BUY |
| 3 | ZZZZ | 5.4 | 6 | 5 | 5 | 5 | WATCH |
```

### Step 5: Entry Plan (for top-ranked)

For stocks scoring 7+:
- Position size (from position-sizer skill)
- Entry tranches with specific prices
- Stop loss level
- How it contributes to the $1M financial goal
- Which "wave" or theme it belongs to

## Tracking System

### Discovery Tracker: `state/discovery/watchlist.yaml`

```yaml
last_updated: "YYYY-MM-DD"

ranked_candidates:
  - ticker: XXXX
    score: 8.2
    verdict: STRONG_BUY
    analysis_date: "YYYY-MM-DD"
    theme: "quantum_computing"
    entry_plan:
      status: BUILDING / WATCHING / PASSED
      target_price: $XX
      shares_target: XX
    notes: "Key reasoning summary"
    
  - ticker: YYYY
    score: 7.1
    ...

watch_list:
  - ticker: ZZZZ
    reason: "Interesting but not ready"
    revisit_date: "YYYY-MM-DD"
    condition: "Buy if drops to $XX or if [catalyst] happens"

passed:
  - ticker: WWWW
    reason: "Revenue declining, no moat"
    analysis_date: "YYYY-MM-DD"
    
themes_tracked:
  - name: "AI Infrastructure"
    stocks: [NBIS, IREN, ANET]
    wave_position: "Wave 1 maturing"
  - name: "Optical/Photonics"
    stocks: [EUV]
    wave_position: "Wave 3 emerging"
  - name: "Quantum Computing"
    stocks: [IONQ]
    wave_position: "Wave 4 early"
```

### Analysis Archive: `state/discovery/analysis_TICKER_YYYY-MM-DD.md`

Each analysis is saved for future reference. When re-analyzing a stock:
1. Load previous analysis
2. Compare: what changed? Revenue better/worse? New catalysts? Price moved?
3. Update score and ranking
4. Note evolution in the tracker

## Integration with Financial Goal

Every discovery recommendation must answer:
- "If I put $X into this stock, what's the realistic return in 1-2 years?"
- "Does this expected return beat my required 23.4% CAGR?"
- "Does this take capital away from higher-conviction plays (NBIS, META, APP)?"
- "What's the asymmetric upside? Could this 5-10x?" (for ambush positions)

## External Opinions Integration (Future)

When `data/others_opinions/` contains files:
- Read all opinion files for the ticker being analyzed
- Extract: bull case, bear case, price targets, key arguments
- Score consensus: BULLISH / MIXED / BEARISH
- Note disagreements between your analysis and external opinions
- Flag if a popular YouTuber/analyst has a STRONG contrary view

**For now**: Leave this as a placeholder. When user creates the crawl function, update this section with specific file format expectations and parsing logic.

## Output Format

```markdown
## Stock Discovery Report — [DATE]

### Theme: [if applicable]
[Brief thesis on the wave/trend being exploited]

### Rankings
| Rank | Ticker | Score | Key Strength | Key Risk | Verdict |
|------|--------|-------|-------------|----------|---------|

### #1: [TICKER] — Detailed Analysis
[Full breakdown: fundamentals, technicals, catalysts, thesis]
[Entry plan if BUY+]

### #2: [TICKER] — Detailed Analysis
...

### External Opinions Summary (if available)
[What others are saying — confirms or contradicts?]

### Previous Analysis Comparison (if exists)
[What changed since last time we looked at this stock?]

### Action Items
[Specific orders to place, or conditions to watch for]
```

## When to Run

- User asks to compare/rank multiple stocks
- User identifies a new theme and wants candidates
- Monthly: re-rank the discovery watchlist (have scores changed?)
- When external opinion data arrives in data/others_opinions/
