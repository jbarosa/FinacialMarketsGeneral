import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import trading_bot_aux as aux

eurusd = yf.Ticker("EURUSD=X")
today = datetime.now().date().strftime("%Y-%m-%d")
start_date = "2024-07-01"

df = eurusd.history(start=start_date, end=today, interval='15m')
#tdf = yf.download("EURUSD=X", start="2024-07-01", end=today, interval='15m')

print(df['Close'].iloc[-1:]) #most recent closing price

aux.add_pattern(df) #1- Bear; 2- Bull; 0- Null
#print(df['Signal'].value_counts())

print(df.iloc[4])
