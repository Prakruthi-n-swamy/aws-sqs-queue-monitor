# aws-sqs-queue-monitor
Python-based AWS SQS monitoring solution with queue health checks, threshold alerts, and reporting automation.

## Features

- Queue depth monitoring
- Oldest message age tracking
- Threshold-based alerting
- CSV reporting
- Endpoint health checks
- GitHub Actions CI

## Architecture

```text
SQS Queue
    |
    v
Python Monitor
    |
    +---- Alert Handler
    |
    +---- CSV Reports
```

## Technologies

- Python
- AWS SQS
- boto3
- GitHub Actions

## Example Alert

ALERT: payment-queue exceeded message_count threshold. Current value: 1500

## Future Enhancements

- SNS Integration
- Slack Notifications
- CloudWatch Metric Publishing
- Prometheus Exporter
