import os
import json
import requests
from loguru import logger
from flask import request
from utils.tracer import trace_time

LAUNCHING_APPLICATION_NAME = os.getenv("LAUNCHING_APPLICATION_NAME")
LAUNCHING_APPLICATION_TOKEN = os.getenv("LAUNCHING_APPLICATION_TOKEN")


@trace_time
def log_metrics(user, endpoint, metric_name):
    url = f"https://launching.mlops.dp.tech/api/applications/{LAUNCHING_APPLICATION_NAME}/metrics/"

    client_ip = request.remote_addr  # 获取客户端 IP 地址

    payload = {
        "application_secret": LAUNCHING_APPLICATION_TOKEN,
        "dp_method": "GET",
        "dp_path": "test_path",
        "dp_host": "lab",
        "dp_login_type": "sso",
        "dp_user": user or "anonymous",
        "dp_ip": client_ip,
        "dp_dataset": "unknown",
        "dp_endpoint": endpoint,
        "dp_source": "workbench",
        "metric_name": "_." + metric_name,
        "metric_value": 1.0,
        "metric_type": "button",
        "metric_namespace": "common",
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        logger.debug("Metrics reported successfully.")
        return True
    else:
        logger.error(
            f"Failed to report metrics. Status code: {response.status_code}. Response: {response.text}"
        )
        return False


if __name__ == "__main__":
    ret = log_metrics("liupeng", "main.go", "lp", "127.0.0.1")
    print(ret)
