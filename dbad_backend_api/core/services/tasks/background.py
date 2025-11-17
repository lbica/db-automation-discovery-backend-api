from fastapi import BackgroundTasks
import time
import logging

logger = logging.getLogger(__name__)

def perform_long_task(task_id: str):
    logger.info(f"Starting long task {task_id}")
    time.sleep(10)
    logger.info(f"Completed long task {task_id}")
