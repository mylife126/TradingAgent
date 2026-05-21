"""
Fetch current price data and technical indicators for holdings.
Uses yfinance (free, no API key required).
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
STATE_DIR = PROJECT_ROOT / "state" / "holdings"


def get_holdings_tickers() -> list[str]:
    """Load tickers from current holdings state."""
    state_file = STATE_DIR / "current.yaml"
    if not state_file.exists():
        print("No holdings state found. Run import_holdings.py first.")
        return []
    with open(state_file) as f:
        state = yaml.safe_load(f)
    return [p["ticker"] for p in state.get("consolidated", [])]


def fetch_stock_data(ticker: str, period: str = "6mo") -> dict | None:
    """Fetch price history and compute technical indicators."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        if hist.empty:
            return None

        current = hist["Close"].iloc[-1]
        prev_close = hist["Close"].iloc[-2] if len(hist) > 1 else current

        # Moving averages
        ma20 = hist["Close"].rolling(20).mean().iloc[-1] if len(hist) >= 20 else None
        ma50 = hist["Close"].rolling(50).mean().iloc[-1] if len(hist) >= 50 else None
        ma200 = hist["Close"].rolling(200).mean().iloc[-1] if len(hist) >= 200 else None

        # RSI(14)
        rsi = _compute_rsi(hist["Close"], 14)

        # Average volume (20-day)
        avg_vol_20 = hist["Volume"].rolling(20).mean().iloc[-1] if len(hist) >= 20 else hist["Volume"].mean()
        today_vol = hist["Volume"].iloc[-1]
        vol_ratio = today_vol / avg_vol_20 if avg_vol_20 > 0 else 1.0

        # Price vs MAs
        pct_above_20ma = ((current - ma20) / ma20 * 100) if ma20 else None
        pct_above_50ma = ((current - ma50) / ma50 * 100) if ma50 else None

        # Consecutive up/down days
        consecutive_up = 0
        for i in range(len(hist) - 1, 0, -1):
            if hist["Close"].iloc[i] > hist["Close"].iloc[i - 1]:
                consecutive_up += 1
            else:
                break

        # 52-week high/low
        hist_1y = stock.history(period="1y")
        high_52w = hist_1y["High"].max() if not hist_1y.empty else None
        low_52w = hist_1y["Low"].min() if not hist_1y.empty else None

        return {
            "ticker": ticker,
            "current_price": float(round(current, 2)),
            "prev_close": float(round(prev_close, 2)),
            "daily_change_pct": float(round((current - prev_close) / prev_close * 100, 2)),
            "ma20": float(round(ma20, 2)) if ma20 else None,
            "ma50": float(round(ma50, 2)) if ma50 else None,
            "ma200": float(round(ma200, 2)) if ma200 else None,
            "pct_above_20ma": float(round(pct_above_20ma, 2)) if pct_above_20ma else None,
            "pct_above_50ma": float(round(pct_above_50ma, 2)) if pct_above_50ma else None,
            "rsi_14": float(round(rsi, 2)) if rsi else None,
            "volume_today": int(today_vol),
            "volume_avg_20": int(avg_vol_20),
            "volume_ratio": float(round(vol_ratio, 2)),
            "consecutive_up_days": int(consecutive_up),
            "high_52w": float(round(high_52w, 2)) if high_52w else None,
            "low_52w": float(round(low_52w, 2)) if low_52w else None,
            "pct_from_52w_high": float(round((current - high_52w) / high_52w * 100, 2)) if high_52w else None,
        }
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None


