import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):

    location_id = event.get("pathParameters", {}).get("id")

    if not location_id:
        return {"statusCode": 400, "body": "Missing location id"}

    response = table.query(
        IndexName="location_id-index",
        KeyConditionExpression=Key("location_id").eq(int(location_id))
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response.get("Items", []))
    }