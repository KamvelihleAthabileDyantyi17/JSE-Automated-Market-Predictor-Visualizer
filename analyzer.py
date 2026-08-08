import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker_symbol):
    print(f"Fetching data for {ticker_symbol}...")

    #Create a Ticker object for the given stock symbol
    stock = yf.Ticker(ticker_sysmbol)

    #fetch historical market data for the stock(1 month, daily interval)
    history_data =stock.history(period="1mo", interval="1d")
    return history_data

# Main Execution
if __name__ == "__main__":
    # .JO tells yfinance to look at the Johannesburg Stock Exchange
    my_ticker = "SBK.JO" 
    
    raw_data = fetch_stock_data(my_ticker)
    
    # Print the last 5 days of data to the console
    print("\n--- Last 5 Days of Market Data ---")
    print(raw_data.tail(5))