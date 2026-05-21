"""
Import holdings from Fidelity and Robinhood CSV exports.
Normalizes data and updates state/holdings/current.yaml
"""

import csv
import os
import yaml
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
STATE_DIR = PROJECT_ROOT / "state" / "holdings"
ARCHIVE_DIR_SUFFIX = "archive"


def parse_fidelity_csv(filepath: str) -> list[dict]:
    """Parse Fidelity Positions CSV export."""
    positions = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            symbol = row.get("Symbol")
            if symbol is None:
                continue
            symbol = symbol.strip()
            if not symbol:
                continue
            # Skip money market, cash, pending, options, disclaimer rows
            if symbol.endswith("**") or symbol.startswith("Pending"):
                continue
            if symbol.startswith("-"):
                continue
            # Skip rows that look like disclaimers or non-stock (no quantity)
            quantity_raw = row.get("Quantity")
            if quantity_raw is None:
                continue
            quantity_str = quantity_raw.replace(",", "").strip()
            if not quantity_str:
                continue
            try:
                quantity = float(quantity_str)
            except ValueError:
                continue
            if quantity <= 0:
                continue

            account_name = row.get("Account Name", "Fidelity")
            account_num = row.get("Account Number", "")
            account_label = f"Fidelity-{account_name}"

            positions.append({
                "ticker": symbol,
                "shares": quantity,
                "avg_cost": _parse_dollar(row.get("Average Cost Basis", "0")),
                "current_price": _parse_dollar(row.get("Last Price", "0")),
                "market_value": _parse_dollar(row.get("Current Value", "0")),
                "unrealized_pnl": _parse_dollar(row.get("Total Gain/Loss Dollar", "0")),
                "unrealized_pnl_pct": _parse_pct(row.get("Total Gain/Loss Percent", "0")),
                "cost_basis_total": _parse_dollar(row.get("Cost Basis Total", "0")),
                "account": account_label,
                "account_number": account_num,
            })
    return positions


def parse_robinhood_csv(filepath: str) -> list[dict]:
    """Parse Robinhood positions/statement CSV export.
    Supports both positions format and activity/transaction history format.
    If the file is an activity log, compute net stock positions from Buy/Sell transactions.
    """
    positions = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        # Detect if this is an activity log (has "Trans Code" column) vs positions export
        if "Trans Code" in headers or "Activity Date" in headers:
            return _parse_robinhood_activity(filepath)

        for row in reader:
            symbol_raw = row.get("Symbol", row.get("Instrument"))
            if symbol_raw is None:
                continue
            symbol = symbol_raw.strip()
            if not symbol:
                continue
            quantity_raw = row.get("Quantity", "0")
            if quantity_raw is None:
                continue
            quantity_str = quantity_raw.replace(",", "")
            try:
                quantity = float(quantity_str)
            except ValueError:
                continue
            if quantity == 0:
                continue

            positions.append({
                "ticker": symbol,
                "shares": quantity,
                "avg_cost": _parse_dollar(row.get("Average Cost", "0")),
                "current_price": _parse_dollar(row.get("Current Price", row.get("Last Price", "0"))),
                "market_value": _parse_dollar(row.get("Market Value", row.get("Equity", "0"))),
                "unrealized_pnl": _parse_dollar(row.get("Unrealized P&L", row.get("Total Return", "0"))),
                "unrealized_pnl_pct": _parse_pct(row.get("Unrealized P&L %", row.get("Total Return %", "0"))),
                "account": "Robinhood",
            })
    return positions


