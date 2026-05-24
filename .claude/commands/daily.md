Run the daily market scan, swing signals, position build alerts, CC opportunities, and independent market reasoning.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

## Core Philosophy
This command is NOT just a passive scan. It must:
1. Proactively REASON about the market using all available data
2. Connect dots between macro events, sector trends, and individual stock movements
3. Apply second-order thinking (if X happens → who benefits → what should we do)
4. Reference the user's investment theses (photonics wave, quantum, AI infra layers) and validate/invalidate them
5. Suggest NEW opportunities discovered through reasoning, not just check existing positions

## Data Sources (MUST use at least 3 external sources per /daily run)
- stockanalysis.com/news/ — daily market headlines, earnings
- Web search — breaking news, Trump/Fed/geopolitics
- yfinance (scripts) — price data, technicals
- User's YouTube references: @RhinoFinance (犀牛财经), @财经观察站 (if data/others_opinions/ has transcripts)
- state/theses/ — validate wave theories against today's market

## Steps

### Phase 1: Read ALL State Files (保留原有逻辑)
0. ALWAYS read state/progress/financial_goal.yaml FIRST — understand the target ($1M). Frame daily with goal status.
1. ALWAYS read state/holdings/current.yaml — all positions with exact shares, avg cost, accounts
2. ALWAYS read state/holdings/goals.yaml — accumulation targets and strategy for each holding
3. ALWAYS read state/progress/tracker.yaml to check:
   - Open swing cycles and their rebuy targets (did any fill overnight?)
   - Pending orders (still active or expired?)
   - Position builds in progress
   - Cash flow state
4. ALWAYS check state/theses/ for any thesis files. Read them to understand WHY the user holds each position. If today's news/price action invalidates a thesis, flag it prominently.
5. Check state/actions/ for the most recent action tracker file. If there are SUGGESTED actions still pending, remind the user.
6. Read state/cost_basis/adjusted_costs.yaml — CC/option income tracking

### Phase 2: Read ALL Skills (显式调用，保留原有)
7. Read skills/market-scanner/SKILL.md for the market scanning framework
8. Read skills/swing-accumulator/SKILL.md for scoring interpretation and trim/rebuy logic
9. Read skills/news-catalyst-analyst/SKILL.md for news/catalyst reasoning framework
10. Read skills/exposure-coach/SKILL.md for market posture (NEW_ENTRY_ALLOWED / REDUCE_ONLY / CASH_PRIORITY)
11. Read skills/position-sizer/SKILL.md for sizing any new recommendations
12. Read skills/covered-call-strategy/SKILL.md for CC/CSP rules
13. Read skills/technical-analyst/SKILL.md for market structure (HH/HL/LL/LH trend flip theory), support/resistance, volume analysis. Apply market structure assessment to key holdings — especially when deciding if a pullback is "buy the dip" (HL in uptrend) vs "dead cat bounce" (LH in downtrend).

### Phase 3: External Research & Independent Reasoning (新增)
13. Use web search to check today's market-moving news: major political events, geopolitical developments, sector catalysts, earnings reports
14. Apply INDEPENDENT REASONING — don't just report news, ANALYZE it:
    - "Oil prices dropping → inflation easing → Fed less likely to hike → growth stocks benefit"
    - "NVIDIA said 'supply constrained' → optical networking demand confirmed → EUV thesis validated"
15. Check if any WAVE THESIS is being validated or invalidated:
    - Wave 1 (GPU): NVDA news
    - Wave 2 (Memory): HBM/SNDK news
    - Wave 3 (Optical): COHR/GLW/EUV news
    - Wave 4 (Quantum): IONQ news
    - Networking: ANET news
16. Apply second-order logical reasoning per the catalyst skill (e.g., "presidential visit → trade deal → who benefits?")

### Phase 3b: Distribution Day & Breadth Check (from exposure-coach)
14b. Check SPY and QQQ: did either close down >0.2% on higher volume yesterday? If yes = distribution day.
14c. Estimate current distribution day count (d5/d15/d25) based on recent market action.
14d. Assess breadth: SPY vs IWM divergence? Advance/decline?
14e. Report: "Market Health: [NORMAL/CAUTION/HIGH/SEVERE]" with implication for swing buys.
14f. If HIGH or SEVERE: explicitly state "⚠️ PAUSE swing buys — distribution day count elevated"

