import numpy as np

def calculate_performance(df, initial_cash):
    """
    Calculates performance metrics from portfolio value.

    Parameters:
    - df (DataFrame): Must contain 'Portfolio Value'
    - initial_cash (float): Starting capital

    Returns:
    - Dictionary of performance metrics
    """
    df = df.copy()
    df['Portfolio Value'] = df['Portfolio Value'].ffill().bfill() # Fill any NaN values
    df['Daily Return'] = df['Portfolio Value'].pct_change()
    df['Daily Return'] = df['Daily Return'].replace([np.inf, -np.inf], np.nan).dropna()

    # Total Return
    final_value = df['Portfolio Value'].iloc[-1]
    total_return = ((final_value - initial_cash) / initial_cash) * 100

    # Max Drawdown
    rolling_max = df['Portfolio Value'].cummax()
    # Handle cases where rolling_max might be zero to avoid division by zero
    drawdown = (df['Portfolio Value'] - rolling_max) / rolling_max.replace(0, np.nan)
    max_drawdown = drawdown.min(skipna=True) * 100 # Explicitly skip NaNs

    # Sharpe Ratio (Assume 0.5% daily risk-free rate annually ~ 0.00002 daily)
    if df['Daily Return'].empty or df['Daily Return'].std() == 0:
        sharpe_ratio = 0.0
    else:
        sharpe_ratio = (df['Daily Return'].mean() / df['Daily Return'].std()) * np.sqrt(252)

    return {
        "Total Return (%)": round(total_return, 2),
        "Max Drawdown (%)": round(max_drawdown, 2),
        "Sharpe Ratio": round(sharpe_ratio, 2)
    }
