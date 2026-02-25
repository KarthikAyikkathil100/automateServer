import logging
import os
import requests
import boto3
from multiprocessing import Value, Lock

# Shared across forked processes
active_tasks = Value('i', 0)
lock = Lock()

ecs = boto3.client("ecs")

_cluster_name = None
_task_id = None
_protection_enabled = False


def _get_task_info():
    global _cluster_name, _task_id

    if _cluster_name and _task_id:
        return _cluster_name, _task_id

    metadata_uri = os.environ.get("ECS_CONTAINER_METADATA_URI_V4")
    if not metadata_uri:
        raise RuntimeError("Not running inside ECS")

    data = requests.get(f"{metadata_uri}/task").json()

    task_arn = data["TaskARN"]
    cluster_arn = data["Cluster"]

    _cluster_name = cluster_arn.split("/")[-1]
    _task_id = task_arn.split("/")[-1]

    return _cluster_name, _task_id


def _update_protection(enable: bool, expires_in_minutes: int = 120):
    global _protection_enabled

    cluster, task_id = _get_task_info()
    params = {
        'cluster': cluster,
        'tasks': [task_id],
        'protectionEnabled': enable,
    }
    if enable == True:
        params['expiresInMinutes'] = expires_in_minutes
    ecs.update_task_protection(**params)

    _protection_enabled = enable
    logging.info(f"[ECS] Protection set to {enable}")
    if enable == True:
        logging.info(f"[ECS] Protection extended for {expires_in_minutes} minutes")


def increment():
    with lock:
        active_tasks.value += 1
        _update_protection(True, 120)


def decrement():
    with lock:
        active_tasks.value -= 1
        if active_tasks.value == 0:
            _update_protection(False)