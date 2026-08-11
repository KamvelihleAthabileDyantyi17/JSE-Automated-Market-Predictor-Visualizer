import json
import os
import pandas as pd
import yfinance as yf

def load_config(config_path="src/config.json"):
    """Reads project settings and ticker lists from config.json."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    with open(config_path, "r") as f:
        return json.load(f)

def analyze_ticker(ticker_symbol, short_w=50, long_w=200, period="1y"):
    """Fetches market data for a ticker and calculates technical signals."""
    print(f"[+] Fetching & analyzing: {ticker_symbol}")
    stock = yf.Ticker(ticker_symbol)
    df = stock.history(period=period, interval="1d")
    
    if df.empty:
        print(f"[-] No data found for {ticker_symbol}")
        return None

    # Calculate Moving Averages using core Pandas
    df['SMA_50'] = df['Close'].rolling(window=short_w).mean()
    df['SMA_200'] = df['Close'].rolling(window=long_w).mean()
    
    # Calculate RSI (14-day Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI_14'] = 100 - (100 / (1 + rs))

    # Drop incomplete calculation rows
    df = df.dropna()

    if df.empty:
        print(f"[-] Insufficient historical data for indicators on {ticker_symbol}")
        return None

    # Latest indicator evaluation
    latest_row = df.iloc[-1]
    close_price = round(latest_row['Close'], 2)
    sma_50 = round(latest_row['SMA_50'], 2)
    sma_200 = round(latest_row['SMA_200'], 2)
    rsi_14 = round(latest_row['RSI_14'], 2)

    # Determine Signal
    if sma_50 > sma_200 and rsi_14 < 70:
        signal = "Strong Buy"
    elif rsi_14 < 30:
        signal = "Oversold (Buy Watch)"
    elif rsi_14 > 70:
        signal = "Overbought (Risk)"
    else:
        signal = "Hold"

    return {
        "Ticker": ticker_symbol,
        "Close Price": close_price,
        "SMA 50": sma_50,
        "SMA 200": sma_200,
        "RSI (14)": rsi_14,
        "Signal": signal
    }

def run_analysis():
    """Main execution function iterating over configured tickers."""
    config = load_config()
    all_tickers = config["jse_tickers"] + config["us_tickers"]
    results = []

    print("=== Starting Market Predictor Analysis ===")
    for ticker in all_tickers:
        summary = analyze_ticker(
            ticker, 
            short_w=config["analysis_settings"]["short_window"],
            long_w=config["analysis_settings"]["long_window"],
            period=config["analysis_settings"]["period"]
        )
        if summary:
            results.append(summary)

    summary_df = pd.DataFrame(results)
    print("\n=== Final Market Summary ===")
    print(summary_df.to_string(index=False))
    return summary_df

if __name__ == "__main__":
    run_analysis()