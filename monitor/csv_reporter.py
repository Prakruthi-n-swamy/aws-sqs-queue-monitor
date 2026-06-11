import csv
from datetime import datetime

def write_report(queue_name, messages, age):

    with open(
        "reports/queue_report.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            queue_name,
            messages,
            age
        ])
