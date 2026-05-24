---
name: covered-call-strategy
description: Systematically sell covered calls on eligible holdings to generate monthly income and reduce cost basis toward zero. Determines when to sell, what strike, what expiry, and how it integrates with swing cycles. Referenced by /daily (quick signal) and /cc (detailed analysis).
---

# Covered Call Strategy

## Purpose

Generate $2,000-3,000/month in option income by selling covered calls on stocks you hold 100+ shares of. This income reduces your cost basis, eventually reaching ZERO COST (free shares).

## Eligible Holdings (100+ shares required)

Check state/holdings/current.yaml for positions ≥ 100 shares:
- NBIS: 194 shares → can sell 1 contract
- GOOGL: 120.5 shares (Robinhood) → can sell 1 contract
- META: 146 shares → can sell 1 contract
- NVDA: 110.3 shares → can sell 1 contract

## When to Sell CC — Signal Conditions (ALL must be true)

1. **RSI > 60** — Stock has had a recent rally (premium is fat)
2. **Distance from last CC > 14 days** — Don't overlap contracts
3. **Not within 7 days before earnings** — IV crush risk after earnings
4. **Not in active swing trim** — If you're about to trim shares, don't also sell a call on the same shares
5. **Score ≤ 4** — Not yet at trim level (if score ≥ 6, do a swing trim instead, which is better)

If score is 4-5 (borderline): CC is BETTER than trim because:
- You collect premium regardless
- If stock keeps rising and gets called away = you trimmed at strike + collected premium
- If stock pulls back = you keep shares + keep premium + cost reduced

## User Philosophy: CONSERVATIVE — 白赚premium, 不贪

The user's core principle: "稍微保守一点，卖一个较高的位置。概率更低，真不幸被assign了也算超额收益。不要太激进。"

This means:
- ALWAYS prefer LOWER delta (further OTM) over higher premium
- Being assigned = still acceptable (selling high is fine) — but the GOAL is to keep shares
- Consistent small income > occasional big premium with high assignment risk
- Think of it as "monthly rent" from your stocks, not a gambling strategy

## Strike Selection Rules (CONSERVATIVE bias)

| Market Condition | Strike Distance | Delta Target | Approx Premium | Assignment Risk |
|-----------------|----------------|-------------|---------------|-----------------|
| Overextended (RSI 70-80) | +15-20% OTM | 0.15-0.20 delta | $400-800 | 10-15% (safe) |
| Uptrend (RSI 60-70) | +20-25% OTM | 0.10-0.15 delta | $200-500 | 5-10% (very safe) |
| Neutral (RSI 45-60) | +25-30% OTM | 0.05-0.10 delta | $100-300 | <5% (near-free money) |

**Key rule: If in doubt, go FURTHER OTM.** Less premium is fine — the goal is consistent income with minimal risk of losing shares.

## Expiry Selection

| Timeframe | Pros | Cons | When to use |
|-----------|------|------|-------------|
| **30 days (recommended)** | Best theta decay curve, good premium | Monthly management | Default choice |
| 14 days | Faster cycle, lower risk | Less premium per contract | After earnings, known catalyst passed |
| 45 days | Higher total premium | More time for stock to move against you | When you're very bullish and want far OTM |

## Integration with Swing Accumulator

| Scenario | Swing Says | CC Says | Best Action |
|----------|-----------|---------|-------------|
| Score 6+ | TRIM 20% | — | **TRIM** (swing takes priority) |
| Score 4-5 | Optional 10% trim | Sell CC | **SELL CC** (earn premium, let market decide) |
| Score 0-3 | HOLD | Wait for signal | **WAIT** (no CC when stock is weak/falling) |

Key Rule: **Never sell CC on shares you plan to swing-trim in the same cycle.** Pick one:
- Core shares (50%) → sell CC on these for income
- Swingable shares (50%) → use for trim/rebuy cycles

## Premium vs Cost Reduction Math

```
Example: NBIS 194 shares, sell 1 contract (100 shares covered)

Monthly CC income: ~$800 (avg across market conditions)
Annual: $800 × 12 = $9,600
Current adjusted cost: $40.31/share × 100 shares covered = $4,031

Months to zero cost on covered 100 shares: $4,031 ÷ $800 = 5 months!
```

## Risk Management

| Risk | Mitigation |
|------|-----------|
| Stock rockets past strike (miss upside) | Use 10-15% OTM strike. Accept that CC = income strategy, not max-gain strategy. |
| Stock crashes after selling CC | CC doesn't make crash worse — premium actually reduces your loss slightly. |
| Assigned early | Rare for American calls (only near ex-div). If it happens, you sold at profit + premium. Fine. |
| Can't sell underlying while CC active | True — your 100 shares are "locked." That's why use core shares, not swingable. |

## Output Format (for /cc command)

