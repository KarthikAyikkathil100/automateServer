import os
import logging
logging.basicConfig(level=logging.INFO)

import ecs_protection as protection


from celery import Celery, signals

# Celery app instance
app = Celery('tasks')
env_value = os.environ.get("STAGE", "staging")
logging.info(f"Environment: {env_value}")
# Configure Celery to use SQS as the broker
app.conf.update(
    broker_url="sqs://",  
    broker_transport_options={
        "region": os.environ.get("AWS_DEFAULT_REGION"),
        "visibility_timeout": 9000
    },
    task_default_queue=f"RoutemeWayfinding-{env_value}-AutomationQueue", 

    task_default_max_retries=0,

    # The below config makes sure that prefetch of SQS items is minimum
    worker_prefetch_multiplier=1,
    task_acks_late=True
)
app.conf.imports = ['celery_tasks']

# ----- SIGNAL HOOKS -----

@signals.task_prerun.connect
def task_started(**kwargs):
    protection.increment()


@signals.task_postrun.connect
def task_finished(**kwargs):
    protection.decrement()


