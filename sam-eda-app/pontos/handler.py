import json
import boto3
import os
from jsonschema import validate, ValidationError

def handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name=os.environ['AWS_REGION'])
    
    lista_pontos = []
    pontos = dynamodb.scan(
        TableName=os.environ['PONTOS_TABLE_NAME']
    )
    
    for item in pontos['Items']:
        ponto = {
            'cep': item['cep']['S'],
            'cidade': item['cidade']['S'],
            'latitude': item['latitude']['S'],
            'longitude': item['longitude']['S'],
            'rua': item['rua']['S']
        }
        lista_pontos.append(ponto)

    return {
            'statusCode': 200,
            'body': json.dumps(lista_pontos),
            'headers': {
                "Access-Control-Allow-Headers" : "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            }
        }