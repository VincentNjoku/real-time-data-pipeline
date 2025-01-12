import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IoTData')

def lambda_handler(event, context):
    for record in event['Records']:
        s3_object = record['s3']['object']['key'] 
        s3_bucket = record['s3']['bucket']['name'] 

        s3 = boto3.client('s3')
        file_conent = s3.get_object(Bucket=s3_bucket, Key=s3_object)['Body'].read().decode('utf-8')
        sensor_data = json.loads(file_conent)

        table.put_item(Item={
            "sensor_id": sensor_data["sensor_id"],
            "temperature": sensor_data["temperature"],
            "humidity": sensor_data["humidity"],
            "timestamp": int(sensor_data["timestamp"])
        })
    return {"statusCode": 200, "body": "Data processed successfully"}
