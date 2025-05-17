import json
import boto3
import re
import os
from jsonschema import validate, ValidationError


def handler(event, context):
    if(event['httpMethod'] == 'OPTIONS'):
        return {
            'statusCode': 200,
            'body': 'CORS preflight response',
            'headers': {
                "Access-Control-Allow-Headers" : "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            }
        }
    
    #conexão com a tabela espectadores no dynamoDB
    print("Inserting item into DynamoDB")
    dynamodb = boto3.client('dynamodb', region_name=os.environ['AWS_REGION'])
    
    schema = {
        "type": "object",
        "properties": {
            "nome": {"type": "string"},
            "cep": {"type": "string"},
        },
        "required": ["nome", "cep"]
    }

    espectador = json.loads(event['body'])
    print(json.dumps(espectador))

    try:
        validate(instance=espectador, schema=schema)
        espectador['cep'] = re.sub(r"[-.\s_,;:()]", "", espectador['cep'])
        dynamodb.put_item(
            TableName=os.environ['ESPECTADORES_TABLE_NAME'],
            Item={
                'nome': {'S': espectador['nome']},
                'cep': {'S': espectador['cep']},
            }
        )
        print(f"Item inserted: {espectador}")

        return {
            'statusCode': 200,
            'body': '{}',
            'headers': {
                "Access-Control-Allow-Headers" : "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            }
        }
    except ValidationError as e:
        return {
            'statusCode': 400,
            'body': '{}',
            'headers': {
                "Access-Control-Allow-Headers" : "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            }
        }