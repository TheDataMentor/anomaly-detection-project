import pytest
import pandas as pd
import numpy as np
from src.anomaly_detection import detect_anomalies

def test_detect_anomalies():
    # Create a sample dataset with known anomalies
    dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
    values = np.random.randn(100).cumsum() + 100  # Random walk
    values[50] += 50  # Introduce an anomaly
    values[80] -= 50  # Introduce another anomaly
    
    df = pd.DataFrame({'date': dates, 'value': values})
    df.set_index('date', inplace=True)
    
    result = detect_anomalies(df)
    
    # Check if the function adds the expected columns
    assert all(col in result.columns for col in ['forecast', 'residual', 'residual_mean', 'residual_std', 'anomaly'])
    
    # Check if the known anomalies are detected
    assert result.loc['2022-02-19', 'anomaly']  # 50th day
    assert result.loc['2022-03-21', 'anomaly']  # 80th day
    
    # Check if the number of detected anomalies is reasonable (adjust as needed)
    assert 2 <= result['anomaly'].sum() <= 5

    # Check if forecasts are generated for all data points
    assert result['forecast'].notna().all()
    
    # Check if residuals are calculated correctly
    np.testing.assert_allclose(result['residual'], result['value'] - result['forecast'])

if __name__ == "__main__":
    pytest.main([__file__])
