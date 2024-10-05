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

## Key Findings

1. The ARIMA-based anomaly detection method identified several anomalies that were missed by traditional methods.
2. These anomalies corresponded to significant business events or process inefficiencies that were previously unnoticed.
3. The method proved to be robust against false positives, providing high-confidence anomaly detection.

## Project Structure

- `data/`: Contains the synthetic data used for the project.
- `src/`: Source code for data generation, anomaly detection, and visualization.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model development.
- `tests/`: Unit tests for the main functionalities.
- `results/`: Output plots and visualizations.
- `app/`: A simple Flask web application to showcase the results.

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

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Add your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License.
