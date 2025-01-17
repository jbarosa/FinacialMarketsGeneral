import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

#plt.style.use('seaborn')

msft = yf.Ticker('msft')

#print(type(msft.info)) #dict with a lot of info

#let's make the dict readable:
stockinfo = msft.info
'''
#for key, value in stockinfo.items():
#    print(key, ":", value, ";")

#let's find one info:
numshares = msft.info['sharesOutstanding']
#print(numshares)

#print(msft.recommendations)
#print(msft.splits)

#print(msft.dividends)
#print(msft.major_holders)
#print(msft.institutional_holders)

print(type(msft.dividends)) #it's a pandas series we need to convert to df
tdf = msft.dividends
#print(df)

#resample df by year to sum div distributed twice a year
tdf1 = tdf.resample('YE').sum()
df = pd.DataFrame({'Date': tdf1.index, 'Dividend': tdf1.values}) # convert to df
df['Year'] = df['Date'].dt.year
#print(df)

#plot:
plt.figure()
plt.bar(df['Year'], df['Dividend'])
plt.xlabel('Year')
plt.ylabel('Dividend Yield ($)')
plt.title('Dividend History')
plt.xlim(2014, 2024)
#plt.show()
'''

#print(msft.history(period='max'))
#print(type(msft.history(period='max')))

df = msft.history(period='5y')

lastdate = df.index[-1]
firstdate = df.index[0]
#print(lastdate)
tdf = msft.history(start=firstdate, end=lastdate) #excluding dates mentioned as args in DF
#print(tdf)

today = datetime.now().date().strftime("%Y-%m-%d")
df = msft.history(start=firstdate, end=today) #better option to not lose the first and last dates
#print(df)

#plt.figure()
#plt.plot(df['Close'])
#plt.show()

#Inedexes and ETFs:

#security = yf.Ticker('voo') #ETF
#security = yf.Ticker('djia') #INDEX
security = yf.Ticker('spy')

df = security.history(period='5y')
#plt.figure()
#plt.plot(df['Close'])
#plt.show()

#multiple tickers

securities = ['voo', 'msft', 'aapl', 'nvda']
df = pd.DataFrame()
today = datetime.now().date().strftime("%Y-%m-%d")

for security in securities:
    df[security] = yf.Ticker(security).history(start=firstdate,
                                               end=today).Close

#print(df)

#plt.figure()
#plt.plot(df)
#plt.show()