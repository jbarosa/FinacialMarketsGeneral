import financial_formulas as fin_form
import pandas as pd
from ipywidgets import interact, fixed

option_price = fin_form.down_and_in_put_black_scholes(100, 100, 1, 0.2, 0.05, 95)
price = round(option_price, 2)
print(price)

interact(fin_form.down_and_in_put_black_scholes, S= (70, 130), K=fixed(100), T=fixed(1), sigma=fixed(0.2), drift=fixed(0.05), B=fixed(95) )
#d = {'underlying_price': [90, 100, 110]}
#df = pd.DataFrame(data=d)
#df['option_price'] = fin_form.down_and_in_put_black_scholes(df['underlying_price'], 100, 1, 0.2, 0.05, 95)
#print(df)
