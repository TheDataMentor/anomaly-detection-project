import pytest
import pandas as pd
import numpy as np
from src.anomaly_detection import test_stationarity, difference_series, detect_anomalies
from src.data_generation import generate_synthetic_data

@pytest.fixture
def sample_data():
    return generate_synthetic_data()

def test_test_stationarity(sample_data):
    result = test_stationarity(sample_data['value'])
    assert isinstance(result, bool)

def test_difference_series(sample_data):
    diff, count = difference_series(sample_data['value'])
    assert isinstance(diff, pd.Series)
    assert isinstance(count, int)
    assert count >= 0

def test_detect_anomalies(sample_data):
    df_with_anomalies = detect_anomalies(sample_data)
    
    assert 'anomaly' in df_with_anomalies.columns
    assert df_with_anomalies['anomaly'].dtype == bool
    assert df_with_anomalies['anomaly'].sum() > 0  # Ensure some anomalies are detected
    assert df_with_anomalies['anomaly'].sum() < len(df_with_anomalies)  # Ensure not everything is flagged as anomaly

def test_detect_anomalies_custom_threshold(sample_data):
    df_with_anomalies_1 = detect_anomalies(sample_data, threshold=2)
    df_with_anomalies_2 = detect_anomalies(sample_data, threshold=4)
    
    # Lower threshold should detect more anomalies
    assert df_with_anomalies_1['anomaly'].sum() >= df_with_anomalies_2['anomaly'].sum()

def test_detect_anomalies_different_column(sample_data):
    sample_data['other_column'] = sample_data['value'] * 2
    df_with_anomalies = detect_anomalies(sample_data, column='other_column')
    
    assert 'anomaly' in df_with_anomalies.columns
    assert df_with_anomalies
