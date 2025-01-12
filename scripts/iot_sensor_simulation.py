import boto3
import random
import json
import time

#AWS S3 Setup
s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'iot-sensor-data123'

def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 100),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2),
        "timestamp": time.time()
    }

while True:
    data = generate_sensor_data()
    file_name = f"iot-data-{int(time.time())}.json"
    s3.put_object(
        Bucket=bucket_name,
        Key=f"raw/{file_name}",
        Body=json.dumps(data)
    )
    print(f"Uploaded: {file_name} to S3")
    time.sleep(2) # Simulate data every 2 seconds