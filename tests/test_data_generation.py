import pytest
import pandas as pd
import numpy as np
from src.data_generation import generate_synthetic_data

def test_generate_synthetic_data():
    df = generate_synthetic_data()
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 365
    assert 'date' in df.columns
    assert 'value' in df.columns
    assert df['date'].dtype == 'datetime64[ns]'
    assert df['value'].dtype == 'float64'

def test_generate_synthetic_data_custom_params():
    df = generate_synthetic_data(start_date='2024-01-01', periods=100, freq='W')
    
    assert len(df) == 100
    assert df['date'].min() == pd.Timestamp('2024-01-01')
    assert df['date'].max() == pd.Timestamp('2024-01-01') + pd.Timedelta(weeks=99)

def test_generate_synthetic_data_anomalies():
    df = generate_synthetic_data()
    
    # Check if there are at least 3 significant jumps in the data
    diff = df['value'].diff().abs()
    large_jumps = diff[diff > diff.mean() + 2*diff.std()]
    assert len(large_jumps) >= 3

def test_generate_synthetic_data_seasonality():
    df = generate_synthetic_data()
    
    # Check for seasonality by comparing first and last quarter of the year
    first_quarter = df['value'][:91].mean()
    last_quarter = df['value'][-91:].mean()
    assert abs(first_quarter - last_quarter) > 20  # Assuming significant seasonal difference

def test_generate_synthetic_data_trend():
    df = generate_synthetic_data()
    
    # Check for overall increasing trend
    first_month = df['value'][:30].mean()
    last_month = df['value'][-30:].mean()
    assert last_month > first_month

def test_generate_synthetic_data_noise():
    df = generate_synthetic_data()
    
    # Check for presence of noise
    smooth = df['value'].rolling(window=7).mean()
    noise = df['value'] - smooth
    assert noise.std() > 0  # Ensure there's some variation due to noise

if __name__ == "__main__":
    pytest.main()