def _parse_robinhood_activity(filepath: str) -> list[dict]:
    """Parse Robinhood activity/transaction CSV and compute net stock positions."""
    from collections import defaultdict
    net = defaultdict(lambda: {"shares": 0, "cost": 0})

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            instrument = (row.get("Instrument") or "").strip()
            desc = (row.get("Description") or "").strip()
            trans = (row.get("Trans Code") or "").strip()
            qty_str = (row.get("Quantity") or "").strip()
            price_str = (row.get("Price") or "").replace("$", "").replace(",", "").strip()

            if not instrument or not trans:
                continue
            # Only process stock Buy/Sell (skip options BTO/STO/STC/BTC/OEXP)
            if trans not in ("Buy", "Sell"):
                continue
            # Skip options described in the Description field
            if "Call" in desc or "Put" in desc:
                continue

            try:
                qty = float(qty_str)
                price = float(price_str) if price_str else 0
            except ValueError:
                continue

            if trans == "Buy":
                net[instrument]["shares"] += qty
                net[instrument]["cost"] += qty * price
            elif trans == "Sell":
                net[instrument]["shares"] -= qty
                net[instrument]["cost"] -= qty * price

    positions = []
    for ticker, data in sorted(net.items()):
        if data["shares"] > 0.01:
            avg_cost = data["cost"] / data["shares"] if data["shares"] > 0 else 0
            positions.append({
                "ticker": ticker,
                "shares": data["shares"],
                "avg_cost": round(avg_cost, 2),
                "current_price": 0,
                "market_value": 0,
                "unrealized_pnl": 0,
                "unrealized_pnl_pct": 0,
                "account": "Robinhood",
            })
    return positions


def consolidate_positions(fidelity: list[dict], robinhood: list[dict]) -> dict:
    """Merge positions across brokers into consolidated view."""
    by_ticker = {}

    for pos in fidelity + robinhood:
        ticker = pos["ticker"]
        if ticker not in by_ticker:
            by_ticker[ticker] = {
                "ticker": ticker,
                "positions": [],
                "total_shares": 0,
                "total_cost": 0,
                "total_value": 0,
            }
        by_ticker[ticker]["positions"].append(pos)
        by_ticker[ticker]["total_shares"] += pos["shares"]
        by_ticker[ticker]["total_cost"] += pos["shares"] * pos["avg_cost"]
        by_ticker[ticker]["total_value"] += pos["market_value"]

    consolidated = []
    for ticker, data in sorted(by_ticker.items()):
        avg_cost = data["total_cost"] / data["total_shares"] if data["total_shares"] > 0 else 0
        pnl = data["total_value"] - data["total_cost"]
        pnl_pct = (pnl / data["total_cost"] * 100) if data["total_cost"] > 0 else 0
        consolidated.append({
            "ticker": ticker,
            "total_shares": data["total_shares"],
            "weighted_avg_cost": round(avg_cost, 4),
            "total_value": round(data["total_value"], 2),
            "total_pnl": round(pnl, 2),
            "total_pnl_pct": round(pnl_pct, 2),
            "accounts": [p["account"] for p in data["positions"]],
        })

    return consolidated


def load_previous_state() -> dict | None:
    """Load previous holdings state for comparison."""
    state_file = STATE_DIR / "current.yaml"
    if state_file.exists():
        with open(state_file) as f:
            return yaml.safe_load(f)
    return None