```markdown
## CC Opportunity — [DATE]

### Eligible Holdings
| Ticker | Shares | RSI | Score | Last CC | Signal |
[list which stocks qualify today]

### Recommendation
| Ticker | Action | Strike | Expiry | Est. Premium | Delta | If Assigned |
| NBIS | SELL 1 CALL | $XXX | MM/DD | ~$XXX | 0.XX | Sell 100sh @ $XXX + keep $XXX premium |

### Impact on Cost Basis
| Ticker | Current Adj Cost | After This CC | Progress to Zero |
```

---

# Cash-Secured Put (CSP) Strategy

## Purpose

Sell puts on stocks you WANT to own (accumulation targets). Two outcomes, both good:
- Put expires worthless → you keep premium (free income)
- Put is assigned → you buy the stock at a low price (which you wanted anyway!) + keep premium

## User Philosophy: Same as CC — CONSERVATIVE

- Sell puts at a price you'd be HAPPY to buy at (well below current)
- The goal is to collect premium while waiting for dips you already want
- If assigned = "I got my GTC fill AND got paid for waiting"

## When to Sell Puts — Signal Conditions

1. **Stock is on your accumulation/build list** (NBIS, GOOGL, APP, META, LLY, IONQ, MSTR)
2. **You have cash or margin to cover** (strike × 100 = cash needed if assigned)
3. **Stock is NOT in freefall** (RSI > 30, not crashing on thesis-breaking news)
4. **You would genuinely buy 100 shares at the strike price**
5. **No existing put already open on this ticker**

## Strike Selection (CONSERVATIVE)

| Scenario | Strike Location | Delta | Premium | Assignment Risk |
|----------|----------------|-------|---------|-----------------|
| Stock near your GTC buy price | At or slightly below GTC level | 0.20-0.30 | Moderate | 20-30% (acceptable — you wanted to buy here anyway) |
| Stock well above your buy target | 20-30% below current | 0.10-0.15 | Low-moderate | 10-15% (safe, near-free money) |
| After big drop (RSI <35) | At strong support level | 0.15-0.20 | High (IV elevated) | 15-20% (good timing — sell fear) |

**Key rule:** The strike price MUST be a price where you say "I'd happily buy 100 shares here." If you wouldn't, don't sell the put there.

## Integration with Position Builds

| If you have GTC order... | Put strategy... | Why |
|--------------------------|----------------|-----|
| BUY 15 GOOGL @ $370 | SELL 1 PUT GOOGL $360 (30 day) | If assigned: you buy 100sh @ $360 (even better than your $370 GTC!) + premium |
| BUY 30 IONQ @ $50 | SELL 1 PUT IONQ $45 (30 day) | If assigned: 100sh @ $45 (below your $50 GTC) + premium |
| BUY 10 META @ $590 | SELL 1 PUT META $570 (30 day) | If assigned: 100sh @ $570 (better than $590!) + premium |

**CSP is like a "paid GTC order"** — you get the same fill (or better) AND collect premium while waiting!

## Examples for Your Portfolio

```
NBIS (you already did this!):
  SOLD PUT $140 Jun 18 → collected $424
  If NBIS stays above $140 (extremely likely): free $424
  If NBIS crashes to $140: you buy 100 shares at $140 (amazing price for 500-share goal!)

Potential new puts:
  SELL PUT GOOGL $350 (30 day) → collect ~$300-500
  SELL PUT META $570 (30 day) → collect ~$400-700  
  SELL PUT APP $430 (30 day) → collect ~$200-400
```

## Margin Requirement

Selling a put requires either:
- **Cash-secured**: Full strike × 100 held in cash (e.g., $350 strike = $35,000 reserved)
- **Margin**: Broker only requires 20-30% (e.g., $350 strike = $7,000-10,500 reserved)

Your current situation: $18,300 already reserved for options. Be aware of how much additional margin each new put requires.

## Risk Management for Puts

| Risk | Mitigation |
|------|-----------|
| Stock crashes 50% below strike | Only sell puts on stocks with STRONG thesis (not speculative). |
| Assigned more shares than you want | Only sell 1 put per ticker. 100 shares max exposure per stock. |
| Multiple puts assigned simultaneously (crash) | Never have total put exposure > 30% of portfolio. |
| Premium not worth the risk | If premium < $200 for 30 days, skip it. Not worth tying up margin. |

## Combined Wheel Strategy (CC + CSP)

The full "wheel" cycle:
```
Phase 1: SELL PUT → collect premium while waiting to buy
Phase 2: GET ASSIGNED → now you own 100 shares at low price + kept premium  
Phase 3: SELL COVERED CALL → collect premium while holding
Phase 4: GET CALLED AWAY → sold shares at high price + kept premium
Phase 5: Back to Phase 1 (sell put again to re-enter)

Each rotation: you earn premium at EVERY step AND buy low / sell high.
```

---

## Tracking

When user sells a CC or CSP:
- Update state/cost_basis/adjusted_costs.yaml with new option income
- Add trade to option_income history  
- Recalculate adjusted_cost_per_share
- Update months_to_zero_cost
- Note in daily journal
- For CSPs: track expiry date and assignment status
