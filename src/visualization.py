import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series_with_anomalies(df, value_col='value', date_col='date', anomaly_col='anomaly'):
    """
    Plot time series data with highlighted anomalies
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df[date_col], df[value_col], label='Original Data')
    
    anomalies = df[df[anomaly_col]]
    plt.scatter(anomalies[date_col], anomalies[value_col], color='red', label='Anomalies')
    
    plt.title('Time Series with Detected Anomalies')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/detected_anomalies.png')
    plt.close()

def plot_residuals_distribution(residuals):
    """
    Plot the distribution of residuals
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.title('Distribution of ARIMA Residuals')
    plt.xlabel('Residual Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('results/residuals_distribution.png')
    plt.close()

if __name__ == "__main__":
    import pandas as pd
    from anomaly_detection import detect_anomalies
    
    df = pd.read_csv('data/synthetic_data.csv', parse_dates=['date'])
    df_with_anomalies = detect_anomalies(df)
    
    plot_time_series_with_anomalies(df_with_anomalies)
    plot_residuals_distribution(df_with_anomalies['value'] - df_with_anomalies['value'].mean())
    
    print("Plots saved in the results/ directory")
