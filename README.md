# Stocks Trading — Claude Code Agentic Workflow

> **Your AI-powered trading co-pilot.** 11 slash commands. 14 decision-making skills. Automated progress tracking. One goal: grow your portfolio systematically while you sleep.

## What This Does

This is a **fully agentic stock trading workflow** built on Claude Code that turns your terminal into a professional-grade trading desk:

- 🎯 **Sets a financial goal** (e.g., $1M) and ensures EVERY decision serves it
- 📊 **Scans the market daily** with independent reasoning, wave thesis validation, and catalyst analysis
- 🔄 **Executes swing accumulation** — mechanically trims winners high, rebuys low, grows share count for free
- 💰 **Generates option income** — sells covered calls and cash-secured puts to reduce cost basis toward **zero**
- 🏗️ **Manages position builds** — tracks all GTC limit orders, alerts when approaching fill, recommends adjustments
- 🧠 **Reasons like a strategist** — connects macro events → sector trends → your specific stocks using second-order thinking
- 📈 **Tracks everything** — adjusted cost basis, swing cycle P&L, option income, goal progress, execution rate
- 🔍 **Discovers new opportunities** — scores and ranks stocks across themes (AI infrastructure, quantum, photonics, etc.)
- ⚠️ **Protects your capital** — distribution day monitoring, market top detection, breadth analysis gates

**Real results from the first week of operation:**
- ✅ First swing cycle: trimmed NBIS at $213, rebought at $195 → **+19 shares gained**
- ✅ First covered call sold: **+$656 income** in one trade (cost basis reduced $6.57/share)
- ✅ Multiple GTC orders filled automatically during market dips
- ✅ Portfolio restructured: eliminated leverage-decay ETFs, concentrated into conviction winners

