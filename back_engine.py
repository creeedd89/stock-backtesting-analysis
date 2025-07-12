def backtest_sma_strategy(df, initial_cash=100000):
    """
    Backtests SMA crossover strategy with a simple buy-sell system.

    Parameters:
    - df (DataFrame): Must contain 'Close' and 'Signal' columns
    - initial_cash (float): Starting capital

    Returns:
    - portfolio_value (float): Final portfolio value
    - trades (int): Number of trades made
    - df (DataFrame): With portfolio tracking columns
    """
    cash = initial_cash
    shares = 0
    trades = 0
    df = df.copy()
    df['Position'] = 0
    df['Portfolio Value'] = 0.0 # Initialize with float type

    for i in range(1, len(df)):
        signal = df.iloc[i]['Signal'].item()
        price = df.iloc[i]['Close'].item()

        if signal == 1 and cash >= price:
            # Buy
            shares = cash // price
            cash -= shares * price
            trades += 1
            df.at[df.index[i], 'Position'] = shares

        elif signal == -1 and shares > 0:
            # Sell
            cash += shares * price
            shares = 0
            trades += 1
            df.at[df.index[i], 'Position'] = -1

        # Track portfolio value
        df.at[df.index[i], 'Portfolio Value'] = cash + shares * price

    final_value = cash + shares * df.iloc[-1]['Close'].item()
    return final_value, trades, df
