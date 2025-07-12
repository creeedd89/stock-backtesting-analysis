import yfinance as yf
import pandas as pd
import os

def download_stock_data(ticker, start_date, end_date, save=True):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.dropna(inplace=True)
    if save:
        os.makedirs("data", exist_ok=True)
        data.to_csv(f"data/{ticker}.csv")
    return data

if __name__ == "__main__":
    df = download_stock_data("AAPL", "2020-01-01", "2023-12-31")
    print(df.head())
