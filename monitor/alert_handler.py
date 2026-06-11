def send_alert(queue_name, metric, value):

    print(
        f"ALERT: {queue_name} exceeded {metric} threshold. Current value: {value}"
    )
