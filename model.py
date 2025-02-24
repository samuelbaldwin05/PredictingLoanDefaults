import numpy as np
from scipy.stats import norm
import pandas as pd

# x0: initial value
# time: time to maturity
# X: strike price
# r: risk-free interest rate
# sigma: volatility of the underlying asset


def get_options(x0, time, X, r, sigma):
    b = (np.log(x0 / X) + (r - 0.5 * sigma**2) * time) / (sigma * np.sqrt(time))
    option = x0 * norm.cdf(sigma * np.sqrt(time) + b) - X * np.exp(
        -r * time
    ) * norm.cdf(b)
    return option


def calculate_volatility(df, column_name):
    # Calculate daily returns
    df["Returns"] = df[column_name].pct_change()

    # Calculate daily and annualized volatility
    daily_volatility = df["Returns"].std()
    annualized_volatility = daily_volatility * np.sqrt(252)

    return daily_volatility, annualized_volatility
