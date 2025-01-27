import json
import boto3
import logging
from decimal import Decimal

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IoTData')

def lambda_handler(event, context):
    for record in event['Records']:
        # Extract the S3 object details from the event
        s3_object = record['s3']['object']['key']
        s3_bucket = record['s3']['bucket']['name']

        # Retrieve the file content from S3
        s3 = boto3.client('s3')
        file_content = s3.get_object(Bucket=s3_bucket, Key=s3_object)['Body'].read().decode('utf-8')
        sensor_data = json.loads(file_content)

        # Log the raw data
        logger.info(f"Raw Data: {sensor_data}")

        # Transform the data and ensure float values are converted to Decimal
        transformed_data = {
            "sensor_id": int(sensor_data["sensor_id"]),  # Integer (valid as-is)
            "temperature": Decimal(str(sensor_data["temperature"])),  # Convert float to Decimal
            "humidity": Decimal(str(sensor_data["humidity"])),        # Convert float to Decimal
            "timestamp": int(sensor_data["timestamp"])               # Integer (valid as-is)
        }

        # Log the transformed data
        logger.info(f"Transformed Data: {transformed_data}")

        # Save transformed data to DynamoDB
        table.put_item(Item=transformed_data)

    return {"statusCode": 200, "body": "Data processed successfully"}
