# Stock Analysis and Backtesting Project

## 📜 Project Overview

This project provides a comprehensive framework for analyzing stock performance using a Simple Moving Average (SMA) crossover trading strategy. It's designed for educational purposes and as a foundation for more advanced algorithmic trading simulations. The core functionality includes fetching historical stock data, applying a defined trading strategy, backtesting its performance, calculating key financial metrics, and visualizing the outcomes across multiple selected stocks.

## ✨ Features

-   **Batch Processing**: Efficiently analyze a predefined list of stock tickers (e.g., AAPL, TSLA, MSFT, INFY.NS, RELIANCE.NS) to compare their performance under the same strategy.
-   **SMA Crossover Strategy**: Implements a widely used technical analysis strategy where buy and sell signals are generated based on the crossing of short-term and long-term Simple Moving Averages.
-   **Robust Backtesting Engine**: A dedicated module simulates trades over historical data, tracking cash, shares, and portfolio value to determine the strategy's profitability.
-   **Comprehensive Performance Metrics**: Calculates essential metrics to evaluate the strategy's effectiveness, including:
    -   **Total Return (%)**: The percentage gain or loss over the backtesting period.
    -   **Max Drawdown (%)**: The largest peak-to-trough decline in portfolio value, indicating risk.
    -   **Sharpe Ratio**: A measure of risk-adjusted return, indicating how much excess return is received for the volatility taken.
-   **Advanced Data Visualization**: Generates insightful plots to understand the strategy's impact:
    -   **SMA Crossover Plot**: Visualizes closing prices, short SMA, long SMA, and buy/sell signals for each stock.
    -   **Portfolio Value Plot**: Displays the evolution of the portfolio's value over the backtesting period.
-   **CSV Export**: All calculated performance metrics for each stock are neatly summarized and saved to a CSV file (`strategy_results.csv`) for easy analysis and record-keeping.

## 📁 Project Structure

```
stock_analysis/
├── data/
│   └── fetch_stocks.py     # Handles downloading historical stock data
│   └── AAPL.csv            # Example downloaded stock data (can be removed or regenerated)
├── back_engine.py          # Contains the backtesting logic
├── performance.py          # Calculates various performance metrics
├── plot_signals.py         # Functions for plotting SMA crossovers
├── portfolio_value.py      # Functions for plotting portfolio value
├── main.py                 # Main script to run the analysis
└── README.md               # This README file
└── strategy_results.csv    # (Generated after running) Stores batched analysis results
```

## 🛠️ Setup

To get this project up and running on your local machine, follow these steps:

1.  **Clone the Repository:**
    If you have a Git client installed, open your terminal or command prompt and run:
    ```bash
    git clone <repository_url>
    cd stock_analysis
    ```
    (Replace `<repository_url>` with the actual URL of your repository.)

2.  **Install Dependencies:**
    This project relies on several Python libraries. It's recommended to use a virtual environment to manage dependencies.
    ```bash
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install the required Python packages
    pip install pandas matplotlib yfinance numpy
    ```

## 🚀 Usage

Once the setup is complete, you can run the analysis from your terminal:

```bash
python main.py
```

Upon execution, the script will:

1.  **Prompt for Initial Capital**: You will be asked to enter an initial cash amount for the backtesting simulation. You can type a value (e.g., `100000`) and press Enter, or simply press Enter to use the default initial capital (₹100,000).
2.  **Process Stocks**: The script will then iterate through each stock ticker defined in `main.py`. For each stock, it will:
    -   Download historical data using `yfinance`.
    -   Apply the SMA crossover strategy.
    -   Perform a backtest to simulate trading.
    -   Calculate performance metrics.
3.  **Display Graphs**: Two separate `matplotlib` plot windows will appear:
    -   One showing the **SMA Crossover Strategies Across Multiple Stocks**.
    -   Another showing the **Portfolio Value Across Multiple Stocks**.
    **Important**: The script will pause execution until you manually close these plot windows.
4.  **Print Summary**: After you close the plot windows, a detailed summary table of performance metrics for all analyzed stocks will be printed directly to your console.
5.  **Save Results**: The same performance summary will be saved to a CSV file named `strategy_results.csv` in the root directory of your project.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature` or `fix/BugFix`).
3.  Make your changes and ensure your code adheres to the existing style.
4.  Write clear commit messages.
5.  Push your changes and open a pull request.

## ❓ Troubleshooting

-   **`ModuleNotFoundError`**: Ensure all dependencies are installed using `pip install pandas matplotlib yfinance numpy`. Also, check that file names and import paths are correct (e.g., `your_module.py` vs `your_module`).
-   **Graphs Not Appearing / Script Hanging**: If the script seems to stop after "SMA strategy applied" or "Plot generated", it's likely waiting for you to manually close the `matplotlib` plot windows that pop up. Close them to continue.
-   **`RuntimeWarning` / `Sharpe Ratio: nan`**: These warnings often indicate issues with data (e.g., divisions by zero or `NaN` values) during performance calculations. The code has been designed to handle many of these, but complex market data can sometimes introduce edge cases. Ensure your `yfinance` data is clean and consider longer date ranges if experiencing many `NaN`s in early data points.
-   **`FutureWarning` from `yfinance` or `pandas`**: These are generally informational warnings about upcoming changes in the libraries and do not usually break the functionality of the script. It's good practice to keep your libraries updated (`pip install --upgrade yfinance pandas`). 