import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

def test_stationarity(timeseries):
    """
    Perform Dickey-Fuller test for stationarity
    """
    result = adfuller(timeseries, autolag='AIC')
    return result[1] <= 0.05

def difference_series(series):
    """
    Difference the series until it becomes stationary
    """
    diff = series
    count = 0
    while not test_stationarity(diff):
        diff = diff.diff().dropna()
        count += 1
    return diff, count

def detect_anomalies(df, column='value', threshold=3):
    """
    Detect anomalies using ARIMA forecasting residuals
    """
    series = df[column]
    
    # Difference series if not stationary
    diff_series, d = difference_series(series)
    
    # Fit ARIMA model
    model = ARIMA(series, order=(1, d, 1))
    results = model.fit()
    
    # Calculate residuals
    residuals = results.resid
    
    # Detect anomalies
    mean_residual = np.mean(residuals)
    std_residual = np.std(residuals)
    anomalies = np.abs(residuals - mean_residual) > (threshold * std_residual)
    
    df['anomaly'] = anomalies
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/synthetic_data.csv', parse_dates=['date'])
    df.set_index('date', inplace=True)
    
    df_with_anomalies = detect_anomalies(df)
    print(f"Detected {df_with_anomalies['anomaly'].sum()} anomalies")
    df_with_anomalies.to_csv('results/detected_anomalies.csv')
