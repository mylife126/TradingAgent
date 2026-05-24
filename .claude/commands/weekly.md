Run the comprehensive weekly portfolio review with forward-looking analysis.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

## Core Philosophy
The weekly review is the STRATEGIC command. It must:
1. Look BACKWARD: what happened this week, what worked, what didn't
2. Look FORWARD: what's coming next week, how to position
3. REASON independently: connect macro trends to portfolio decisions
4. VALIDATE theses: are wave theories (photonics, quantum, AI layers) still correct?
5. DISCOVER: proactively find new information that might change strategy

## Data Sources (Use ALL available — at least 5 external checks)
- stockanalysis.com/news/ — week summary + next week events
- Web search: "[upcoming week] stock market events economic data"
- Web search: sector-specific news for AI/optical/quantum if relevant
- data/others_opinions/ — if YouTube transcripts available, reference their views
- User's YouTube refs: @RhinoFinance, @FinanceObserver

## Steps

### Phase 1: Read ALL State Files
0. ALWAYS read state/progress/financial_goal.yaml FIRST. Calculate current portfolio value vs. milestone schedule. Report: ON TRACK / AHEAD / BEHIND / CRITICAL.
1. Check data/fidelity/ and data/robinhood/ for new CSV files
2. If CSVs found: run `python3 scripts/import_holdings.py` to parse and update state
3. If no CSVs found: use existing state/holdings/current.yaml
4. ALWAYS read state/holdings/current.yaml and state/holdings/goals.yaml for full position context
5. ALWAYS read all files in state/theses/ to understand investment theses. Flag any being validated/invalidated.
6. ALWAYS read state/progress/tracker.yaml for the full progress picture:
   - Accumulation goal progress
   - Open swing cycles
   - Position builds
   - Pending orders
   - Cash flow state
7. Read all files in state/actions/ from the past week to review what was suggested vs. executed vs. skipped
8. Read state/cost_basis/adjusted_costs.yaml — option income tracking

### Phase 2: Read ALL Skills
9. Read skills/market-scanner/SKILL.md for market regime framework
10. Read skills/swing-accumulator/SKILL.md for scoring and trim/rebuy logic
11. Read skills/news-catalyst-analyst/SKILL.md for catalyst reasoning
12. Read skills/exposure-coach/SKILL.md for market posture assessment
13. Read skills/covered-call-strategy/SKILL.md for CC/CSP analysis
14. Read skills/signal-postmortem/SKILL.md for reviewing completed cycles
15. Read skills/portfolio-cleanup/SKILL.md for cleanup candidates
16. Read skills/technical-analyst/SKILL.md for market structure analysis (HH/HL/LL/LH), trend flip identification, support/resistance, volume confirmation. Apply to: assess if key stocks are in valid uptrend (safe to add) or showing trend breakdown (wait for confirmation).

### Phase 3: Generate Reports & Fetch Data
16. Run `python3 scripts/generate_report.py` to update portfolio spreadsheet and weekly report
17. Run `python3 scripts/fetch_price_data.py` on individual stock holdings for current prices and swing scores
18. Present: portfolio summary, top/bottom performers, accumulation progress vs goals.yaml

### Phase 4: Discrepancy Check
19. After importing new holdings data, COMPARE actual holdings vs expected state (tracker.yaml):
    - For each ticker: actual shares vs tracker expected shares
    - If delta > 0.5 shares: flag discrepancy
    - Check if any pending_orders appear to have filled or expired
    - Write discrepancy alerts to tracker.yaml
20. Present discrepancies clearly and ask user to confirm

### Phase 4b: Market Top Detection & Theme Lifecycle
20b. Run `python3 scripts/distribution_days.py` for PRECISE distribution day data.
    Report: "SPY d5=X, d15=X, d25=X | QQQ d5=X, d15=X, d25=X | Overall: [RISK LEVEL]"
20b2. Then run the full 6-component Market Top Detection scoring (from exposure-coach skill):
    - Distribution day count (from script), leading stock health, defensive rotation, breadth divergence, index technicals, sentiment
    - Report composite score and risk zone (Green/Yellow/Orange/Red/Critical)
20c. Assess theme lifecycle for user's key themes:
    - AI Infrastructure: stage? still accelerating or maturing?
    - Optical/Photonics: still emerging?
    - Quantum: still emerging?
    - Report any theme stage shifts from last week
20d. Check institutional flow changes (quarterly, after 13F deadlines):
    - If near a 13F deadline (mid-Feb/May/Aug/Nov): flag "13F data coming, check NBIS/GOOGL/META institutional changes"

### Phase 5: Position Build Review
21. Read state/actions/position_build_plan_2026-05-18.md (or most recent)
22. Run fetch on ALL position build tickers (even if not currently held)
23. For each position build, report:
    - Current price vs target entry price → % gap → getting closer or further?
    - Has 20-MA or 50-MA shifted? Should limit prices be adjusted?
    - Any new catalysts that change timing or urgency?
    - Status: FILLING / APPROACHING / STALLED / NEEDS ADJUSTMENT
