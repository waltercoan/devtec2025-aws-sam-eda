import json
import requests
import boto3
import os

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    try:
        dynamodb = boto3.client('dynamodb', region_name=os.environ['AWS_REGION'])

        streamData = event
        for record in streamData['Records']:
            if 'eventSource' in record and record['eventSource'] == 'aws:sqs':
                print(f"Processing SQS message: {record['body']}")
                sqs_message = json.loads(record['body'])
                
                response = requests.get(f"https://brasilapi.com.br/api/cep/v2/{sqs_message['cep']}")
                if response.status_code == 200:
                    data = response.json()
                    
                    if 'latitude' in data['location']['coordinates']:
                        dynamodb.put_item(
                            TableName=os.environ['PONTOS_TABLE_NAME'],
                            Item={
                                'cep': {'S': data['cep']},
                                'cidade': {'S': data['city']},
                                'rua': {'S': "" if data['street'] is None else data['street']},
                                'latitude': {'S': data['location']['coordinates']['latitude']},
                                'longitude': {'S': data['location']['coordinates']['longitude']}
                            }
                        )
                        print("Data inserted into DynamoDB")
                else:
                    print(f"Error fetching data from BrasilAPI: {response.status_code}")
    finally:
        return {
            'statusCode': 200
        }
