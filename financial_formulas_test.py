import financial_formulas as fin_form

option_type = 'put'
S = 100
K = 100
T = 1
sigma = 0.5
drift = 0.02
B = 75

test_down_and_in = fin_form.down_and_in_put_black_scholes(S, K, T, sigma, drift, B)
print(f"The price of the down and in {option_type} option is {round(test_down_and_in,2)}\n"
      f"This value was calculated with the following inputs:\n"
      f"Stock price = {S};\n"
      f"Stock standard deviation = {sigma};\n"
      f"Strike price = {K};\n"
      f"Time of option expiration (in years) = {T};\n"
      f"Drift (only risk free rate) = {drift};\n"
      f"Barrier = {B}.\n")

test_simple = fin_form.simple_black_scholes(option_type, S, K, T, sigma, drift)
print(f'''The price of the {option_type} option is {round(test_simple, 2)}
This value was calculated with the following inputs:
Stock price = {S};
Stock standard deviation = {sigma};
Strike price = {K};
Time of option expiration (in years) = {T};
Drift (only risk free rate) = {drift};\n
''')