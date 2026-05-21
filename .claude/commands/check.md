Check a specific stock's swing signal and technical levels, with news/catalyst context.

Usage: /check TICKER (e.g., /check META)

Steps:
1. ALWAYS read state/holdings/current.yaml first to check if user holds this stock and get their exact shares, avg cost, and account info
2. ALWAYS read state/holdings/goals.yaml to check if this stock has an accumulation target
3. ALWAYS read state/progress/tracker.yaml to check:
   - Open swing cycles for this ticker
   - Pending orders for this ticker
   - Position build status if applicable
   - Cash available for new orders
4. Check if state/theses/ has a file for this ticker (e.g., state/theses/nbis*.md or state/theses/euv*.md). If found, read it to understand the user's original investment thesis, then evaluate whether current price action/news supports or invalidates that thesis.
5. Check state/actions/ for any recent action tracker that mentions this ticker — note pending/suggested actions.
6. Run `python3 scripts/fetch_price_data.py $ARGUMENTS` for live price data and swing score
7. Read skills/swing-accumulator/SKILL.md for scoring interpretation and trim/rebuy logic
8. Read skills/news-catalyst-analyst/SKILL.md for catalyst reasoning framework
9. Use web search to check for recent news, catalysts, political/social signals, and upcoming events for this stock (e.g., "[TICKER] news today", earnings dates, Trump posts mentioning the company/sector, geopolitical events). Apply second-order logical reasoning per the catalyst skill (e.g., presidential visit -> trade deal -> who benefits?)
10. Produce a catalyst modifier (STRONG_POSITIVE to STRONG_NEGATIVE) and adjust the technical signal accordingly
11. If user holds this stock: calculate exact trim shares (based on their position size), rebuy share counts (based on trim proceeds / rebuy price), and expected share gain from the full cycle
12. If user does NOT hold this stock: provide a quick assessment of whether it's in a buy zone, sell zone, or neutral zone — and reference skills/stock-evaluator/SKILL.md if they might want to start a position
13. Present: key metrics table, swing score, catalyst assessment, position context, and specific actionable recommendation with exact share counts and prices

The recommendation MUST reference the user's actual position size and cost basis -- never give generic advice without anchoring to their real numbers. Keep output concise: one table + catalyst context + action items.

## Action Tracking

14. If the check produces actionable suggestions (trim, buy, adjust orders), append them to the current day's action tracker:
    - If `state/actions/daily_YYYY-MM-DD.md` exists, append to it
    - If not, create `state/actions/check_TICKER_YYYY-MM-DD.md` with the suggestion
15. If the check reveals a pending order should be adjusted (e.g., rebuy price too high/low), note it in the tracker and in state/progress/tracker.yaml pending_orders.

## Tracking User Confirmations

When the user says they acted on a /check suggestion:
1. Update the relevant action tracker in state/actions/
2. Update state/progress/tracker.yaml (shares, cash flow, cycles, builds)
