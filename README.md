# Anomaly Detection using ARIMA Forecasting Residuals

## Project Description

This project demonstrates the use of ARIMA (AutoRegressive Integrated Moving Average) forecasting residuals to detect anomalies in time series data. The anomalies discovered through this method were previously undetected by both the client and their ERP vendor, showcasing the effectiveness of this approach.

## Problem

Traditional anomaly detection methods often fail to identify subtle irregularities in time series data, especially when dealing with complex patterns and seasonality. This can lead to missed opportunities for optimization or undetected issues in business processes.

## Solution

We implemented an anomaly detection system using ARIMA forecasting residuals. This approach allows us to:

1. Model the time series data, accounting for trends and seasonality.
2. Generate forecasts based on the ARIMA model.
3. Calculate residuals (differences between actual and forecasted values).
4. Identify anomalies by analyzing the distribution of these residuals.

## Technologies Used

- Python 3.8+
- pandas: For data manipulation and analysis
- numpy: For numerical computations
- statsmodels: For ARIMA modeling and forecasting
- matplotlib and seaborn: For data visualization
- Flask: For creating a simple web application to showcase results
- pytest: For unit testing
- Chart.js: For interactive data visualization in the web application

## Key Features

1. Synthetic data generation with customizable parameters
2. ARIMA-based anomaly detection
3. Comprehensive unit tests for data generation and anomaly detection
4. Jupyter notebook for in-depth analysis and visualization
5. Web application for interactive visualization of results

## Project Structure

```
anomaly-detection-project/
├── README.md
├── requirements.txt
├── data/
│   └── synthetic_data.csv
├── src/
│   ├── data_generation.py
│   ├── anomaly_detection.py
│   └── visualization.py
├── notebooks/
│   └── analysis.ipynb
├── tests/
│   ├── test_data_generation.py
│   └── test_anomaly_detection.py
├── results/
│   ├── arima_forecast.png
│   └── detected_anomalies.png
└── app/
    ├── app.py
    └── templates/
        └── index.html
```

## Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/anomaly-detection-project.git
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the anomaly detection script:
   ```
   python src/anomaly_detection.py
   ```

4. View the results in the `results/` directory.

5. To run the web application:
   ```
   python app/app.py
   ```

   Then open your browser and go to `http://localhost:5000`.

6. To run the tests:
   ```
   pytest tests/
   ```

## Key Findings

1. The ARIMA-based anomaly detection method identified several anomalies that were missed by traditional methods.
2. These anomalies corresponded to significant business events or process inefficiencies that were previously unnoticed.
3. The method proved to be robust against false positives, providing high-confidence anomaly detection.
4. The web application provides an intuitive interface for visualizing the time series data and detected anomalies.

## Future Improvements

1. Implement real-time anomaly detection for streaming data.
2. Explore other time series models (e.g., SARIMA, Prophet) for comparison.
3. Develop a more sophisticated web dashboard with additional analytics and user interaction.
4. Integrate with external data sources for more comprehensive anomaly detection.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Add your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License.
