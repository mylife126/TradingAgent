# Stocks Trading — Claude Code Workflow

A rule-based trading workflow powered by Claude Code. Designed for long-term holders who want to grow share count on conviction positions using disciplined swing mechanics.

## Financial Goal (Everything Serves This)

| | Primary | Stretch |
|--|---------|---------|
| Target | **$1,000,000** | **$2,000,000** |
| Timeline | 2 years (May 2028) | 5 years (May 2031) |
| Starting | $656,244 | $656,244 |
| Required CAGR | 23.4% | 25.0% |

Every command, every recommendation, every trade is evaluated against: "Does this move me toward $1M?"

Growth comes from 4 sources:
- **Market appreciation** (~12%/yr) — hold quality compounders
- **Swing accumulation** (~8%/yr) — trim/rebuy cycles grow share count
- **Capital rotation** (~3%/yr) — sell dead money, buy winners
- **Asymmetric bets** (~2%/yr) — small ambush positions that can 5-10x

## What This Does

1. **Daily scan** — Market regime + exposure check + swing signals + catalyst analysis
2. **Weekly review** — Import brokerage data, track goal progress, detect discrepancies
3. **Stock evaluation** — Analyze candidates with position sizing and goal alignment
4. **Swing accumulation** — Trim/rebuy cycles to grow shares without new capital
5. **Portfolio cleanup** — Identify dead money, free cash for better opportunities
6. **Progress tracking** — Milestones, action tracking, postmortems

---

## Setup

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- Python 3.10+
- A Fidelity and/or Robinhood account

### Install

```bash
cd ~/Dropbox/MyCodeWorkSpace/stocksTrading
pip install -r requirements.txt
```

That installs `yfinance` (free market data) and `pyyaml` (state files).

### Configure Your Goals

Edit `state/holdings/goals.yaml` to set your accumulation targets:

```yaml
NBIS:
  strategy: accumulate
  target_shares: 500
  shares_gained_swing: 0
  notes: "Core conviction holding"
  started: "2025-08-15"

META:
  strategy: accumulate
  target_shares: 100
  shares_gained_swing: 0
  notes: "Building position on pullbacks"
  started: "2026-05-01"
```

### Import Your Holdings (First Time)

1. **Fidelity**: Log in → Positions → Download (CSV) → save to `data/fidelity/`
2. **Robinhood**: Account → Statements → Export positions → save to `data/robinhood/`
3. Run `/weekly` or say "update portfolio"

---

## Usage

Start Claude Code from this directory:

```bash
cd ~/Dropbox/MyCodeWorkSpace/stocksTrading
claude
```

### Slash Commands

| Command | What it does | When to use |
|---------|-------------|-------------|
| `/daily` | Market scan + swing signals for all holdings | Every trading day, before market open |
| `/check TICKER` | Quick swing signal for one stock | Anytime you want a read on a stock |
| `/evaluate TICKER` | Full go/no-go analysis for a new stock | When considering a new position |
| `/plan TICKER` | Detailed trim/rebuy plan with math | When you want specific swing levels |
| `/weekly` | Import CSVs + update spreadsheet + review | Weekends |
| `/cleanup` | Review all holdings for sell candidates | When portfolio feels bloated or cash is needed |
| `/discover TICKER1 TICKER2` | Compare and rank specific stocks you name | When evaluating multiple candidates |
| `/discover theme:quantum` | Research and find top stocks in a theme | When exploring a sector you don't know well |
| `/discover sector:photonics` | Same as theme — discover stocks you haven't heard of | Sector research |
| `/discover update` | Re-rank entire watchlist with fresh data | Monthly or after major market moves |
| `/discover` (no args) | Auto-discover based on existing themes/trends | When looking for new ideas |

All commands automatically track their suggestions in `state/actions/` and update `state/progress/tracker.yaml`. When you tell Claude you executed an action ("I sold QBTS", "I placed the NBIS rebuy"), it updates the tracker status.

