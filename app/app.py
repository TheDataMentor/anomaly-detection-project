from flask import Flask, render_template, jsonify
import pandas as pd
import json
from src.data_generation import generate_synthetic_data
from src.anomaly_detection import detect_anomalies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    df = generate_synthetic_data()
    df_with_anomalies = detect_anomalies(df)
    
    data = {
        'dates': df_with_anomalies.index.strftime('%Y-%m-%d').tolist(),
        'values': df_with_anomalies['value'].tolist(),
        'anomalies': df_with_anomalies['anomaly'].tolist()
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
