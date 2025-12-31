import json
import boto3

s3 = boto3.client("s3")
RAW_BUCKET = "event-driven-pipeline-raw-data"
PROCESSED_BUCKET = "event-driven-pipeline-processed-data"

def lambda_handler(event, context):
    objects = s3.list_objects_v2(Bucket=RAW_BUCKET)
    count = objects.get("KeyCount", 0)

    report = {
        "total_events": count
    }

    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        Key="daily_report.json",
        Body=json.dumps(report)
    )

    return {"status": "report generated"}
