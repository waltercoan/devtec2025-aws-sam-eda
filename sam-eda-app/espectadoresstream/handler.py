import json
import boto3
import os
from jsonschema import validate, ValidationError

def handler(event, context):
    # conectar no SQS
    sqs = boto3.client('sqs', region_name=os.environ['AWS_REGION'])
    
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))
    streamData = event
    for record in streamData['Records']:
        if 'dynamodb' in record and record['eventName'] == 'INSERT':
            dynamodb_record = record['dynamodb']
            print(f"Processing DynamoDB record: {json.dumps(dynamodb_record)}")

            espectador = dynamodb_record['NewImage']

            sqs.send_message(
                QueueUrl=os.environ['ESPECTADORESQUEUE_QUEUE_NAME'],
                MessageBody = json.dumps({
                    'cep': espectador['cep']['S']
                })
            )
            
        else:
            print("No DynamoDB record found in the event.")	
        
    return {}