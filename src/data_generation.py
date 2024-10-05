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



# Set random seed for reproducibility
np.random.seed(42)

# Generate date range for two years
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Define categories and stores
categories = ['Electronics', 'Clothing', 'Groceries', 'Home & Garden', 'Toys']
stores = [f'Store_{i}' for i in range(1, 11)]  # 10 stores

# Create base data
data = []
for store in stores:
    for category in categories:
        base_sales = np.random.randint(1000, 5000)
        trend = np.random.uniform(0.8, 1.2)
        seasonal_amplitude = np.random.uniform(0.1, 0.3) * base_sales
        
        for date in date_range:
            # Add trend
            trend_component = base_sales * (trend ** ((date - start_date).days / 365))
            
            # Add seasonality (yearly cycle)
            day_of_year = date.dayofyear
            seasonal_component = seasonal_amplitude * np.sin(2 * np.pi * day_of_year / 365)
            
            # Add noise
            noise = np.random.normal(0, base_sales * 0.1)
            
            # Calculate sales
            sales = max(0, trend_component + seasonal_component + noise)
            
            data.append({
                'Date': date,
                'Store': store,
                'Category': category,
                'Sales': round(sales, 2)
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Add anomalies (10% chance for each day)
anomaly_dates = date_range[np.random.random(len(date_range)) < 0.1]
for date in anomaly_dates:
    mask = (df['Date'] == date)
    df.loc[mask, 'Sales'] *= np.random.uniform(1.5, 3)

# Sort the DataFrame
df = df.sort_values(['Date', 'Store', 'Category'])

# Display the first few rows
print(df.head())

# Save to CSV
df.to_csv('synthetic_retail_data.csv', index=False)
print("Data saved to 'synthetic_retail_data.csv'")

# Summary statistics
print("\nSummary Statistics:")
print(df.groupby('Category')['Sales'].describe())

# Verify seasonality
print("\nMonthly Average Sales:")
print(df.groupby([df['Date'].dt.to_period('M'), 'Category'])['Sales'].mean().unstack())
