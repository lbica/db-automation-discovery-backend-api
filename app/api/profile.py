from fastapi import APIRouter
from app.services.profiler import run_profiler

router = APIRouter()

@router.post("/")
async def profile_code(payload: dict):
    result = run_profiler(payload.get("code"))
    return {"result": result}
