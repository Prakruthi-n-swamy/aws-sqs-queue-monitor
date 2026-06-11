import boto3
import yaml

from monitor.alert_handler import send_alert
from monitor.csv_reporter import write_report

sqs = boto3.client("sqs")

with open("config/queues.yaml") as file:
    config = yaml.safe_load(file)

for queue_name, threshold in config["queues"].items():

    print(f"Checking {queue_name}")

    current_messages = 150
    current_age = 350

    if current_messages > threshold["max_messages"]:
        send_alert(
            queue_name,
            "message_count",
            current_messages
        )

    if current_age > threshold["max_age_seconds"]:
        send_alert(
            queue_name,
            "message_age",
            current_age
        )

    write_report(
        queue_name,
        current_messages,
        current_age
    )
