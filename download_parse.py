import yfinance as yf


# Load data from Yahoo Finance
def load_data(stock, start, end):
    df = yf.download(stock, start, end)["Close"]  # First sections for Apple
    return df
