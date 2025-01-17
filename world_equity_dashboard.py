import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)

# List of major global indices (tickers may vary)
indices = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "Nasdaq": "^IXIC",
    "FTSE 100": "^FTSE",
    #"Nikkei 225": "^N225",
    "DAX": "^GDAXI",
    "CAC 40": "^FCHI",
    "Shanghai Composite": "000001.SS",
}

# Fetch data
data = {}
for name, ticker in indices.items():
    # Fetch historical data
    df = yf.Ticker(ticker).history(period="ytd", interval="1d")

    # drop hours. We only care about days
    df.index = df.index.date

    # Store the cleaned daily 'Close' prices
    data[name] = df['Close']

# Combine into a single DataFrame
df_combined = pd.DataFrame(data)

print(df_combined.head())

# Combine data into a DataFrame
df = pd.DataFrame(data)
print(df.head())

#visualize data
plt.figure(figsize=(15, 6))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)

plt.title("Global Equity Indices - YTD")
plt.xlabel("Date")
plt.ylabel("Index Value")
plt.legend()
plt.grid(True)

# Calculate percentage change over the period
performance_ytd = (df.iloc[-1] - df.iloc[0]) / df.iloc[0] * 100
performance_ytd = performance_ytd.sort_values(ascending=False)

performance_5d = (df.iloc[-1] - df.iloc[-5]) / df.iloc[-5] * 100
performance_5d = performance_5d.sort_values(ascending=False)

performance_1d = (df.iloc[-1] - df.iloc[-2]) / df.iloc[-2] * 100
performance_1d = performance_1d.sort_values(ascending=False)

performance = pd.DataFrame({"ytd (%)": performance_ytd,
                            "last 5 days (%)": performance_5d,
                            "yesterday (%)": performance_1d})
performance = performance.sort_values(by='yesterday (%)', ascending=False)

# Display performance rankings
print("Performance Rankings Pct:")
print(performance)

#performance.to_csv('C:/Users/vdiuser/PycharmProjects/pythonProject/performance_data.csv', index=True)

plt.show()