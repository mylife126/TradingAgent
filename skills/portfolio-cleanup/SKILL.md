---
name: portfolio-cleanup
description: Review all holdings to identify candidates for selling (dead money, broken thesis, better use of capital). For each position, research current fundamentals/news/catalysts and apply reasoning to determine if the stock still has potential or should be sold to free up cash. Trigger when user asks "what should I sell", "clean up portfolio", "free up cash", or "which stocks are bad".
---

# Portfolio Cleanup

## Purpose

Identify holdings that should be sold — not because they're down, but because:
1. The original thesis is broken (fundamentals deteriorated)
2. The capital is dead money (no catalyst, no growth, just sitting there losing)
3. Better opportunities exist and cash is limited
4. Tax-loss harvesting benefit outweighs holding

## Framework: The 4-Question Test

For EACH position, answer:

1. **If you didn't own it, would you buy it today at this price?**
   - If NO → strong sell candidate
   - If YES → hold

2. **Is there a credible catalyst in the next 6 months?**
   - Earnings inflection, product launch, regulatory change, partnership
   - If NO → dead money, consider selling

3. **Is the thesis that made you buy it still intact?**
   - Revenue growing? Management executing? Competitive position strong?
   - If thesis is BROKEN → sell regardless of loss

4. **Is this capital better deployed elsewhere?**
   - Compare: expected return here vs. putting it into your #1 conviction (NBIS)
   - Opportunity cost is real

## Scoring

| Score | Meaning | Action |
|-------|---------|--------|
| 4/4 YES | Strong hold | Keep, possibly add |
| 3/4 YES | Hold | Keep, monitor |
| 2/4 YES | Weak hold | Consider trimming |
| 1/4 YES | Sell candidate | Sell, redeploy |
| 0/4 YES | Dead money | Sell immediately |

## Research Requirements

For each holding being evaluated:
- Web search for recent news, earnings, analyst coverage
- Check if revenue/earnings are growing or declining
- Look for upcoming catalysts or thesis-breaking events
- Compare against the user's original thesis (if saved in state/theses/)
- Apply second-order reasoning: is the sector/theme still favorable?

## Output Format

```markdown
## Portfolio Cleanup — [DATE]

### Sell Candidates (free up cash)
| Ticker | Shares | P&L | Score | Reason | Cash Freed |
|--------|--------|-----|-------|--------|-----------|

### Weak Holds (monitor closely)
| Ticker | Shares | P&L | Score | Concern | Trigger to Sell |

### Strong Holds (keep or add)
| Ticker | Shares | P&L | Score | Why Keep |

### Recommended Actions
1. SELL [X] — [reason] — redeploy $[Y] to [Z]
2. ...

### Tax Impact Note
- Short-term losses that offset gains
- Long-term losses to carry forward
```

## Action Tracking Integration

After completing the cleanup analysis:
1. Write all suggested actions to `state/actions/cleanup_YYYY-MM-DD.md` with status tracking
2. Each action gets a status: SUGGESTED / EXECUTED / SKIPPED / PARTIAL / CANCELLED
3. Link the action tracker from the day's journal entry
4. When the user reports executing an action, update both:
   - The action tracker file (status -> EXECUTED with details)
   - `state/progress/tracker.yaml` (shares, cash flow, accumulation goals)
5. Cross-reference with tracker.yaml to ensure redeployment suggestions account for:
   - Cash already committed to pending orders
   - Accumulation goals that need funding
   - Open swing cycles that may need rebuy cash

## Key Principles

- Being down doesn't automatically mean sell — thesis matters more than P&L
- Being up doesn't automatically mean hold — overvalued winners should be trimmed
- Every dollar in a dead stock is a dollar NOT working toward your goals
- Tax-loss harvesting is valid — sell the loser, buy something better, offset gains from NBIS trim
- Always present the "do nothing" option with its cost (opportunity cost of holding dead money)