24. If any build target moved >10% away: "Consider raising limit or capitulation order"
25. If any build target within 3%: "⚠️ ABOUT TO FILL — confirm order active"
26. For watchlist stocks WITHOUT GTC: is this a good week to place?

### Phase 6: Swing & CC Review
27. Review active swing cycles: status, what filled, what's pending
28. Completed cycles: run signal-postmortem framework (what worked, what didn't)
29. Option income this week: CC/CSP premium earned, cost basis impact
30. Next CC/CSP opportunities forming (which stocks approaching CC-eligible RSI)
31. For any holding with upcoming catalyst: note it (e.g., "APP: June platform launch")

### Phase 7: Deep Market Analysis & Independent Reasoning
32. Use web search: what are next week's KEY events?
    - Economic data (PCE, CPI, jobs, Fed minutes)
    - Earnings of relevant companies
    - Fed speeches / rate decisions
    - Geopolitical events (Iran, China trade, tariffs)
    - Sector-specific catalysts (AI conferences, product launches)
33. INDEPENDENT REASONING — connect the dots:
    - "PCE hot → yields spike → growth sells off → our GTC orders fill = GOOD"
    - "Iran peace deal → oil drops → inflation eases → Fed less hawkish → tech rallies"
34. VALIDATE WAVE THESES with this week's evidence:
    - Wave 1 (GPU): NVDA/AMD/ARM developments
    - Wave 2 (Memory): HBM, SNDK
    - Wave 3 (Optical): COHR/GLW/EUV — did photonics thesis advance?
    - Wave 4 (Quantum): IONQ — govt grant playing out?
    - Networking: ANET recovery trajectory?
35. SENTIMENT ANALYSIS:
    - Market sentiment indicators (VIX, put/call ratio)
    - Retail vs institutional positioning
    - Contrarian signals: is everyone too bullish/bearish?
    - If data/others_opinions/ has YouTuber transcripts: incorporate their views

### Phase 8: Next Week Outlook — Forward-Looking Analysis
36. Present "NEXT WEEK OUTLOOK" section:
    - Key events calendar (dates and expected impact)
    - Scenario analysis: bull case vs bear case for the week
    - Which of YOUR stocks are most affected by upcoming events?
    - Specific preparation actions
37. Position adjustments for next week:
    - Any GTC to raise/lower based on new info?
    - Any new GTC to place?
    - Any CC/CSP opportunities forming?
    - Swing trim/entry signals approaching?
38. NEW DISCOVERY suggestions:
    - Based on this week's trends, what NEW stocks/themes should you research?
    - "Optical stocks rallied 5-10% on NVDA comments. Wave 3 accelerating. Look at: [tickers]"

### Phase 9: Action Plan & Tracking
39. Present prioritized action list for next week (top 7-10 items)
40. Write state/actions/weekly_YYYY-MM-DD.md with all suggestions
41. Review action tracker files from past week — summarize execution rate
42. Update state/progress/tracker.yaml with all changes
43. Update state/progress/financial_goal.yaml progress_log

## Output Structure (all sections required)

```
═══ WEEKLY REVIEW — Week of [DATE] ═══

FINANCIAL GOAL PROGRESS
  [Value vs milestone. AHEAD/BEHIND/ON TRACK.]

THIS WEEK'S PERFORMANCE
  [Portfolio change. Top/bottom movers. Key events.]

EXECUTION REVIEW
  [Suggested vs executed. Rate. What missed.]

SWING CYCLES & CC INCOME
  [Active cycles. Option income earned. Cost basis updates.]

POSITION BUILD STATUS
  [All GTC orders. Gaps. Adjustments needed.]

DISCREPANCIES
  [Any unexpected changes vs tracker]

MARKET REASONING & THESIS VALIDATION
  [Independent analysis. Wave thesis check. Macro implications.]
  [Sentiment analysis. Contrarian signals.]

NEXT WEEK OUTLOOK (Forward Look)
  [Key events calendar]
  [Scenario: if X → impact on portfolio]
  [Which stocks to watch most closely]
  [Preparation actions]

NEW DISCOVERIES & IDEAS
  [Proactive suggestions for research or position changes]
  [Wave/theme evolution observations]

NEXT WEEK ACTION PLAN (Top 10)
  [Prioritized list with specific instructions]
```

## Tracking User Confirmations
When the user confirms a discrepancy or reports an action:
1. Update state/progress/tracker.yaml (shares, cycles, cash flow, resolve discrepancy)
2. Update the relevant action tracker in state/actions/
3. Add a history entry to the appropriate accumulation_goals or position_builds section
