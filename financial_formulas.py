import math
from scipy.stats import norm


def simple_black_scholes(option_type, s, k, t, sigma, drift):
    """
    Calculate option price for a simple call or put option
    
    :param option_type: option type, call or put
    :param s: stock current price
    :param k: option strike
    :param t: period in years
    :param sigma: stock standard deviation
    :param drift: for now let's only use riskFreeRate (next we can add dividend,
     repo or historical drift)
    :return: Option current price
    """
    d1 = 1/(sigma * math.sqrt(t)) * (math.log(s/k) + (drift + (sigma**2)/2)*t)
    d2 = d1 - sigma*math.sqrt(t)
    if option_type == 'call':
        option_price = norm.cdf(d1) * s - norm.cdf(d2) * k * math.exp(-drift*t)
    elif option_type == 'put':
        option_price = norm.cdf(-d2)*k*math.exp(-drift*t) - norm.cdf(-d1)*s
    else:
        raise ValueError('only call or put are accepted as types')
    return option_price


def down_and_in_put_black_scholes(s, k, t, sigma, drift, b):
    """
    Calculates current price for a down-and-in option
    
    :param s: stock current price
    :param k: option strike
    :param t: period in years
    :param sigma: stock standard deviation
    :param drift: for now let's only use riskFreeRate (next we can add dividend,
    repo or historical drift)
    :param b: Barrier level
    :return: Option Current Price
    """
    lambda_1 = (drift + (sigma**2)/2)/(sigma**2)
    y_0 = (math.log((b**2)/(s*k))/(sigma*math.sqrt(t)) +
           lambda_1*sigma*math.sqrt(t))
    y_1 = math.log(b/s)/(sigma*math.sqrt(t)) + lambda_1*sigma*math.sqrt(t)
    x_1 = math.log(s/b)/(sigma*math.sqrt(t)) + lambda_1*sigma*math.sqrt(t)
    option_price = (-s * norm.cdf(-x_1) +
                    k * math.exp(-drift * t) *
                    norm.cdf(-x_1 + sigma * math.sqrt(t))) + \
        s * ((b / s)**(2 * lambda_1)) * (norm.cdf(y_0) - norm.cdf(y_1)) - \
        k * math.exp(-drift * t) * ((b/s)**(2*lambda_1-2)) * \
        (norm.cdf(y_0-sigma*math.sqrt(t)) - norm.cdf(y_1-sigma*math.sqrt(t)))

    return option_price


def bond_valuation():

    res = 1

    return res
