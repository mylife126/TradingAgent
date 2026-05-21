Review all holdings to identify sell candidates, dead money, and broken theses.

Usage: /cleanup

Steps:
1. ALWAYS read state/holdings/current.yaml to get all positions with exact shares, cost, P&L
2. ALWAYS read state/holdings/goals.yaml to understand which positions are strategic vs. opportunistic
3. ALWAYS read state/progress/tracker.yaml for accumulation progress, pending orders, and cash flow context
4. ALWAYS read all files in state/theses/ to understand the original reasoning behind each position
5. Read skills/portfolio-cleanup/SKILL.md for the 4-question evaluation framework
6. Read skills/news-catalyst-analyst/SKILL.md for catalyst reasoning
7. For EACH individual stock position (skip index funds unless user asks):
   a. Use web search to check: current revenue/earnings trajectory, recent news, analyst sentiment, upcoming catalysts
   b. Apply the 4-question test (would you buy today? catalyst ahead? thesis intact? better use of capital?)
   c. Score 0-4 and categorize as: Sell / Weak Hold / Strong Hold
8. Apply second-order reasoning: is the sector/theme still alive? Has something structurally changed?
9. Calculate total cash that could be freed by selling the candidates
10. Suggest where to redeploy that cash (toward existing goals or better opportunities)
11. Note tax implications: short-term vs long-term losses, potential to offset gains (e.g., NBIS trim gains)

## Position Build Redeployment (REQUIRED)

11b. ALWAYS read state/actions/position_build_plan_2026-05-18.md (or most recent build plan).
11c. When suggesting where to redeploy freed cash, PRIORITIZE active position builds that are closest to their buy alert triggers:
    - Calculate: for each build target, how close is current price to the limit?
    - Rank redeployment targets by: (1) proximity to filling, (2) conviction level (Tier 1 > Tier 2 > Tier 3)
    - Example: "Sell PGY ($2,469) → redeploy to GOOGL (only 7% away from $370 target) or COHR (only 6% away from $340)"
11d. If cleanup frees significant cash (>$5,000), reassess whether any position build should be UPGRADED (larger position, higher limit price, or additional tranche).

Present results as: sell candidates table -> weak holds table -> strong holds table -> specific action plan with redeployment mapped to position builds.

## Action Tracker (REQUIRED)

12. After presenting the analysis, ALWAYS write an action tracker file to `state/actions/cleanup_YYYY-MM-DD.md` with the following format:

```markdown
# Cleanup Action Tracker — YYYY-MM-DD

## Summary
- Sell candidates: N positions, ~$X total
- Weak holds: N positions
- Strong holds: N positions
- Cash to redeploy: $X

## Actions

### Sells
| # | Action | Ticker | Shares | Est. Proceeds | Status | Updated |
|---|--------|--------|--------|---------------|--------|---------|
| 1 | SELL | XXXX | NN | $X,XXX | SUGGESTED | YYYY-MM-DD |

### Redeployments
| # | Action | Ticker | Shares | Est. Cost | Status | Updated |
|---|--------|--------|--------|-----------|--------|---------|
| 1 | BUY | XXXX | NN | $X,XXX | SUGGESTED | YYYY-MM-DD |

### Other Actions
| # | Action | Details | Status | Updated |
|---|--------|---------|--------|---------|
| 1 | REVIEW | Re-check XXXX thesis in 2 weeks | SUGGESTED | YYYY-MM-DD |
```

Status values: SUGGESTED / EXECUTED / SKIPPED / PARTIAL / CANCELLED

13. After writing the action tracker, update today's journal entry (state/journal/YYYY-MM-DD.md) to include a link:
    - Add a section: `## Cleanup Review` with `Action tracker: [state/actions/cleanup_YYYY-MM-DD.md]`

14. Tell the user: "Action tracker saved to state/actions/cleanup_YYYY-MM-DD.md. As you execute actions, tell me (e.g., 'I sold QBTS' or 'skip the ONDS sell') and I'll update the tracker status."

## Tracking User Confirmations

When the user later says they executed an action (e.g., "I sold QBTS", "I bought 15 META", "skip the ONDS sell"):
1. Read the most recent cleanup action tracker from state/actions/
2. Update the matching action's Status to EXECUTED (with fill details if provided) or SKIPPED
3. Update the "Updated" column with today's date
4. If the action affects share counts, also update state/progress/tracker.yaml:
   - Update accumulation_goals current_shares
   - Update position_builds filled_tranches
   - Update cash_flow estimates
   - Add a history entry
5. Save both files
