import matplotlib.pyplot as plt

def plot_sma_crossover(df, ticker):
    """
    Plots closing price, SMAs, and buy/sell signals.

    Parameters:
    - df (DataFrame): Data with 'Close', 'SMA_Short', 'SMA_Long', and 'Signal'
    - ticker (str): Stock ticker for the title
    """
    plt.figure(figsize=(14, 7))
    
    # Price and SMAs
    plt.plot(df['Close'], label='Close Price', alpha=0.6)
    plt.plot(df['SMA_Short'], label='Short SMA', color='green')
    plt.plot(df['SMA_Long'], label='Long SMA', color='red')

    # Buy signals
    buy_signals = df[df['Signal'] == 1]
    plt.scatter(buy_signals.index, buy_signals['Close'], label='Buy Signal', marker='^', color='blue', alpha=1)

    # Sell signals
    sell_signals = df[df['Signal'] == -1]
    plt.scatter(sell_signals.index, sell_signals['Close'], label='Sell Signal', marker='v', color='black', alpha=1)

    plt.title(f"{ticker} - SMA Crossover Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_all_sma_crossovers(all_stocks_data):
    """
    Plots SMA crossover strategies for multiple stocks on a single graph.

    Parameters:
    - all_stocks_data (dict): Dictionary with ticker as key and DataFrame as value.
    """
    plt.figure(figsize=(16, 9))
    for ticker, df in all_stocks_data.items():
        plt.plot(df['Close'], label=f'{ticker} Close Price', alpha=0.6)
        plt.plot(df['SMA_Short'], label=f'{ticker} Short SMA', linestyle='--')
        plt.plot(df['SMA_Long'], label=f'{ticker} Long SMA', linestyle=':')

    plt.title("SMA Crossover Strategies Across Multiple Stocks")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
