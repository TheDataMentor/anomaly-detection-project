import pandas as pd
import numpy as np

def generate_synthetic_data(start_date='2023-01-01', periods=365, freq='D'):
    """
    Generate synthetic time series data with trend, seasonality, and anomalies.
    """
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate base trend
    trend = np.linspace(100, 200, periods)
    
    # Add seasonality
    seasonality = 50 * np.sin(np.arange(periods) * (2 * np.pi / 365))
    
    # Add noise
    noise = np.random.normal(0, 10, periods)
    
    # Combine components
    values = trend + seasonality + noise
    
    # Add anomalies
    anomaly_indices = [50, 150, 250]
    for idx in anomaly_indices:
        values[idx] += np.random.uniform(50, 100)
    
    df = pd.DataFrame({'date': date_range, 'value': values})
    return df

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv('data/synthetic_data.csv', index=False)
    print("Synthetic data generated and saved to data/synthetic_data.csv")
