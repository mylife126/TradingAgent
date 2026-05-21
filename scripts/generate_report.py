"""
Generate portfolio performance reports and update the tracking spreadsheet.
Outputs CSV for easy viewing in Excel/Google Sheets.
"""

import csv
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
STATE_DIR = PROJECT_ROOT / "state" / "holdings"
REPORTS_DIR = PROJECT_ROOT / "reports"


def load_holdings() -> dict | None:
    state_file = STATE_DIR / "current.yaml"
    if not state_file.exists():
        print("No holdings state found. Run import_holdings.py first.")
        return None
    with open(state_file) as f:
        return yaml.safe_load(f)


def load_goals() -> dict:
    """Load accumulation goals if defined."""
    goals_file = STATE_DIR / "goals.yaml"
    if goals_file.exists():
        with open(goals_file) as f:
            return yaml.safe_load(f) or {}
    return {}


def generate_summary_csv(holdings: dict, goals: dict):
    """Generate/update the master portfolio CSV spreadsheet."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_file = REPORTS_DIR / "portfolio_summary.csv"

    consolidated = holdings.get("consolidated", [])
    total_value = sum(p.get("total_value", 0) for p in consolidated)

    rows = []
    for pos in sorted(consolidated, key=lambda x: x.get("total_value", 0), reverse=True):
        ticker = pos["ticker"]
        goal_info = goals.get(ticker, {})
        target_shares = goal_info.get("target_shares", "")
        progress = ""
        if target_shares:
            progress = f"{pos['total_shares'] / target_shares * 100:.1f}%"

        weight = (pos.get("total_value", 0) / total_value * 100) if total_value > 0 else 0

        rows.append({
            "Ticker": ticker,
            "Shares": pos["total_shares"],
            "Avg Cost": f"${pos['weighted_avg_cost']:.2f}",
            "Current Price": "",  # filled by fetch_price_data
            "Market Value": f"${pos.get('total_value', 0):,.2f}",
            "Unrealized P&L ($)": f"${pos.get('total_pnl', 0):,.2f}",
            "Unrealized P&L (%)": f"{pos.get('total_pnl_pct', 0):+.2f}%",
            "Weight (%)": f"{weight:.1f}%",
            "Accounts": ", ".join(pos.get("accounts", [])),
            "Goal": goal_info.get("strategy", ""),
            "Target Shares": target_shares,
            "Progress": progress,
            "Shares Gained (Swing)": goal_info.get("shares_gained_swing", 0),
        })

    fieldnames = [
        "Ticker", "Shares", "Avg Cost", "Current Price", "Market Value",
        "Unrealized P&L ($)", "Unrealized P&L (%)", "Weight (%)",
        "Accounts", "Goal", "Target Shares", "Progress", "Shares Gained (Swing)"
    ]

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Portfolio summary written to {output_file}")
    print(f"  Positions: {len(rows)}")
    print(f"  Total Value: ${total_value:,.2f}")
    return output_file


def generate_weekly_report(holdings: dict, goals: dict) -> str:
    """Generate a markdown weekly performance report."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = REPORTS_DIR / f"weekly_review_{date_str}.md"

    consolidated = holdings.get("consolidated", [])
    total_value = sum(p.get("total_value", 0) for p in consolidated)
    total_cost = sum(p.get("total_shares", 0) * p.get("weighted_avg_cost", 0) for p in consolidated)
    total_pnl = total_value - total_cost
    total_pnl_pct = (total_pnl / total_cost * 100) if total_cost > 0 else 0

    lines = [
        f"# Weekly Portfolio Review — {date_str}\n",
        f"## Summary",
        f"- **Total Value**: ${total_value:,.2f}",
        f"- **Total Cost Basis**: ${total_cost:,.2f}",
        f"- **Total P&L**: ${total_pnl:,.2f} ({total_pnl_pct:+.1f}%)",
        f"- **Positions**: {len(consolidated)}",
        f"",
        f"## Holdings",
        f"| Ticker | Shares | Avg Cost | Value | P&L % | Weight |",
        f"|--------|--------|----------|-------|-------|--------|",
    ]

    for pos in sorted(consolidated, key=lambda x: x.get("total_value", 0), reverse=True):
        weight = (pos.get("total_value", 0) / total_value * 100) if total_value > 0 else 0
        lines.append(
            f"| {pos['ticker']} | {pos['total_shares']:.0f} | "
            f"${pos['weighted_avg_cost']:.2f} | "
            f"${pos.get('total_value', 0):,.0f} | "
            f"{pos.get('total_pnl_pct', 0):+.1f}% | "
            f"{weight:.1f}% |"
        )

    # Accumulation progress
    if goals:
        lines.extend([
            f"",
            f"## Accumulation Progress",
            f"| Ticker | Current | Target | Progress | Swing Gains |",
            f"|--------|---------|--------|----------|-------------|",
        ])
        for ticker, goal in goals.items():
            pos = next((p for p in consolidated if p["ticker"] == ticker), None)
            if pos:
                current = pos["total_shares"]
                target = goal.get("target_shares", "?")
                progress = f"{current / target * 100:.0f}%" if isinstance(target, (int, float)) else "?"
                swing_gains = goal.get("shares_gained_swing", 0)
                lines.append(f"| {ticker} | {current:.0f} | {target} | {progress} | +{swing_gains} |")

    lines.extend([
        f"",
        f"## Action Items",
        f"- [ ] Review swing levels for overextended positions",
        f"- [ ] Check for upcoming earnings on holdings",
        f"- [ ] Update accumulation goals if needed",
        f"",
        f"---",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
    ])

    content = "\n".join(lines)
    with open(output_file, "w") as f:
        f.write(content)

    print(f"Weekly report written to {output_file}")
    return str(output_file)


if __name__ == "__main__":
    holdings = load_holdings()
    if holdings is None:
        sys.exit(1)

    goals = load_goals()
    generate_summary_csv(holdings, goals)
    generate_weekly_report(holdings, goals)
