import pytest
import pandas as pd
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
    large_jumps = diff[diff > diff.mean() + 2*