### Natural Language (also works)

You don't have to use slash commands. These all work:

```
"what should I do today?"
"check NBIS"
"should I trim META?"
"is PLTR a good buy?"
"how do I build a position in AMZN?"
"update portfolio"
"how am I doing?"
```

---

## Daily Workflow (5 minutes)

```
you: /daily

Claude:
  1. Fetches SPY, QQQ, IWM, VIX → determines market regime
  2. Runs swing score on each of your holdings
  3. Returns a table like:

  Ticker  Price    Chg%   RSI   vs20MA  Score  Signal
  NBIS    $221.15  +6.7%  74.0  +32.0%  5/10   HOLD (borderline)
  META    $618.43  +0.3%  28.2  -3.1%   1/10   REBUY ZONE

  Action: No orders today. NBIS approaching trim zone if rally
  continues. META oversold — consider adding if you have a target.
```

---

## Weekly Workflow (30 minutes)

```
1. Export positions from Fidelity/Robinhood
2. Drop CSVs into data/fidelity/ and data/robinhood/
3. Open Claude:

you: /weekly

Claude:
  - Parses CSVs, detects changes since last import
  - Updates reports/portfolio_summary.csv (your tracking spreadsheet)
  - Generates reports/weekly_review_YYYY-MM-DD.md
  - Shows accumulation progress:

    Ticker  Current  Target  Progress  Swing Gains
    NBIS    175      500     35%       +0
    META    50       100     50%       +3

  - Recommends swing level adjustments for next week
```

---

## Action Tracking System

Every command that produces actionable suggestions writes them to `state/actions/` with status tracking. This creates an audit trail of what was suggested, what you actually did, and what you skipped.

### How It Works

1. **Commands generate action files**: `/cleanup` creates `state/actions/cleanup_2026-05-15.md`, `/daily` creates `state/actions/daily_2026-05-15.md`, etc.
2. **Each action has a status**: `SUGGESTED` -> `EXECUTED` / `SKIPPED` / `PARTIAL` / `CANCELLED`
3. **You report back naturally**: Say "I sold QBTS" or "skip the ONDS sell" and Claude updates the tracker.
4. **Journal entries link to action docs**: Each day's journal references its action tracker for a complete record.

### Action File Types

| File Pattern | Created By | Contains |
|-------------|------------|----------|
| `cleanup_YYYY-MM-DD.md` | `/cleanup` | Sell candidates, redeployment suggestions |
| `daily_YYYY-MM-DD.md` | `/daily` | Daily trim/rebuy signals, order updates |
| `weekly_YYYY-MM-DD.md` | `/weekly` | Weekly rebalancing suggestions |
| `plan_TICKER_YYYY-MM-DD.md` | `/plan` | Swing cycle actions for one stock |
| `evaluate_TICKER_YYYY-MM-DD.md` | `/evaluate` | Entry plan for a new position |
| `check_TICKER_YYYY-MM-DD.md` | `/check` | Quick signal actions (if actionable) |

---

## Progress Tracker

The file `state/progress/tracker.yaml` is the central state for tracking your trading progress across sessions. It is automatically read and updated by all commands.

### What It Tracks

**Accumulation Goals** — Share count targets with history of changes:
```yaml
NBIS:
  target_shares: 500
  current_shares: 158.248
  shares_to_go: 341.752
  history:
    - date: "2026-05-15"
      event: "Trimmed 17 in first swing cycle"
      shares: 158.248
```

**Swing Cycles** — Each trim/rebuy cycle from start to completion:
```yaml
NBIS_cycle_1:
  status: OPEN
  trim: { date: "2026-05-15", shares: 17, price: 213.10 }
  rebuys:
    L1: { target_price: 195, target_shares: 19, status: PENDING }
    L2: { target_price: 170, target_shares: 8, status: PENDING }
  expected_result: { net_share_gain: 10 }
```

