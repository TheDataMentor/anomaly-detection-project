from flask import Flask, render_template, jsonify
import pandas as pd
import json
import logging
from src.data_generation import generate_synthetic_data
from src.anomaly_detection import detect_anomalies

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    try:
        # Generate synthetic data
        df = generate_synthetic_data()
        logger.info("Synthetic data generated successfully")

        # Perform anomaly detection
        df_with_anomalies = detect_anomalies(df)
        logger.info("Anomaly detection completed")

        # Prepare data for JSON response
        data = {
            'dates': df_with_anomalies.index.strftime('%Y-%m-%d').tolist(),
            'values': df_with_anomalies['value'].tolist(),
            'anomalies': df_with_anomalies['anomaly'].tolist()
        }

        return jsonify(data)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing the data"}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
