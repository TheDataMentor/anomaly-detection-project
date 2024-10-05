import pytest
import pandas as pd
from src.data_generation import generate_synthetic_data

def test_generate_synthetic_data():
    df = generate_synthetic_data(start_date='2022-01-01', periods=100)
    
    # Check if the dataframe has the correct number of rows
    assert len(df) == 5000  # 10 stores * 5 categories * 100 days
    
    # Check if all expected columns are present
    expected_columns = ['date', 'store', 'category', 'value']
    assert all(col in df.columns for col in expected_columns)
    
    # Check if the date range is correct
    assert df['date'].min() == pd.Timestamp('2022-01-01')
    assert df['date'].max() == pd.Timestamp('2022-04-10')  # 100 days after start
    
    # Check if all stores and categories are present
    assert df['store'].nunique() == 10
    assert df['category'].nunique() == 5
    
    # Check if values are within a reasonable range
    assert df['value'].min() >= 0
    assert df['value'].max() < 1000  # Adjust this based on your expected maximum value

    # Check for the presence of seasonality (this is a simple check and might need refinement)
    monthly_avg = df.groupby(df['date'].dt.month)['value'].mean()
    assert monthly_avg.max() / monthly_avg.min() > 1.1  # Expecting at least 10% difference between highest and lowest months

if __name__ == "__main__":
    pytest.main([__file__])
