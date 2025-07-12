from data.fetch_stocks import download_stock_data
from strategies import sma_crossover_strategy
from back_engine import backtest_sma_strategy
from performance import calculate_performance
from plot_signals import plot_all_sma_crossovers # Import only the collective plot
from portfolio_value import plot_all_portfolio_values # Import only the collective plot
import pandas as pd

# ✅ CONFIG
tickers = ["AAPL", "TSLA", "MSFT", "INFY.NS", "RELIANCE.NS"]
start_date = "2020-01-01"
end_date = "2023-12-31"
initial_cash = 100000

summary = []
all_stocks_data = {}

# ✅ RUN FOR MULTIPLE STOCKS
for ticker in tickers:
    print(f"\n📈 Processing {ticker}...")
    try:
        df = download_stock_data(ticker, start_date, end_date, save=False)
        df = sma_crossover_strategy(df)
        final_value, trades, df = backtest_sma_strategy(df, initial_cash)
        metrics = calculate_performance(df, initial_cash)

        # Store the DataFrame for collective plotting later
        all_stocks_data[ticker] = df

        summary.append({
            "Ticker": ticker,
            "Final Value": round(final_value, 2),
            "Trades": trades,
            **metrics
        })

    except Exception as e:
        print(f"❌ Error processing {ticker}: {e}")

# ✅ SHOW RESULTS
result_df = pd.DataFrame(summary)
print("\n📊 Strategy Summary Across Multiple Stocks:")
print(result_df.to_string(index=False))

# ✅ Plotting all strategies and portfolio values on single graphs
plot_all_sma_crossovers(all_stocks_data)
plot_all_portfolio_values(all_stocks_data)

