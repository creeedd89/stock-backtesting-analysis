import pandas as pd

def sma_crossover_strategy(df, short_window=20, long_window=50):
    """
    Adds SMA crossover buy/sell signals to the DataFrame.

    Parameters:
    - df (DataFrame): Stock price data with 'Close' column
    - short_window (int): Window for short-term SMA
    - long_window (int): Window for long-term SMA

    Returns:
    - df (DataFrame): Original df with 'Signal' and SMAs
    """

    df = df.copy()

    # Calculate SMAs
    df['SMA_Short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window).mean()

    # Create signals
    df['Signal'] = 0
    df.loc[df['SMA_Short'] > df['SMA_Long'], 'Signal'] = 1
    df.loc[df['SMA_Short'] < df['SMA_Long'], 'Signal'] = -1

    return df