def compute_swing_score(data: dict) -> dict:
    """Compute swing accumulator signal score (0-10)."""
    score = 0
    details = []

    # Price vs 20-MA (0-2)
    pct = data.get("pct_above_20ma")
    if pct is not None:
        if pct > 10:
            score += 2
            details.append(f"Price vs 20MA: 2pts ({pct:+.1f}% above)")
        elif pct > 5:
            score += 1
            details.append(f"Price vs 20MA: 1pt ({pct:+.1f}% above)")
        else:
            details.append(f"Price vs 20MA: 0pts ({pct:+.1f}%)")

    # RSI (0-2)
    rsi = data.get("rsi_14")
    if rsi is not None:
        if rsi > 70:
            score += 2
            details.append(f"RSI(14): 2pts ({rsi:.1f})")
        elif rsi > 60:
            score += 1
            details.append(f"RSI(14): 1pt ({rsi:.1f})")
        else:
            details.append(f"RSI(14): 0pts ({rsi:.1f})")

    # Volume (0-2)
    vol_ratio = data.get("volume_ratio", 1.0)
    if vol_ratio > 2.0:
        score += 2
        details.append(f"Volume: 2pts ({vol_ratio:.1f}x avg)")
    elif vol_ratio > 1.5:
        score += 1
        details.append(f"Volume: 1pt ({vol_ratio:.1f}x avg)")
    else:
        details.append(f"Volume: 0pts ({vol_ratio:.1f}x avg)")

    # Proximity to 52-week high (proxy for resistance) (0-2)
    pct_from_high = data.get("pct_from_52w_high")
    if pct_from_high is not None:
        if pct_from_high > -2:
            score += 2
            details.append(f"Near 52w high: 2pts ({pct_from_high:+.1f}%)")
        elif pct_from_high > -5:
            score += 1
            details.append(f"Near 52w high: 1pt ({pct_from_high:+.1f}%)")
        else:
            details.append(f"Near 52w high: 0pts ({pct_from_high:+.1f}%)")

    # Consecutive up days (0-2)
    consec = data.get("consecutive_up_days", 0)
    if consec >= 5:
        score += 2
        details.append(f"Rally duration: 2pts ({consec} days)")
    elif consec >= 3:
        score += 1
        details.append(f"Rally duration: 1pt ({consec} days)")
    else:
        details.append(f"Rally duration: 0pts ({consec} days)")

    return {"score": score, "max_score": 10, "details": details}


def _compute_rsi(prices, period: int = 14) -> float | None:
    """Compute RSI for a price series."""
    if len(prices) < period + 1:
        return None
    deltas = prices.diff()
    gains = deltas.where(deltas > 0, 0.0)
    losses = (-deltas).where(deltas < 0, 0.0)
    avg_gain = gains.rolling(period).mean().iloc[-1]
    avg_loss = losses.rolling(period).mean().iloc[-1]
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def scan_all_holdings():
    """Scan all holdings and print swing scores."""
    tickers = get_holdings_tickers()
    if not tickers:
        return

    print(f"Scanning {len(tickers)} holdings — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    print(f"{'Ticker':<8} {'Price':>8} {'Chg%':>7} {'RSI':>6} {'vs20MA':>7} {'VolR':>6} {'Score':>6} {'Signal':<12}")
    print("-" * 72)

    results = []
    for ticker in tickers:
        data = fetch_stock_data(ticker)
        if data is None:
            print(f"{ticker:<8} — fetch failed")
            continue
        swing = compute_swing_score(data)
        signal = "TRIM 30%" if swing["score"] >= 8 else "TRIM 20%" if swing["score"] >= 6 else "TRIM 10%" if swing["score"] >= 4 else "HOLD"
        print(f"{ticker:<8} {data['current_price']:>8.2f} {data['daily_change_pct']:>+6.1f}% {data.get('rsi_14', 0):>5.1f} {data.get('pct_above_20ma', 0):>+6.1f}% {data.get('volume_ratio', 0):>5.1f}x {swing['score']:>4}/10  {signal:<12}")
        results.append({**data, **swing})

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ticker = sys.argv[1].upper()
        print(f"Fetching data for {ticker}...\n")
        data = fetch_stock_data(ticker, period="1y")
        if data:
            swing = compute_swing_score(data)
            print(yaml.dump({**data, "swing_signal": swing}, default_flow_style=False))
        else:
            print(f"Could not fetch data for {ticker}")
    else:
        scan_all_holdings()
