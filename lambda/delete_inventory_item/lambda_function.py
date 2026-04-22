import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']

    table.delete_item(
        Key={'item_id': item_id}
    )

    return {
        'statusCode': 200,
        'body': 'Item deleted'
    }