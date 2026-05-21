---
name: scenario-analyzer
description: When a major news event hits (Fed decision, trade war, geopolitical crisis), analyze 3 probability-weighted scenarios (Base/Bull/Bear) with sector impacts and specific stock picks. Integrates with news-catalyst-analyst for deeper event analysis.
---

# Scenario Analyzer

## Purpose

When a market-moving event occurs, don't react emotionally. Instead:
1. Define 3 scenarios with probabilities
2. Map sector/stock impacts for each
3. Determine optimal positioning across all scenarios
4. Identify "no-regret" moves (actions that work in 2+ scenarios)

## When to Use

- Major Fed announcement or surprise
- Geopolitical escalation/de-escalation
- Major earnings surprise from market bellwether
- Policy change (tariffs, regulation, tax)
- Black swan events

## Framework

### Step 1: Event Classification
| Type | Examples | Time Horizon |
|------|----------|--------------|
| Monetary | Rate hike/cut, QE/QT change | 3-6 months |
| Geopolitical | War, trade deal, sanctions | 6-18 months |
| Regulatory | Antitrust, new laws, deregulation | 6-12 months |
| Tech disruption | New AI breakthrough, platform shift | 12-36 months |
| Commodity | Oil shock, supply disruption | 3-12 months |

### Step 2: Three Scenarios (must sum to 100%)

| Scenario | Typical Weight | Definition |
|----------|---------------|------------|
| Base | 50-60% | Most likely outcome given historical precedent |
| Bull | 20-30% | Upside surprise — event better than expected |
| Bear | 15-25% | Downside — event worse than expected or second-order damage |

### Step 3: Impact Mapping

For each scenario, identify:
- **1st order**: Direct impact (company named, sector targeted)
- **2nd order**: Implication chain (if X then Y benefits/hurts)
- **3rd order**: Non-obvious winner/loser (what everyone misses)

### Step 4: No-Regret Moves

Actions that are good in 2+ scenarios:
- "If it's bullish OR neutral, this stock wins" → safe to buy
- "If it's bearish OR neutral, raising cash is right" → trim regardless
- "Only works in bull case" → risky, size smaller

## Integration with Financial Goal

Rate each scenario's impact on your $1M goal:
- Base case: stays on track
- Bull case: accelerates timeline
- Bear case: how far behind does it put you? Can you recover?

Choose actions that protect the goal in the bear case while participating in the base/bull case.

## Output Format

```markdown
## Scenario Analysis: [EVENT] — [DATE]

### Event: [description]
### Classification: [type]

| Scenario | Probability | S&P Impact | Your Portfolio Impact |
|----------|-------------|-----------|---------------------|
| Base | 55% | [range] | [description] |
| Bull | 25% | [range] | [description] |
| Bear | 20% | [range] | [description] |

### No-Regret Moves
1. [Action that works in 2+ scenarios]
2. [Action that works in 2+ scenarios]

### Holdings Impact
| Ticker | Base | Bull | Bear | Action |
|--------|------|------|------|--------|
```
