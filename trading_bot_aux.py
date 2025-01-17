def signal_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if open > close and previous_open < previous_close and close < previous_open and open >= previous_close:
        return 1

    # Bullish Pattern
    elif (open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
        return 2

    # No clear pattern
    else:
        return 0

def add_pattern(df):
    signal = []
    signal.append(0)
    for i in range(1, len(df)):
        tdf = df[i - 1:i + 1]
        signal.append(signal_generator(tdf))
    df["Signal"] = signal

    return df