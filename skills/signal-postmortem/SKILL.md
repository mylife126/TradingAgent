---
name: signal-postmortem
description: After a swing cycle completes or a position is closed, analyze what worked and what didn't. Classify outcomes, identify patterns, and feed learnings back into the system. Run during /weekly review for any completed cycles.
---

# Signal Postmortem

## Purpose

Close the learning loop. After every completed trade/cycle, ask:
1. Did it work as planned?
2. Why or why not?
3. What should we do differently next time?

## Outcome Classification

| Category | Definition | Action |
|----------|-----------|--------|
| TRUE_POSITIVE | Trim signal was correct, stock pulled back, rebuys filled | Reinforce: keep using same thresholds |
| FALSE_POSITIVE | Trim signal fired but stock never pulled back — missed upside | Adjust: raise trim threshold, or add capitulation rebuy sooner |
| MISSED_OPPORTUNITY | Didn't trim but should have (stock crashed after score was high) | Adjust: lower trim threshold, be more decisive |
| REGIME_MISMATCH | Signal was right individually but macro shift overwhelmed it | Note: regime changed, not a skill failure. Integrate exposure-coach. |

## Postmortem Template

```markdown
## Postmortem: [TICKER] Cycle [N] — [DATE]

### What Happened
- Trim: [shares] @ [price] on [date]
- Rebuy L1: [filled/unfilled] @ [price]
- Rebuy L2: [filled/unfilled] @ [price]
- Net result: [+X shares / -X shares / flat]

### Classification: [TRUE_POSITIVE / FALSE_POSITIVE / MISSED / REGIME_MISMATCH]

### What Worked
- [specific observation]

### What Didn't Work
- [specific observation]

### Lesson for Next Cycle
- [actionable adjustment]

### Score Card
- Share gain: [+N or -N]
- Dollar gain: [$X]
- Days to complete cycle: [N]
- Goal impact: [moved from X% to Y% toward 500 shares]
```

## When to Run

- Every /weekly: check if any swing cycles completed (rebuys filled or capitulation triggered)
- When user reports closing a position
- Monthly: review all signals given vs. outcomes

## Integration with Financial Goal

Track cumulative swing gains over time:
- Total shares gained from all completed cycles
- Dollar value of those gains at current prices
- Contribution to CAGR (swing gains as % of portfolio growth)