**Position Builds** — New positions being built via tranches:
```yaml
IONQ:
  status: BUILDING
  target_shares: 100
  total_filled: 50
  total_pending: 50
```

**Cash Flow** — Estimated cash available, committed to orders, and free:
```yaml
cash_flow:
  estimated_remaining_cash: 26192.80
  total_committed: 17905.00
  free_cash_after_commitments: 8287.80
```

**Discrepancy Alerts** — Flagged when actual holdings differ from expectations after a `/weekly` import:
```
DISCREPANCY: NBIS expected 158.248, actual 177.248 (+19)
Likely: Rebuy L1 filled. Confirm?
```

### How Journals and Action Docs Connect

```
/daily runs on May 15
  -> writes state/actions/daily_2026-05-15.md (suggested actions)
  -> updates state/progress/tracker.yaml (pending orders, cash)
  -> journal entry state/journal/2026-05-15.md links to action doc

User says "I trimmed NBIS"
  -> daily_2026-05-15.md: TRIM action status -> EXECUTED
  -> tracker.yaml: NBIS shares updated, swing cycle opened, cash updated

/weekly runs on May 18
  -> imports new CSVs, compares actual vs tracker expected
  -> flags discrepancies (e.g., "NBIS rebuy filled!")
  -> updates tracker.yaml with resolved discrepancies
  -> writes state/actions/weekly_2026-05-18.md
  -> summarizes: "This week: 8/12 actions executed, 2 skipped, 2 pending"
```

---

## Swing Accumulator Logic

The core strategy for growing shares without new cash:

### Signal Scoring (0-10)

| Factor | 0 pts | 1 pt | 2 pts |
|--------|-------|------|-------|
| Price vs 20-MA | <5% above | 5-10% above | >10% above |
| RSI(14) | <60 | 60-70 | >70 |
| Volume | <1.5x avg | 1.5-2x avg | >2x avg |
| Near 52w high | >5% away | 2-5% away | <2% away |
| Rally duration | <3 days | 3-4 days | 5+ days |

### Action Thresholds

| Score | Action |
|-------|--------|
| 8-10 | **Trim 30%** — sell and set rebuy orders |
| 6-7 | **Trim 20%** — moderate trim |
| 4-5 | **Trim 10%** — optional, light trim |
| 0-3 | **Hold** — no action, or look for rebuy |

### Example Cycle

```
Start:    175 shares @ $50
Trim 30%: Sell 52 shares @ $62 (+25%)     → Cash: $3,224
Rebuy L1: Buy 35 shares @ $55 (-11%)      → Spent: $1,925
Rebuy L2: Buy 22 shares @ $51 (-18%)      → Spent: $1,122
Result:   180 shares @ lower avg cost     → Gained: +5 shares
```

### Catalyst Modifier (News/Events Override)

Before acting on the score, a catalyst check adjusts the threshold:

| Catalyst | Modifier | Example |
|----------|----------|---------|
| STRONG_POSITIVE | +2 (harder to trim) | AI spending bill passing, earnings in 3 days |
| POSITIVE | +1 | Presidential visit benefits sector |
| NEUTRAL | 0 | No change |
| NEGATIVE | -1 (easier to trim) | Regulatory crackdown, negative Trump post |
| STRONG_NEGATIVE | -2 (trim now) | Thesis-breaking news |

Example: Score 6 (normally trim 20%) + STRONG_POSITIVE catalyst = need score 8 → HOLD.

This catches situations like: "Score says trim NBIS, but there's an AI infrastructure bill vote next week that could send it higher — wait."

### Rules

- Never trim more than 30% at once
- Never trim the core 50% (long-term hold portion)
- Rebuy orders are always limit GTC
- If stock runs away after trim: accept it, core position still rides
- If stock drops past rebuy levels: hold cash, reassess thesis
- Catalyst modifiers adjust timing/size but NEVER override hard stop-losses

---

## File Structure