Built on 12+ proven trading theories (O'Neil distribution days, Minervini VCP, market structure HH/HL/LL/LH, wheel strategy, institutional flow analysis, theme lifecycle detection) and inspired by [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills).

---

## How the Growth Engine Works

The system compounds your portfolio through 4 simultaneous growth sources:

| Source | Est. Annual | How It Works |
|--------|-------------|-------------|
| **Market appreciation** | ~12% | Hold quality compounders (AI, mega-caps) |
| **Swing accumulation** | ~8% | Trim high / rebuy low → more shares without new cash |
| **Option income** | ~3-5% | Monthly CC/CSP premiums reduce cost basis toward $0 |
| **Capital rotation** | ~3% | Sell dead money → redeploy to winners |
| **Combined** | **~25-30%** | 4 engines working simultaneously |

---

## Quick Start

```bash
git clone https://github.com/anthropics/stocksTrading.git  # or your fork
cd stocksTrading
pip install -r requirements.txt

# Set up your goals (copy templates and edit)
cp templates/financial_goal_template.yaml state/progress/financial_goal.yaml
cp templates/goals_template.yaml state/holdings/goals.yaml
cp templates/tracker_template.yaml state/progress/tracker.yaml

# Launch Claude Code
claude
```

Then type any command: `/daily`, `/status`, `/check AAPL`, etc.

---

## Setup Guide (For New Users)

### Step 1: Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/stocksTrading.git
cd stocksTrading
pip install -r requirements.txt  # yfinance + pyyaml
```

### Step 2: Configure Your Financial Goal

```bash
cp templates/financial_goal_template.yaml state/progress/financial_goal.yaml
```

Edit `state/progress/financial_goal.yaml`:
```yaml
goal:
  target_value: 1000000        # ← Your target (e.g., $1M)
  start_value: 500000          # ← Your current portfolio value
  target_date: "2028-12-31"    # ← Your deadline
  timeline_years: 2.5          # ← Years to achieve
```

### Step 3: Set Your Accumulation Goals

```bash
cp templates/goals_template.yaml state/holdings/goals.yaml
```

Edit `state/holdings/goals.yaml` — add your stocks:
```yaml
AAPL:
  strategy: swing_and_accumulate  # or: accumulate, ambush, hold
  target_shares: 200              # How many shares you want to own
  tier: CORE                      # CORE, GROWTH, or SATELLITE
  notes: "My top conviction stock"
```

### Step 4: Initialize the Progress Tracker

```bash
cp templates/tracker_template.yaml state/progress/tracker.yaml
```

Edit the `accumulation_goals` section to match your `goals.yaml`, and set your initial `cash_flow` numbers.

### Step 5: (Optional) Set Up Cost Basis Tracking

```bash
cp templates/adjusted_costs_template.yaml state/cost_basis/adjusted_costs.yaml
```

Add your stocks with their cost basis. Claude will update this automatically as you report option trades.

### Step 6: Import Your Holdings

Place your brokerage export CSV in the appropriate folder:
- Fidelity: `data/fidelity/` (Positions CSV export)
- Robinhood: `data/robinhood/` (Activity CSV or monthly PDF statements)

Then run `/weekly` to import and reconcile.

### Step 7: Start Using!

```bash
claude
```

```
/status          ← See your dashboard
/daily           ← Get today's signals
/check AAPL      ← Quick analysis on any stock
/discover NVDA GOOGL META  ← Compare and rank stocks
```

---

## Template Files Explained

All templates are in the `templates/` folder with extensive comments explaining every field:

| Template | Copy To | Purpose |
|----------|---------|---------|
| `goals_template.yaml` | `state/holdings/goals.yaml` | Define which stocks to accumulate and targets |
| `tracker_template.yaml` | `state/progress/tracker.yaml` | Track swing cycles, GTC orders, cash flow |
| `financial_goal_template.yaml` | `state/progress/financial_goal.yaml` | Set your $1M (or any) financial target |
| `adjusted_costs_template.yaml` | `state/cost_basis/adjusted_costs.yaml` | Track option income → adjusted cost per share |

### YAML Tips for Beginners

```yaml
# Strings: use quotes for dates and text
started: "2026-05-15"
notes: "My investment thesis"

# Numbers: no quotes
target_shares: 500
current_price: 220.50

# Lists: use dash + space
history:
  - date: "2026-05-15"
    event: "First purchase"
  - date: "2026-06-01"
    event: "Added more shares"

# Nested objects: indent with 2 spaces
trim:
  date: "2026-05-15"
  shares: 17
  price: 213.10
```

### What Claude Auto-Updates vs What You Edit

| File | You Edit | Claude Updates |
|------|----------|---------------|
| `goals.yaml` | ✅ Add new stocks, change targets | ✅ Updates shares_gained_swing |
| `tracker.yaml` | ✅ Initial setup only | ✅ Everything (cycles, orders, cash) |
| `financial_goal.yaml` | ✅ Goal target, start value | ✅ progress_log, milestones |
| `adjusted_costs.yaml` | ✅ Initial cost basis | ✅ Option income entries |
| `state/actions/*.md` | ❌ Don't edit | ✅ Written every /daily, /weekly |
| `state/theses/*.md` | ✅ Write your reasoning | ✅ Claude may suggest updates |

---

## Commands (11 Total)

| Command | Purpose | Frequency |
|---------|---------|-----------|
| **`/status`** | Unified dashboard: goal progress, adjusted costs, all trackers | Anytime |
| **`/daily`** | Market scan + swing signals + CC alerts + position builds + independent reasoning | Daily |
| **`/weekly`** | Portfolio import, discrepancy check, week review + next week outlook | Weekly |
| **`/check TICKER`** | Quick swing signal with catalyst + thesis check | On-demand |
| **`/plan TICKER`** | Detailed swing accumulation plan with exact math | On-demand |
| **`/evaluate TICKER`** | Full go/no-go analysis for new stock candidates | On-demand |
| **`/discover [args]`** | Multi-stock comparison, theme research, watchlist ranking | On-demand |
| **`/cleanup`** | Identify sell candidates + redeploy to position builds | Monthly |
| **`/cc`** | Covered call + cash-secured put analysis | After rallies |
| **`/positions`** | All GTC orders dashboard: gaps, adjustments, fill probability | Weekly+ |
| **`/positions adjust`** | Recommend which GTC to raise/lower/cancel | After big moves |

### Natural Language (also works)
```
"what should I do today?"    "check NBIS"        "should I trim META?"
"evaluate PLTR"              "compare RKLB vs IONQ"   "how am I doing?"
"discover theme:quantum"     "sell options analysis"   "update portfolio"
```

---

## Core Strategies

### 1. Swing Accumulation (Grow Shares Without New Cash)

Score each holding 0-10 based on: RSI, distance from 20-MA, volume, proximity to 52w high, rally duration.

| Score | Action |
|-------|--------|
| 8-10 | Trim 30% — sell and set rebuy orders |
| 6-7 | Trim 20% |
| 4-5 | Trim 10% (optional) |
| 0-3 | Hold |

**Catalyst modifiers** adjust thresholds (news, geopolitics, earnings timing).
**Market structure** (HH/HL/LL/LH) validates whether dips are "buy the dip" or "dead cat bounce."

### 2. Covered Calls & Cash-Secured Puts (Monthly Income)

**Philosophy: CONSERVATIVE — 白赚premium, 不贪.**

| Strategy | When | What | Result |
|----------|------|------|--------|
| Sell CC | After stock rallies (RSI >60) | Far OTM call (15-30%) | Collect $300-1000/month per stock |
| Sell CSP | While waiting for GTC fill | Put below GTC price | "Paid GTC" — earn income while waiting |

Goal: Reduce cost basis toward **zero cost** (free shares) within 6-12 months per stock.

### 3. Position Building (Systematic Entry)

GTC limit orders at technical support levels. The system:
- Scans all GTC daily for gap-to-fill
- Flags orders within 5% ("APPROACHING")
- Flags stale orders >15% away ("ADJUST")
- Monitors market conditions (distribution days) to gate new buys

### 4. Market Analysis (Independent Reasoning)

Every `/daily` and `/weekly` includes:
- **Wave thesis validation** (GPU → Memory → Optical → Quantum → Networking)
- **Distribution day monitoring** (IBD method — pause buys at HIGH/SEVERE)
- **Market top detection** (6-component composite scoring)
- **Breadth analysis** (broad participation vs narrow rally)
- **Second-order reasoning** (event → implication → who benefits)
- **Theme lifecycle** (Emerging → Accelerating → Trending → Mature → Exhausting)

---

## Skills (14 Decision Frameworks)

| Skill | Purpose |
|-------|---------|
| `financial-goal-planner` | Master objective: $1M target, milestones, strategy |
| `exposure-coach` | Market posture gate + distribution days + top detection |
| `position-sizer` | Risk-based sizing (1% max risk per trade) |
| `market-scanner` | Daily regime classification + breadth analysis |
| `swing-accumulator` | Score-based trim/rebuy logic + catalyst modifiers |
| `technical-analyst` | Market structure (HH/HL/LL/LH), VCP patterns, S/R, volume |
| `news-catalyst-analyst` | Second-order reasoning, geopolitics, precedent matching |
| `covered-call-strategy` | CC + CSP rules, strike selection, wheel strategy |
| `stock-evaluator` | 5-question screen + deep analysis + institutional flow |
| `stock-discovery` | Multi-stock ranking, theme lifecycle, wave detection |
| `portfolio-tracker` | CSV import, reconciliation, performance metrics |
| `portfolio-cleanup` | 4-question test for sell candidates |
| `scenario-analyzer` | Event-driven 3-scenario probability analysis |
| `signal-postmortem` | Learning loop: classify outcomes, feed back improvements |

---

## External Data Sources

| Category | Source | Used For |
|----------|--------|----------|
| **Prices/Technicals** | yfinance (free) | Prices, MAs, RSI, volume |
| **Holdings** | Fidelity/Robinhood CSV exports | Portfolio state |
| **Market News** | stockanalysis.com, web search | Daily/weekly reasoning |
| **Economic Calendar** | tradingeconomics.com | PCE, CPI, Fed dates |
| **Sector Analysis** | finviz.com, semianalysis.com | Heatmap, AI chip trends |
| **Fed/Rates** | CME FedWatch | Rate probabilities |
| **Sentiment** | YouTube: @RhinoFinance, @财经观察站 | Chinese financial analysis |
| **Institutional** | 13F filings (quarterly) | Smart money validation |
| **Charts** | User-provided screenshots (TradingView) | Visual technical analysis |

---

## State Tracking System

```
state/
├── holdings/
│   ├── current.yaml          ← Latest positions (from CSV import)
│   └── goals.yaml            ← Accumulation targets (NBIS→500, GOOGL→300, etc.)
├── progress/
│   ├── tracker.yaml          ← Swing cycles, GTC orders, cash flow, builds
│   └── financial_goal.yaml   ← $1M milestone tracking + progress log
├── cost_basis/
│   └── adjusted_costs.yaml   ← Option income → adjusted cost per share → path to zero
├── actions/
│   └── [daily/weekly/cleanup/plan/evaluate]_YYYY-MM-DD.md  ← Action trackers
├── theses/
│   └── [ticker]_[thesis].md  ← Investment reasoning (photonics wave, etc.)
├── discovery/
│   ├── watchlist.yaml        ← Ranked candidates, watchlist, themes tracked
│   └── analysis_*.md         ← Deep analysis records
└── journal/
    └── YYYY-MM-DD.md         ← Daily trade journals with links to action docs
```

### How It All Connects

```
You type /daily
  → Claude loads CLAUDE.md (project context)
  → Reads .claude/commands/daily.md (instructions)
  → Reads ALL skills (14 frameworks)
  → Reads state/ files (your positions, goals, orders)
  → Fetches external data (news, prices)
  → Applies reasoning (wave thesis, distribution days, market structure)
  → Produces: signal table + swing opportunities + GTC status + CC signals + new ideas
  → Writes state/actions/daily_YYYY-MM-DD.md (tracks suggestions)
  → You say "I sold 24 NBIS" → tracker updated automatically
```

---

## Directory Structure

```
stocksTrading/
├── .claude/
│   ├── commands/              ← 11 slash commands (auto-registered)
│   └── settings.local.json   ← Permissions
├── CLAUDE.md                  ← Project context (auto-loaded every session)
├── README.md                  ← This file
├── skills/                    ← 14 decision frameworks
├── scripts/                   ← Python utilities (fetch, import, report)
├── state/                     ← All persistent data
├── data/                      ← Raw CSV/PDF imports (gitignored)
│   ├── fidelity/
│   ├── robinhood/
│   └── others_opinions/       ← Future: YouTube transcript crawls
├── reports/                   ← Generated CSV/MD reports (gitignored)
├── workflows/                 ← YAML workflow definitions
└── requirements.txt           ← Python dependencies (yfinance, pyyaml)
```

---

## Trading Theories Incorporated

| Theory | Source | Applied In |
|--------|--------|-----------|
| Swing Accumulation (trim high, rebuy low) | Custom | swing-accumulator skill |
| Market Structure (HH/HL/LL/LH Trend Flip) | Price Action theory | technical-analyst skill |
| VCP (Volatility Contraction Pattern) | Mark Minervini | technical-analyst skill |
| Distribution Day Counting | William O'Neil / IBD | exposure-coach skill |
| Market Top Detection (6-component) | Monty/O'Neil/Minervini blend | exposure-coach skill |
| Breadth Analysis (Uptrend Ratio) | Market internals | market-scanner skill |
| Catalyst Modifiers (news override) | Custom | news-catalyst-analyst skill |
| Theme Lifecycle (Emerging→Exhausting) | Sector rotation theory | stock-discovery skill |
| Institutional Flow (13F analysis) | SEC filings | stock-evaluator skill |
| Wheel Strategy (CC + CSP cycle) | Options income | covered-call-strategy skill |
| Position Sizing (Fixed Fractional + Kelly) | Risk management | position-sizer skill |
| Wave Theory (GPU→Memory→Optical→Quantum) | Custom AI infra thesis | theses/ + all commands |

---

## Option Income Strategy

**Goal: Reduce cost basis to ZERO on core holdings.**

```
How it works (example):
  Stock cost: $50/share, 200 shares = $10,000 total cost
  Sell 1 covered call/month: ~$500 premium
  After 20 months: $10,000 collected → COST BASIS = $0 (FREE shares!)

Monthly income scales with portfolio size:
  $500K portfolio: ~$1,500-2,500/month CC/CSP income
  $1M portfolio:   ~$3,000-5,000/month
  $1.5M portfolio: ~$5,000-8,000/month → can cover living expenses → FIRE!
```

---

## Tips

- **Trust the system**: If the score says hold, hold. Rules > emotions.
- **Provide charts**: Screenshot TradingView charts for visual technical analysis.
- **Report actions**: Tell Claude what you did ("I sold 24 NBIS") → tracker updates automatically.
- **Weekly imports**: Drop fresh CSVs weekly for accurate tracking.
- **Don't chase**: If stock runs past your GTC, let it go. Next opportunity always comes.
- **Sell the losers**: Dead money in EOSE/GLXY = dollars not working toward your goal.
- **CC on green days**: Sell covered calls after rallies (RSI >60), not on red days.

---

## Disclaimer

This is a personal decision-support tool, not financial advice. All outputs are recommendations requiring manual execution. Never auto-executes trades. You are responsible for your own investment decisions.

---

## Credits

- Framework inspired by [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)
- Powered by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) by Anthropic
- Market data via [yfinance](https://github.com/ranaroussi/yfinance) (free)