def save_state(fidelity: list[dict], robinhood: list[dict], consolidated: list[dict]):
    """Save current holdings state."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "accounts": {
            "fidelity": fidelity,
            "robinhood": robinhood,
        },
        "consolidated": consolidated,
    }
    state_file = STATE_DIR / "current.yaml"
    with open(state_file, "w") as f:
        yaml.dump(state, f, default_flow_style=False, sort_keys=False)
    print(f"State saved to {state_file}")


def detect_changes(previous: dict | None, current_consolidated: list[dict]) -> list[str]:
    """Compare current vs previous state and report changes."""
    if previous is None:
        return ["First import — no previous state to compare."]

    changes = []
    prev_tickers = {p["ticker"]: p for p in previous.get("consolidated", [])}
    curr_tickers = {p["ticker"]: p for p in current_consolidated}

    for ticker in curr_tickers:
        if ticker not in prev_tickers:
            changes.append(f"NEW: {ticker} — {curr_tickers[ticker]['total_shares']} shares")

    for ticker in prev_tickers:
        if ticker not in curr_tickers:
            changes.append(f"CLOSED: {ticker} — was {prev_tickers[ticker]['total_shares']} shares")

    for ticker in curr_tickers:
        if ticker in prev_tickers:
            curr = curr_tickers[ticker]
            prev = prev_tickers[ticker]
            share_diff = curr["total_shares"] - prev["total_shares"]
            if abs(share_diff) > 0.01:
                direction = "ADDED" if share_diff > 0 else "REDUCED"
                changes.append(f"{direction}: {ticker} — {share_diff:+.0f} shares (now {curr['total_shares']:.0f})")

    return changes if changes else ["No changes detected."]


def archive_csv(filepath: str, broker: str):
    """Move processed CSV to archive directory."""
    archive_dir = DATA_DIR / broker / ARCHIVE_DIR_SUFFIX
    archive_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = Path(filepath).stem
    dest = archive_dir / f"{filename}_{timestamp}.csv"
    os.rename(filepath, dest)
    print(f"Archived: {filepath} → {dest}")


def import_all():
    """Main import routine: find CSVs, parse, consolidate, save."""
    fidelity_dir = DATA_DIR / "fidelity"
    robinhood_dir = DATA_DIR / "robinhood"

    fidelity_positions = []
    robinhood_positions = []

    # Parse Fidelity CSVs
    if fidelity_dir.exists():
        for csv_file in sorted(fidelity_dir.glob("*.csv")):
            if ARCHIVE_DIR_SUFFIX in str(csv_file):
                continue
            print(f"Parsing Fidelity: {csv_file.name}")
            fidelity_positions.extend(parse_fidelity_csv(str(csv_file)))

    # Parse Robinhood CSVs
    if robinhood_dir.exists():
        for csv_file in sorted(robinhood_dir.glob("*.csv")):
            if ARCHIVE_DIR_SUFFIX in str(csv_file):
                continue
            print(f"Parsing Robinhood: {csv_file.name}")
            robinhood_positions.extend(parse_robinhood_csv(str(csv_file)))

    if not fidelity_positions and not robinhood_positions:
        print("No CSV files found in data/fidelity/ or data/robinhood/")
        print("Export your positions from your broker and place the CSV here.")
        return

    # Consolidate
    consolidated = consolidate_positions(fidelity_positions, robinhood_positions)

    # Detect changes
    previous = load_previous_state()
    changes = detect_changes(previous, consolidated)

    print("\n--- Changes Detected ---")
    for change in changes:
        print(f"  {change}")

    # Save state
    save_state(fidelity_positions, robinhood_positions, consolidated)

    # Print summary
    total_value = sum(p["total_value"] for p in consolidated)
    print(f"\n--- Portfolio Summary ---")
    print(f"Positions: {len(consolidated)}")
    print(f"Total Value: ${total_value:,.2f}")
    print(f"\nTop holdings:")
    for pos in sorted(consolidated, key=lambda x: x["total_value"], reverse=True)[:10]:
        print(f"  {pos['ticker']:6} | {pos['total_shares']:8.1f} shares | ${pos['total_value']:>10,.2f} | {pos['total_pnl_pct']:>+6.1f}%")

    # Archive processed CSVs
    if fidelity_dir.exists():
        for csv_file in fidelity_dir.glob("*.csv"):
            if ARCHIVE_DIR_SUFFIX not in str(csv_file):
                archive_csv(str(csv_file), "fidelity")
    if robinhood_dir.exists():
        for csv_file in robinhood_dir.glob("*.csv"):
            if ARCHIVE_DIR_SUFFIX not in str(csv_file):
                archive_csv(str(csv_file), "robinhood")


def _parse_dollar(value: str) -> float:
    """Parse dollar amount string to float."""
    if not value:
        return 0.0
    cleaned = value.replace("$", "").replace(",", "").replace("+", "").strip()
    if cleaned in ("--", "n/a", ""):
        return 0.0
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def _parse_pct(value: str) -> float:
    """Parse percentage string to float."""
    if not value:
        return 0.0
    cleaned = value.replace("%", "").replace("+", "").strip()
    if cleaned in ("--", "n/a", ""):
        return 0.0
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


if __name__ == "__main__":
    import_all()
