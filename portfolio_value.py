def plot_portfolio_value(df, ticker):
    """
    Plots the portfolio value over time.
    
    Parameters:
    - df (DataFrame): Must contain 'Portfolio Value'
    - ticker (str): Stock ticker
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(14, 5))
    plt.plot(df['Portfolio Value'], label='Portfolio Value', color='purple')
    plt.title(f"{ticker} - Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (₹)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_all_portfolio_values(all_stocks_data):
    """
    Plots portfolio values for multiple stocks on a single graph.

    Parameters:
    - all_stocks_data (dict): Dictionary with ticker as key and DataFrame as value.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(16, 9))
    for ticker, df in all_stocks_data.items():
        if 'Portfolio Value' in df.columns:
            plt.plot(df.index, df['Portfolio Value'], label=f'{ticker} Portfolio Value')
        else:
            print(f"Warning: 'Portfolio Value' column not found for {ticker}.")

    plt.title("Portfolio Value Across Multiple Stocks")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (₹)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
