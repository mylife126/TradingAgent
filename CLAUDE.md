# Stocks Trading - Claude Code Workflow

## Project Purpose

Personal trading workflow for Xin Shen. Three core objectives:
1. **Portfolio Tracking** — Import holdings from Fidelity & Robinhood, track cost basis, performance, and generate reports
2. **Share Accumulation (Swing)** — Daily/weekly operation guidance to grow share count on conviction holdings (e.g., Nebius) without deploying new cash
3. **New Stock Evaluation** — On-demand analysis of stocks to determine if/how to build a position

## Financial Goal (MASTER OBJECTIVE)

**All commands, skills, and recommendations serve this goal:**
- **Target**: $1,000,000 portfolio value by May 2028 (2 years)
- **Stretch**: $2,000,000 by May 2031 (5 years)
- **Starting point**: $656,244 (May 15, 2026)
- **Required CAGR**: 23.4% (primary) / 25.0% (stretch)
- **Tracking**: `state/progress/financial_goal.yaml`

Every `/daily`, `/weekly`, `/cleanup`, `/check`, `/plan`, `/evaluate` must consider: "Does this action move toward or away from the $1M goal?"

## Key Principles

- Never auto-execute trades. All outputs are recommendations requiring manual execution.
- Focus on share accumulation over profit-taking — the goal is to own MORE shares, not to realize gains.
- Be explicit about risk levels and always define stop-loss/re-entry levels.
- All analysis must include a "do nothing" option — holding is always valid.
- Every recommendation must be sized using position-sizer logic (max 1-2% risk per trade).
- Before recommending buys, check exposure-coach: is the market allowing new entries?

## Directory Structure

```
stocksTrading/
├── CLAUDE.md                  # This file
├── skills/                    # Skill definitions (prompt + logic)
│   ├── financial-goal-planner/# MASTER: $1M goal, milestones, strategy
│   ├── exposure-coach/        # Should I be buying at all? (market posture)
│   ├── position-sizer/        # How many shares? (risk-based sizing)
│   ├── portfolio-tracker/     # Holdings import, cost basis, performance
│   ├── portfolio-cleanup/     # Sell candidate identification
│   ├── swing-accumulator/     # Share growth swing strategy
│   ├── stock-evaluator/       # New stock analysis & build strategy
│   ├── market-scanner/        # Daily market context
│   ├── technical-analyst/     # Chart analysis
│   ├── news-catalyst-analyst/ # News, geopolitics, second-order reasoning
│   ├── scenario-analyzer/     # Event-driven 3-scenario analysis
│   ├── signal-postmortem/     # Learning loop: what worked, what didn't
│   └── stock-discovery/       # Multi-stock comparison, ranking, wave/theme tracking
├── workflows/                 # Multi-step workflow definitions
├── scripts/                   # Python utilities
├── state/                     # Persistent state (git-tracked)
│   ├── holdings/              # Current holdings snapshots
│   ├── actions/               # Action tracker docs (suggestions + statuses)
│   ├── progress/              # tracker.yaml — goals, cycles, cash, discrepancies
│   ├── theses/                # Investment theses lifecycle
│   └── journal/               # Trade journal entries
├── reports/                   # Generated analysis reports
├── data/                      # Raw data imports
│   ├── fidelity/              # Fidelity CSV exports
│   └── robinhood/             # Robinhood CSV exports
└── templates/                 # Report templates
```

## Workflows

### Daily (5-10 min)
1. Run market scanner for context (regime, news, sector rotation)
2. Check news/catalysts -- political signals, geopolitics, social media, upcoming events
3. Check swing-accumulator signals for active positions (adjusted by catalyst modifiers)
4. Check progress tracker for pending orders, open cycles, and any unresolved actions
5. Generate action plan: hold / trim / add levels with specific prices
6. Write action tracker to `state/actions/daily_YYYY-MM-DD.md`

### Weekly (30-60 min)
1. Import latest holdings from brokerages
2. Run portfolio tracker to update spreadsheet
3. Compare actual holdings vs. tracker expectations -- flag discrepancies
4. Review performance vs. goals and accumulation progress
5. Adjust swing parameters based on weekly price action
6. Write action tracker + summarize week's execution rate

### On-Demand
- `/cleanup` -- Review all holdings for sell candidates, write action tracker
- `/evaluate TICKER` -- Analyze new candidates, write entry plan if BUY+
- `/plan TICKER` -- Detailed swing plan, register cycle in tracker
- `/check TICKER` -- Quick signal, append actions if actionable
- Deep technical analysis with chart images
- Position sizing for new entries

## Data Sources

- **Fidelity CSV**: Export from Fidelity Positions page
- **Robinhood CSV/PDF**: Export from Robinhood account (activity CSV + monthly statements)
- **Yahoo Finance** (via yfinance): Price data, fundamentals, technicals
- **Chart images**: User-provided candlestick screenshots
- **External Research** (for /daily and /weekly reasoning):
  - stockanalysis.com — market news, earnings calendar, stock screener
  - Web search — breaking news, macro data, geopolitics
  - tradingeconomics.com — economic calendar (PCE, CPI, jobs)
  - finviz.com — stock screener, sector heatmap
- **Sentiment & Opinions**:
  - YouTube: @RhinoFinance (犀牛财经), @财经观察站 — Chinese financial analysis
  - data/others_opinions/ — crawled transcripts (future integration)
- **Sector-Specific**:
  - semianalysis.com — AI chip deep analysis
  - nextplatform.com — AI infrastructure, data center news
- **Macro & Fed**:
  - CME FedWatch — rate probability
  - FRED — official economic data

## Trading Philosophy (User Profile)

- Long-term conviction holder who struggles with profit-taking
- Goal: Grow share count on winners using swing mechanics
- Problem: "Always greedy" — doesn't sell on the way up OR down
- Solution: Rule-based system with pre-defined sell/rebuy levels
- Risk tolerance: Moderate — willing to miss some upside to lock in share growth

## Slash Commands (registered in .claude/commands/)

- `/daily` — Run daily market scan + swing signals for all holdings
- `/weekly` — Full portfolio import and review
- `/check TICKER` — Quick swing signal check for one stock
- `/evaluate TICKER` — Full analysis of a new stock candidate
- `/plan TICKER` — Detailed accumulation plan for a held stock
- `/cleanup` — Review all holdings for sell candidates, dead money, broken theses
- `/discover TICKER1 TICKER2` — Compare, rank, and track new stock candidates
- `/status` — Unified dashboard: goal progress, adjusted costs, all trackers in one view
- `/cc` — Covered call + cash-secured put opportunities (option income strategy)
- `/positions` — All GTC orders dashboard: gaps, adjustments, fill probability

You can also just ask naturally: "check META", "what should I do today?", "evaluate PLTR", "compare RKLB vs IONQ", etc.

## Action Tracking & Progress

All commands auto-track their suggestions in `state/actions/` and update `state/progress/tracker.yaml`.

- **Action tracker files** (`state/actions/*.md`): Every command writes suggested actions with a status (SUGGESTED / EXECUTED / SKIPPED). When the user reports executing an action, update both the action file and tracker.yaml.
- **Progress tracker** (`state/progress/tracker.yaml`): Central state for accumulation goals, swing cycles, position builds, pending orders, cash flow, and discrepancy alerts.
- **Discrepancy detection**: `/weekly` compares actual holdings (from CSV import) against tracker expectations and flags differences (e.g., a rebuy order that filled).
- **User confirmations**: When the user says "I sold X" or "I did Y", update the action tracker status AND the progress tracker in a single operation.