### Phase 4: Holdings Scan (保留原有)
17. Run `python3 scripts/fetch_price_data.py` on the individual stock tickers from holdings (skip index funds like QQQ, VTSAX, FSKAX, SOXX unless user asks)
18. For each holding, calculate swing score AND catalyst modifier. Final action = technical signal adjusted by catalyst context
19. Present a consolidated daily action plan with specific prices, share counts, and recommendations (HOLD / TRIM X% / REBUY ZONE)
20. If any score is >= 6 (after catalyst adjustment), generate specific limit order instructions: ticker, buy/sell, share count, limit price, order type (GTC)
21. If any catalyst is STRONG_POSITIVE or STRONG_NEGATIVE, highlight it prominently

### Phase 5: Swing Opportunities (新增强化)
22. For holdings with score 4+ or RSI >65: suggest specific swing trim actions with exact shares and prices
23. For holdings that pulled back (RSI <40): suggest accumulation entry points
24. Reference swing-accumulator skill framework for scoring and thresholds

### Phase 6: Position Build Scan (保留原有 + 强化)
25. ALWAYS read state/actions/position_build_plan_2026-05-18.md (or most recent position build plan)
26. Run `python3 scripts/fetch_price_data.py` on ALL position build tickers (GOOGL, COHR, RKLB, MSTR, ANET, LLY, and any others)
27. Check each ticker against its BUY ALERT condition from the build plan
28. Present "Position Build Status" section:
    - Show each build target with current price vs entry price and % gap
    - If ANY alert fires (within 5%): highlight with ⚠️
    - If ANY order is stale (>15% away): flag for adjustment
29. For watchlist stocks WITHOUT GTC yet: analyze if NOW is a good time to place orders
30. For existing GTC: are they still technically valid? Has MA shifted?

### Phase 7: Covered Call & CSP Signal Check (保留原有)
31. For each holding with 100+ shares (NBIS, GOOGL, META, NVDA, QQQ, KO), check:
    a. RSI > 60? (stock rallied, premium is worth selling)
    b. Not within 7 days of earnings?
    c. Score ≤ 5? (if 6+ → recommend swing trim instead)
    d. No active CC already on this ticker?
32. If ANY stock passes all CC conditions, add brief alert:
    ```
    💰 CC OPPORTUNITY: [TICKER] — RSI [X], suggest sell $[strike] call, [expiry], ~$[premium]
    ```
33. Also check CSP opportunities for position build targets above GTC buy price:
    ```
    💰 CSP OPPORTUNITY: [TICKER] — sell $[strike] put (below your GTC), ~$[premium]
    ```
34. Philosophy: CONSERVATIVE — far OTM, low assignment risk, 白赚premium为主.

### Phase 8: Independent Discovery & New Ideas (新增)
35. Based on today's news and reasoning, suggest 1-2 NEW ideas or warnings:
    - Connect to user's theses
    - Identify emerging opportunities or threats
    - "PCE data next week — if hot, expect broad selloff. Your GTC orders may all fill."
    - "Your photonics wave thesis is being validated: COHR/GLW hitting highs on NVIDIA demand."

### Phase 9: Action Plan & Tracking (保留原有)
36. Present concise daily action plan (top 5-7 priorities)
37. ALWAYS write suggested actions to `state/actions/daily_YYYY-MM-DD.md`
38. Update state/progress/tracker.yaml if any pending orders filled or swing cycle status changed

The output MUST use real position data — never give generic advice. Keep concise but include ALL sections.

## Output Structure (必须包含所有section)

```
═══ DAILY SCAN — [DATE] ═══

🎯 Goal: $[X] / $1M | [status]

🧠 MARKET REASONING (独立思考 — 2-3段原创分析)
  [连接macro→sector→你的stocks]
  [验证/invalidate wave theses]
  [二阶推理]

📊 HOLDINGS SIGNAL TABLE
  [所有stock + swing score + signal]

🔄 SWING OPPORTUNITIES
  [具体的trim/entry建议 with prices and share counts]

🏗️ POSITION BUILD STATUS
  [所有GTC orders with gaps + adjustment recommendations]

💰 CC/CSP SIGNALS
  [brief alerts for eligible stocks]

💡 NEW IDEAS & WARNINGS
  [1-2个基于reasoning的主动建议]

⚡ ACTION PLAN (Top 5-7)
  [prioritized list with specific instructions]
```

## Tracking User Confirmations
When the user says they executed an action:
1. Read the most recent daily action tracker from state/actions/
2. Update the matching action's Status to EXECUTED or SKIPPED
3. Update state/progress/tracker.yaml accordingly (shares, cash flow, cycle status)
4. Save both files
