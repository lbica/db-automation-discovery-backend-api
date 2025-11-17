from fastapi import APIRouter, BackgroundTasks
from uuid import uuid4


router = APIRouter()

@router.post("/run")
async def run_background_task(background_tasks: BackgroundTasks):
    task_id = str(uuid4())
    # background_tasks.add_task(perform_long_task, task_id)
    return {"task_id": task_id, "status": "started"}
