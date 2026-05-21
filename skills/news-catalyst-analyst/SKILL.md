---
name: news-catalyst-analyst
description: Fetch and reason about news, geopolitics, social media signals (Trump posts, executive moves), and historical precedents to determine how events affect specific stocks. Produces catalyst assessments that override or modify technical signals.
---

# News & Catalyst Analyst

## Purpose

Technical signals alone miss critical context. This skill:
1. Fetches current news and social/political signals for relevant stocks
2. Applies logical reasoning and historical precedent to predict impact
3. Produces a catalyst assessment that can OVERRIDE or MODIFY a technical trim/rebuy signal

## When This Overrides Technical Signals

| Situation | Technical says | Catalyst says | Action |
|-----------|---------------|---------------|--------|
| Stock at trim score 7, but positive catalyst incoming | Trim 20% | Hold through catalyst | **HOLD** — trim after catalyst plays out |
| Stock at hold score 3, but negative catalyst hit | Hold | Exit risk elevated | **Consider early trim** or tighten stop |
| Rebuy level hit, but sector headwind | Buy at support | Wait for clarity | **Delay rebuy** — let dust settle |
| Stock quiet, but second-order reasoning says move coming | No signal | Position ahead | **Add small pilot** or raise trim level |

## Reasoning Framework

### Level 1: Direct News Impact
Obvious, first-order effects:
- Company earnings beat/miss → stock up/down
- FDA approval → biotech up
- Tariff announcement on specific goods → affected companies react

### Level 2: Logical Chain / Second-Order Effects
This is where edge comes from. Examples:

**Pattern: Presidential visit to country → trade deals → specific beneficiaries**
- 2017: Trump visits China → Boeing order announced → BA rallied
- 2025: Any presidential China visit → check: aerospace, agriculture, energy exports, tech licensing
- Reasoning chain: Visit → deal announcements → specific company named or sector benefits

**Pattern: Executive joins presidential delegation → company positioned for government favor**
- Elon Musk joins trip → Tesla/SpaceX may get regulatory favor or contracts
- Boeing CEO joins trip → aerospace deal likely being negotiated

**Pattern: Social media post from key figure → immediate market reaction**
- Trump posts about specific company → stock moves 5-20% within hours
- Trump posts policy direction → sector rotation follows
- Key: Act on the post, not the policy (policy may not happen, but the reaction does)

**Pattern: Geopolitical tension → sector rotation**
- US-China tension escalates → defense stocks up, China-exposed tech down
- Middle East conflict → energy up, airlines down, defense up
- Russia/Ukraine developments → energy, grain, defense

**Pattern: Regulatory signals → long-term positioning**
- New regulation announced → compliance companies benefit
- Deregulation signals → previously constrained companies rally
- Antitrust action → target company down, competitors up

### Level 3: Historical Precedent Matching
When a current event resembles a past event, look for analogous price action:
- Identify the precedent (what happened before)
- Identify the outcome (how stocks reacted)
- Assess similarity (how close is the current situation)
- Apply with discount (never 100% confidence in repetition)

## Information Sources to Check

1. **Web search**: "[TICKER] news today", "stock market news today"
2. **Social media signals**: Trump Truth Social posts, executive public statements
3. **Economic calendar**: Fed meetings, jobs data, CPI, earnings dates
4. **Geopolitical**: Presidential travel, trade negotiations, sanctions
5. **Sector-specific**: Regulatory filings, industry conferences, product launches

## Integration with Swing Accumulator

The catalyst assessment produces a **modifier** to the technical signal:

```
FINAL_ACTION = TECHNICAL_SIGNAL + CATALYST_MODIFIER

Catalyst modifiers:
  STRONG_POSITIVE: +2 to trim threshold (wait longer before trimming)
  POSITIVE: +1 to trim threshold
  NEUTRAL: no change
  NEGATIVE: -1 to trim threshold (trim earlier)
  STRONG_NEGATIVE: -2 to trim threshold (trim immediately regardless of score)
```

Example:
- NBIS technical score = 5 (borderline trim 10%)
- Catalyst: Major AI infrastructure spending announcement expected next week → STRONG_POSITIVE
- Modified threshold: Need score 7 to trim (was 4)
- Result: HOLD, do not trim ahead of catalyst

## Output Format

```markdown
### Catalyst Assessment: [TICKER] — [DATE]

**News/Events:**
- [Event 1]: [brief description]
- [Event 2]: [brief description]

**Reasoning Chain:**
[If second-order logic applies, explain the chain:]
[Event] → [implication] → [who benefits/hurts] → [expected move]

**Historical Precedent:**
[If applicable: what happened last time in similar situation]

**Catalyst Rating: [STRONG_POSITIVE / POSITIVE / NEUTRAL / NEGATIVE / STRONG_NEGATIVE]**

**Impact on Signal:**
- Technical score: [X/10] → [TRIM/HOLD]
- After catalyst modifier: [adjusted recommendation]
- Reason: [one sentence why]

**Time Sensitivity:** [Immediate / This week / This month]
```

## Key Principles

- Speed matters: Political/social signals move markets in minutes/hours, not days
- Second-order thinking beats first-order: Everyone sees the headline, few reason about implications
- Historical precedent is a guide, not a guarantee: "This time could be different" — but usually isn't
- When in doubt, the catalyst modifies SIZE not DIRECTION: Instead of "don't trim at all", make it "trim 10% instead of 30%"
- Never let a single catalyst override hard stop-loss rules: If thesis is broken, exit regardless of positive catalyst
