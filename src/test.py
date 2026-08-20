import yfinance as yf
import pandas as pd

print(" Fetching JSE market data...")

#Pulling naspers ltd (NPN.JO) to test the connection)
ticker = yf.Ticker("NPN.JO")
history = ticker.history(period="5d")

print("\nLast 5 trading days:")
print(history[['Open', 'Close', 'Volume']])
print("\nEnvironment is fully operational!")