```
stocksTrading/
├── .claude/
│   ├── commands/           ← Slash commands (auto-registered)
│   │   ├── daily.md
│   │   ├── weekly.md
│   │   ├── check.md
│   │   ├── evaluate.md
│   │   ├── plan.md
│   │   └── cleanup.md
│   └── settings.local.json ← Permission config
├── CLAUDE.md               ← Auto-loaded project context
├── skills/                 ← Decision frameworks (read on demand)
│   ├── market-scanner/SKILL.md
│   ├── news-catalyst-analyst/SKILL.md
│   ├── portfolio-cleanup/SKILL.md
│   ├── portfolio-tracker/SKILL.md
│   ├── stock-evaluator/SKILL.md
│   ├── swing-accumulator/SKILL.md
│   └── technical-analyst/SKILL.md
├── workflows/              ← Multi-step workflow definitions
│   ├── daily-scan.yaml
│   ├── weekly-portfolio-review.yaml
│   └── evaluate-stock.yaml
├── scripts/                ← Python utilities
│   ├── fetch_price_data.py    ← Price + technical indicators + swing score
│   ├── import_holdings.py     ← Fidelity/Robinhood CSV parser
│   └── generate_report.py    ← Spreadsheet + report generator
├── state/                  ← Persistent state (git-tracked)
│   ├── holdings/
│   │   ├── current.yaml       ← Latest holdings snapshot
│   │   └── goals.yaml         ← Accumulation targets
│   ├── actions/               ← Action tracker docs (per command, per day)
│   │   ├── cleanup_*.md
│   │   ├── daily_*.md
│   │   ├── weekly_*.md
│   │   ├── plan_*.md
│   │   ├── evaluate_*.md
│   │   └── check_*.md
│   ├── progress/
│   │   └── tracker.yaml       ← Central progress tracker (goals, cycles, cash)
│   ├── theses/                ← Investment thesis documents
│   └── journal/               ← Trade journal entries
├── data/                   ← Drop CSVs here (gitignored)
│   ├── fidelity/
│   └── robinhood/
├── reports/                ← Generated outputs (gitignored)
│   ├── portfolio_summary.csv
│   └── weekly_review_*.md
└── requirements.txt
```

---

## How It Works Under the Hood

```
You type /check NBIS
       ↓
Claude auto-loads CLAUDE.md (project context, always)
       ↓
Claude runs .claude/commands/check.md (the slash command definition)
       ↓
check.md instructs: "run fetch_price_data.py, read SKILL.md, apply logic"
       ↓
Claude executes scripts, reads skill frameworks, returns recommendation
```

- **CLAUDE.md** = project context, auto-loaded every session
- **.claude/commands/*.md** = slash command definitions, registered in `/` menu
- **skills/*.md** = decision frameworks, read on-demand when commands reference them
- **scripts/*.py** = data fetching and computation
- **state/** = persistent data between sessions
- **state/actions/** = action tracker docs with suggestion statuses
- **state/progress/tracker.yaml** = central progress tracker (goals, swing cycles, cash flow)

---

## Data Sources

| Source | Cost | Used For |
|--------|------|----------|
| Yahoo Finance (yfinance) | Free | Prices, MAs, volume, RSI |
| Your brokerage CSVs | Free | Holdings, cost basis |
| Web search | Free | Fundamentals, news, catalysts |
| Chart screenshots (you provide) | Free | Visual technical analysis |

No paid API keys required for base functionality.

---

## Tips

- **Be specific**: "should I trim NBIS at $230?" gets better answers than "what about NBIS?"
- **Provide charts**: Screenshot a candlestick chart and paste it for technical analysis
- **Update weekly**: The system works best with fresh holdings data
- **Trust the score**: If the swing score says hold, hold. That's the whole point — rules over emotions.
- **Journal**: After every trim/rebuy, note it. Patterns emerge over time.

---

## Disclaimer

This is a personal decision-support tool, not financial advice. All outputs are recommendations requiring manual execution. Never auto-executes trades. You are responsible for your own investment decisions.
