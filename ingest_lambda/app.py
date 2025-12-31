import json
import boto3
import uuid

s3 = boto3.client("s3")
BUCKET = "event-driven-pipeline-raw-data"

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    key = f"{uuid.uuid4()}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(body)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Data ingested"})
    }
