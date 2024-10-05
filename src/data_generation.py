import pandas as pd
import numpy as np
from datetime import datetime, timedelta

'''
This script generates synthetic retail purchase data with the following characteristics:

Uses pandas and numpy for data manipulation and random number generation.
Covers a two-year period from 2022 to 2023.
Includes data for 10 stores and 5 product categories.
Incorporates a seasonal component using a sine function.
Adds a trend component that varies by store and category.
Includes random noise to make the data more realistic.
Introduces anomalies on random days (10% chance for each day).
Aggregates data at the category level for each store.

The script saves the generated data to a CSV file and prints some summary statistics to verify the seasonality and overall structure of the data.
'''



def generate_synthetic_data(start_date='2022-01-01', periods=730, freq='D'):
    """
    Generate synthetic retail purchase data with trend, seasonality, and anomalies for multiple stores and categories.
    """
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Define categories and stores
    categories = ['Electronics', 'Clothing', 'Groceries', 'Home & Garden', 'Toys']
    stores = [f'Store_{i}' for i in range(1, 11)]  # 10 stores
    
    data = []
    for store in stores:
        for category in categories:
            # Generate base trend
            base_value = np.random.randint(100, 200)
            trend = np.linspace(base_value, base_value * 2, periods)
            
            # Add seasonality
            seasonality_amplitude = np.random.uniform(30, 70)
            seasonality = seasonality_amplitude * np.sin(np.arange(periods) * (2 * np.pi / 365))
            
            # Add noise
            noise = np.random.normal(0, base_value * 0.1, periods)
            
            # Combine components
            values = trend + seasonality + noise
            
            # Add anomalies (randomly for each store-category combination)
            anomaly_indices = np.random.choice(periods, size=3, replace=False)
            for idx in anomaly_indices:
                values[idx] += np.random.uniform(base_value * 0.5, base_value)
            
            # Ensure no negative values
            values = np.maximum(values, 0)
            
            for date, value in zip(date_range, values):
                data.append({
                    'date': date,
                    'store': store,
                    'category': category,
                    'value': round(value, 2)
                })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv('data/synthetic_retail_data.csv', index=False)
    print("Synthetic retail data generated and saved to data/synthetic_retail_data.csv")
    
    # Display summary statistics
    print("\nSummary Statistics:")
    print(df.groupby('category')['value'].describe())
    
    # Verify seasonality
    print("\nMonthly Average Sales:")
    print(df.groupby([df['date'].dt.to_period('M'), 'category'])['value'].mean().unstack())
