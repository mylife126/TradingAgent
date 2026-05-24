"""
Distribution Day Monitor (IBD / O'Neil Method)
Calculates distribution day counts for SPY and QQQ.

A Distribution Day = index closes down ≥0.2% on volume higher than previous day.
Removal: 25 sessions elapse OR index gains 5% from the DD close.

Usage:
    python3 scripts/distribution_days.py
    python3 scripts/distribution_days.py --json  (for machine-readable output)

Output:
    Risk level: NORMAL / CAUTION / HIGH / SEVERE
    d5, d15, d25 counts for SPY and QQQ
    Recommendation for swing accumulation
"""

import sys
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings("ignore")

try:
    import yfinance as yf
except ImportError:
    print("Error: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

try:
    import yaml
except ImportError:
    yaml = None


def get_distribution_days(ticker: str, lookback_days: int = 60) -> dict:
    """Calculate distribution days for a given index ETF."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period=f"{lookback_days + 10}d")

    if hist.empty or len(hist) < 30:
        return {"error": f"Insufficient data for {ticker}"}

    # Calculate daily changes
    hist["pct_change"] = hist["Close"].pct_change()
    hist["vol_change"] = hist["Volume"] > hist["Volume"].shift(1)
    hist["is_dd"] = (hist["pct_change"] <= -0.002) & (hist["vol_change"])

    # Get distribution days within last 25 trading sessions
    recent = hist.tail(26)  # 25 sessions + 1 for volume comparison
    recent_25 = recent.tail(25)

    # Check for 5% rally removal (a DD is "healed" if index rallied 5% from that day)
    current_close = float(hist["Close"].iloc[-1])
    active_dds = []

    for idx, row in recent_25.iterrows():
        if row["is_dd"]:
            dd_close = float(row["Close"])
            # Check if index has rallied 5% from this DD
            if (current_close - dd_close) / dd_close < 0.05:
                active_dds.append({
                    "date": idx.strftime("%Y-%m-%d"),
                    "close": round(dd_close, 2),
                    "pct_change": round(float(row["pct_change"]) * 100, 2),
                    "healed": False,
                })
            else:
                active_dds.append({
                    "date": idx.strftime("%Y-%m-%d"),
                    "close": round(dd_close, 2),
                    "pct_change": round(float(row["pct_change"]) * 100, 2),
                    "healed": True,
                })

    # Count active (unhealed) DDs in windows
    unhealed = [dd for dd in active_dds if not dd["healed"]]

    # Window counts
    last_5_sessions = recent_25.tail(5)
    last_15_sessions = recent_25.tail(15)

    d5 = sum(1 for dd in unhealed if dd["date"] >= last_5_sessions.index[0].strftime("%Y-%m-%d"))
    d15 = sum(1 for dd in unhealed if dd["date"] >= last_15_sessions.index[0].strftime("%Y-%m-%d"))
    d25 = len(unhealed)

    # Check if index is below key MAs
    ma50 = float(hist["Close"].rolling(50).mean().iloc[-1]) if len(hist) >= 50 else current_close
    ma21 = float(hist["Close"].rolling(21).mean().iloc[-1]) if len(hist) >= 21 else current_close
    below_50ma = current_close < ma50
    below_21ema = current_close < ma21

    return {
        "ticker": ticker,
        "current_close": round(current_close, 2),
        "d5": d5,
        "d15": d15,
        "d25": d25,
        "total_dds_in_window": len(active_dds),
        "active_unhealed": d25,
        "below_50ma": below_50ma,
        "below_21ema": below_21ema,
        "ma50": round(ma50, 2),
        "distribution_days": unhealed,
    }


def classify_risk(spy_data: dict, qqq_data: dict) -> dict:
    """Classify overall market risk based on distribution day counts."""

    spy_d5 = spy_data.get("d5", 0)
    spy_d15 = spy_data.get("d15", 0)
    spy_d25 = spy_data.get("d25", 0)
    qqq_d5 = qqq_data.get("d5", 0)
    qqq_d15 = qqq_data.get("d15", 0)
    qqq_d25 = qqq_data.get("d25", 0)
    qqq_below_50 = qqq_data.get("below_50ma", False)
    spy_below_50 = spy_data.get("below_50ma", False)

    # Determine individual risk levels
    def ticker_risk(d5, d15, d25, below_50):
        if d25 >= 6 or d15 >= 4 or (below_50 and d25 >= 5):
            return "SEVERE"
        elif d25 >= 5 or d15 >= 3 or d5 >= 2:
            return "HIGH"
        elif d25 >= 3:
            return "CAUTION"
        else:
            return "NORMAL"

    spy_risk = ticker_risk(spy_d5, spy_d15, spy_d25, spy_below_50)
    qqq_risk = ticker_risk(qqq_d5, qqq_d15, qqq_d25, qqq_below_50)

    # Overall risk (QQQ-weighted for growth stocks)
    risk_order = ["NORMAL", "CAUTION", "HIGH", "SEVERE"]
    spy_idx = risk_order.index(spy_risk)
    qqq_idx = risk_order.index(qqq_risk)

    # QQQ SEVERE or HIGH = overall at least that level
    if qqq_idx >= 3:  # SEVERE
        overall = "SEVERE"
    elif qqq_idx >= 2:  # HIGH
        overall = "HIGH"
    elif spy_idx >= 3:  # SPY SEVERE
        overall = "SEVERE"
    elif spy_idx >= 2:  # SPY HIGH
        overall = "HIGH"
    else:
        overall = risk_order[max(spy_idx, qqq_idx)]

    # Action recommendation
    actions = {
        "NORMAL": "Full-size swing buys OK. Normal operations.",
        "CAUTION": "Reduce swing buy size by 25%. Tighten stops.",
        "HIGH": "⚠️ PAUSE all new buys. Tighten stops. Watch for follow-through.",
        "SEVERE": "🔴 ACTIVELY reduce exposure. Sell weakest holdings. Cash priority.",
    }

    # Exposure multiplier
    exposure = {
        "NORMAL": 1.0,
        "CAUTION": 0.75,
        "HIGH": 0.50,
        "SEVERE": 0.25,
    }

    return {
        "overall_risk": overall,
        "spy_risk": spy_risk,
        "qqq_risk": qqq_risk,
        "action": actions[overall],
        "exposure_multiplier": exposure[overall],
        "spy": spy_data,
        "qqq": qqq_data,
    }


def main():
    json_mode = "--json" in sys.argv

    print("Fetching distribution day data...")
    spy_data = get_distribution_days("SPY")
    qqq_data = get_distribution_days("QQQ")

    if "error" in spy_data or "error" in qqq_data:
        print(f"Error: {spy_data.get('error', '')} {qqq_data.get('error', '')}")
        sys.exit(1)

    result = classify_risk(spy_data, qqq_data)

    if json_mode and yaml:
        print(yaml.dump(result, default_flow_style=False, sort_keys=False))
    else:
        print()
        print("═══ DISTRIBUTION DAY MONITOR ═══")
        print()
        print(f"  SPY: d5={spy_data['d5']}, d15={spy_data['d15']}, d25={spy_data['d25']} | "
              f"Risk: {result['spy_risk']} | Close: ${spy_data['current_close']} | "
              f"{'BELOW 50-MA' if spy_data['below_50ma'] else 'Above 50-MA'}")
        print(f"  QQQ: d5={qqq_data['d5']}, d15={qqq_data['d15']}, d25={qqq_data['d25']} | "
              f"Risk: {result['qqq_risk']} | Close: ${qqq_data['current_close']} | "
              f"{'BELOW 50-MA' if qqq_data['below_50ma'] else 'Above 50-MA'}")
        print()
        print(f"  ═══ OVERALL: {result['overall_risk']} ═══")
        print(f"  Exposure multiplier: {result['exposure_multiplier']:.0%}")
        print(f"  Action: {result['action']}")
        print()

        if spy_data["distribution_days"]:
            print("  Recent Distribution Days (SPY):")
            for dd in spy_data["distribution_days"][-5:]:
                print(f"    {dd['date']}: {dd['pct_change']:+.2f}%")

        if qqq_data["distribution_days"]:
            print("  Recent Distribution Days (QQQ):")
            for dd in qqq_data["distribution_days"][-5:]:
                print(f"    {dd['date']}: {dd['pct_change']:+.2f}%")


if __name__ == "__main__":
    main()
