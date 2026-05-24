Analyze covered call AND cash-secured put opportunities.

Usage: /cc (analyzes both CC and CSP opportunities)

Philosophy: CONSERVATIVE — collect premium safely, not greedy. Prefer far OTM, low assignment risk.
If assigned on CC: sold high, that's above-market profit. If assigned on CSP: bought low, even better.

Steps:
1. Read state/holdings/current.yaml — find all positions with 100+ shares
2. Read state/cost_basis/adjusted_costs.yaml — current adjusted cost, option income history
3. Read state/progress/tracker.yaml — check if any swing cycles active on same shares
4. Read skills/covered-call-strategy/SKILL.md — rules for when/what/how to sell CC
5. Run `python3 scripts/fetch_price_data.py` on all CC-eligible tickers for RSI, price, MAs
6. For each eligible ticker, check CC signal conditions:
   a. RSI > 60? (rally happened, premium is fat)
   b. Not within 7 days of earnings?
   c. Not in active swing trim (don't CC shares you're about to sell)?
   d. Distance from last CC > 14 days?
   e. Score ≤ 5? (if score 6+, recommend swing trim instead)
7. For tickers that pass all conditions:
   a. Calculate recommended strike (10-15% OTM for moderate, 5-10% for aggressive)
   b. Estimate premium (use stock price × delta × volatility approximation)
   c. Calculate impact on adjusted cost basis
   d. Show "if assigned" outcome (still profitable? how much gain?)
8. Present: opportunity table + specific contract recommendations + cost impact

Output:
```markdown
## Covered Call Analysis — [DATE]

### CC-Eligible Holdings
| Ticker | Shares | Coverable | RSI | Score | Last CC | Signal? |
[all stocks with 100+ shares]

### Today's Recommendations
| # | Ticker | Action | Strike | Expiry | Est Premium | Delta | Cost Reduction |
| 1 | NBIS | SELL 1 CALL | $XXX | XX/XX | ~$XXX | 0.XX | -$X.XX/share |

### If Assigned (Worst Case)
| Ticker | Strike | Your Adj Cost | Profit if Called | Acceptable? |
[show that being assigned is still a profitable outcome]

### Cost Basis Impact
| Ticker | Before CC | After CC | Months to Zero |

### Integration with Swing
[Note if any conflicts with open swing cycles]
```

## Tracking

When user confirms they sold a CC:
1. Update state/cost_basis/adjusted_costs.yaml — add to option_income
2. Recalculate adjusted_cost_per_share and months_to_zero_cost
3. Note in journal and action tracker
4. Set reminder: expiry date of the sold call (track if assigned or expired)

When CC expires worthless:
1. Celebrate — pure income, shares retained
2. Check if conditions met to sell another CC (wait 14 days minimum)

When CC is assigned (shares called away):
1. Update holdings (reduce shares by 100)
2. Record as: premium income + stock sale profit
3. Update accumulation goals (shares reduced)
4. If applicable: use cash to buy shares back on next dip (similar to swing rebuy)

## Cash-Secured Put Analysis (ALSO REQUIRED)

After CC analysis, also check CSP opportunities:

9. Read state/holdings/goals.yaml — find stocks user is BUILDING positions in
10. For each build target with pending GTC orders (GOOGL, META, APP, LLY, IONQ, MSTR):
    a. Is the stock above the user's GTC buy price? (yes = CSP opportunity)
    b. Is RSI > 30? (not in freefall)
    c. Does user have margin/cash to support the put?
11. Recommend puts at or slightly BELOW the GTC buy price:
    - Strike = GTC price - 5% (even more conservative entry)
    - Expiry: 30 days
    - This is a "paid GTC" — get the same entry OR BETTER, plus collect premium

Present CSP opportunities after CC section:
```markdown
### Cash-Secured Put Opportunities
| Ticker | Your GTC | Suggested Put Strike | Expiry | Est Premium | If Assigned |
| GOOGL | BUY@$370 | SELL PUT $350 | 30d | ~$300-500 | Buy 100sh@$350 (better than GTC!) + keep premium |

### Margin Impact
| Put | Margin Required | Current Available | Feasible? |
```

## Tracking CSPs

When user sells a put:
1. Update state/cost_basis/adjusted_costs.yaml — add premium to income
2. Track expiry date
3. If assigned: update holdings, recalculate costs, update goals
4. If expires worthless: pure income, reset for next cycle
