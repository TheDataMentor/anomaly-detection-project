import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def detect_anomalies(df, value_col='value', date_col='date', window=30, threshold=3):
    """
    Detect anomalies in time series data using ARIMA forecasting residuals.
    
    Args:
    df (pd.DataFrame): Input dataframe with datetime index and value column
    value_col (str): Name of the column containing the time series values
    date_col (str): Name of the column containing the dates (if not index)
    window (int): Rolling window size for calculating mean and std of residuals
    threshold (float): Number of standard deviations to use as anomaly threshold
    
    Returns:
    pd.DataFrame: Original dataframe with additional columns for forecast and anomaly flag
    """
    
    # Ensure the dataframe is sorted by date
    df = df.sort_index() if df.index.name == date_col else df.sort_values(date_col)
    
    # Fit ARIMA model
    model = ARIMA(df[value_col], order=(1,1,1))  # You might need to adjust these parameters
    results = model.fit()
    
    # Generate forecasts
    forecast = results.forecast(steps=len(df))
    
    # Calculate residuals
    df['forecast'] = forecast
    df['residual'] = df[value_col] - df['forecast']
    
    # Calculate rolling statistics
    df['residual_mean'] = df['residual'].rolling(window=window).mean()
    df['residual_std'] = df['residual'].rolling(window=window).std()
    
    # Detect anomalies
    df['anomaly'] = abs(df['residual'] - df['residual_mean']) > (threshold * df['residual_std'])
    
    return df

if __name__ == "__main__":
    # Test the function with some sample data
    dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
    values = np.random.randn(100).cumsum() + 100  # Random walk
    values[80] += 50  # Introduce an anomaly
    
    df = pd.DataFrame({'date': dates, 'value': values})
    df.set_index('date', inplace=True)
    
    result = detect_anomalies(df)
    print(f"Detected {result['anomaly'].sum()} anomalies")
    print(result[result['anomaly']])
