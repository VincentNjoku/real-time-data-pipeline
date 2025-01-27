# Real-Time Serverless Data Processing Pipeline with Tableau Visualization

## Objective
This project demonstrates a serverless application to process and store IoT sensor data in real time, with data visualization using Tableau.

## Features
- **Simulate IoT Sensor Data**: Generate temperature and humidity data using Python.
- **Real-Time Data Processing**: AWS Lambda processes and stores data in DynamoDB.
- **Data Export**: Export DynamoDB data to CSV for Tableau integration.
- **Visualization**: Tableau dashboards to analyze sensor trends and insights.

## Technologies
- AWS Lambda
- AWS S3
- DynamoDB
- CloudWatch
- Tableau
- Python

## Setup and Execution

### Step 1: Simulate IoT Data
1. Run `iot_sensor_simulation.py` to upload sensor data to S3.
2. AWS Lambda processes the data and stores it in DynamoDB.

### Step 2: Export Data for Tableau
1. Run `export_dynamodb_to_csv.py`:
   ```bash
   python export_dynamodb_to_csv.py
