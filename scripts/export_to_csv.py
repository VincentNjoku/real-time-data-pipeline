import boto3
import pandas as pd
from datetime import datetime

# DynamoDB and S3 configurations
DYNAMODB_TABLE = "IoTData"
OUTPUT_FILE = "iot_data.csv"

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)

def convert_timestamp(epoch_time):
    """Convert Unix epoch time to a readable datetime format."""
    return datetime.fromtimestamp(int(epoch_time)).strftime('%Y-%m-%d %H:%M:%S')

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (float(celsius) * 9/5) + 32

def scale_humidity(humidity):
    """Scale humidity to a percentage if necessary."""
    return float(humidity) * 100

def export_dynamodb_to_csv():
    # Scan the DynamoDB table
    response = table.scan()
    data = response.get('Items', [])

    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Process columns
    if 'timestamp' in df.columns:
        df['timestamp'] = df['timestamp'].apply(convert_timestamp)
    if 'temperature' in df.columns:
        df['temperature'] = df['temperature'].apply(convert_to_fahrenheit)
    if 'humidity' in df.columns:
        df['humidity'] = df['humidity'].apply(scale_humidity)

    # Save as CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Exported data to {OUTPUT_FILE}")

if __name__ == "__main__":
    export_dynamodb_to_csv()
