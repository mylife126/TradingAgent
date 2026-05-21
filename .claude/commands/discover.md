Discover, analyze, rank, and track high-potential new stocks.
ALL actions serve the FINANCIAL GOAL defined in state/progress/financial_goal.yaml.

Usage:
  /discover TICKER1 TICKER2 TICKER3    — Compare and rank specific stocks
  /discover theme:quantum              — Find candidates in a theme/sector
  /discover sector:photonics           — Research and find top stocks in a sector
  /discover wave:3                     — Find stocks in a specific AI infrastructure wave
  /discover update                     — Re-rank existing watchlist with fresh data
  /discover                            — Auto-discover: scan for high-potential stocks based on existing themes and trends

When NO specific tickers are provided (theme/sector/wave/auto mode):
  - Use web search to find top stocks in the requested sector or theme
  - Search for: "[theme] stocks to buy 2026", "best [sector] stocks", "[theme] ETF holdings"
  - Cross-reference with existing watchlist themes in state/discovery/watchlist.yaml
  - Identify 3-6 candidates, then run the full scoring pipeline on each
  - This allows the USER to discover stocks they didn't already know about

Steps:
0. ALWAYS read state/progress/financial_goal.yaml — filter: does this stock help reach $1M? Required CAGR = 23.4%.
1. ALWAYS read state/discovery/watchlist.yaml (if exists) — check if these stocks were analyzed before. If so, load previous scores and note what changed.
2. ALWAYS read state/holdings/current.yaml and state/holdings/goals.yaml — understand current portfolio context, concentration, cash available.
3. ALWAYS read state/progress/tracker.yaml — check free cash, pending orders, position builds in progress.
4. Read all files in state/theses/ — understand existing wave theories (photonics, quantum, etc.) and see if new candidates fit.
5. Check data/others_opinions/ for any external opinion files on these tickers. If found, integrate as confirmation/contradiction.
6. Read skills/stock-discovery/SKILL.md for the full framework (scoring dimensions, ranking methodology).
7. Read skills/exposure-coach/SKILL.md — is the market allowing new entries?
8. Read skills/position-sizer/SKILL.md — size any recommended positions.
9. Read skills/news-catalyst-analyst/SKILL.md — catalyst and second-order reasoning.
10. For EACH ticker:
    a. Run `python3 scripts/fetch_price_data.py TICKER` for technicals
    b. Use web search for: revenue growth, earnings, analyst targets, recent news, catalysts
    c. Apply 5-question quick screen (eliminate if <3/5)
    d. Score on 7 dimensions (growth, profitability, moat, catalyst, entry, valuation, theme)
    e. Determine verdict: STRONG BUY / BUY / WATCH / PASS
11. Rank all candidates by weighted score.
12. For top-ranked (score 7+): design entry plan with tranches, sizing, stop loss.
13. Present: ranking table + detailed analysis for top picks + comparison with previous analysis if exists.

## Tracking (REQUIRED)

14. ALWAYS write/update `state/discovery/watchlist.yaml` with:
    - Ranked candidates (ticker, score, verdict, date, theme, entry plan status)
    - Watch list (stocks to revisit later with conditions)
    - Passed stocks (rejected with reason)
    - Themes tracked
15. For each stock analyzed in depth, write `state/discovery/analysis_TICKER_YYYY-MM-DD.md` with the full analysis.
16. Update state/actions/ with any suggested buy orders.
17. Tell user: "Discovery saved to state/discovery/. Run /discover update anytime to re-rank."

## Re-Ranking (when user says "/discover update")

1. Load watchlist.yaml
2. For each ranked candidate and watch list stock:
   a. Fetch fresh price data
   b. Check for new catalysts/news
   c. Re-score
   d. Compare to previous score — flag if moved significantly (±1.5 points)
3. Re-rank and present changes: "IONQ moved from #3 to #1 (catalyst fired)" or "POET dropped to PASS (Marvell cancelled)"

## External Opinions (Future Integration)

When data/others_opinions/ has files:
- Expected format: `TICKER_source_YYYY-MM-DD.md` (e.g., `IONQ_youtube_2026-05-15.md`)
- Read and extract: bull/bear arguments, price targets, key insights
- Score overall sentiment: BULLISH / MIXED / BEARISH
- Note in analysis: "External consensus: [X], which [confirms/contradicts] our analysis because [reason]"
- If no files exist: proceed normally, note "No external opinions available"

## Analysis Record (REQUIRED)

18. ALWAYS write a consolidated analysis record to `state/discovery/analysis_SESSION_YYYY-MM-DD.md` (or `analysis_TICKER_YYYY-MM-DD.md` for single-stock). This file records:
    - Theme/sector researched
    - All candidates discovered and evaluated
    - Scoring table with all 7 dimensions
    - Reasoning for each score
    - Final ranking with verdicts
    - Comparison to previous analysis if exists
    - Entry plans for BUY+ candidates

## User Selection (REQUIRED — End of Every /discover Call)

19. At the END of every /discover output, ALWAYS ask the user:
    "Which stock(s) do you want to add to your watchlist? And for any BUY candidates, should I set up the entry plan?"

    Options to present:
    - Add to watchlist (WATCHING status — track but no orders yet)
    - Add with entry plan (BUILDING status — define tranches and GTC orders)
    - Pass (rejected — record reason and move on)

20. When user responds with their selection:
    a. Update state/discovery/watchlist.yaml:
       - Add to ranked_candidates (if BUY+) or watch_list (if WATCH)
       - Add to passed (if rejected)
       - Update themes_tracked if new theme identified
    b. Update state/progress/tracker.yaml:
       - Add to position_builds (if BUILDING)
       - Add to accumulation_goals in state/holdings/goals.yaml (if target set)
       - Update cash_flow committed amounts
       - Add to pending_orders if GTC orders suggested
    c. Write thesis to state/theses/ if user's reasoning is non-obvious
    d. Update state/actions/ with any new suggested orders
    e. Confirm to user: "Added [TICKER] to watchlist as [status]. Entry plan: [details]. Tracker updated."
