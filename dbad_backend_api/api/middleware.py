# app/core/middleware.py
from fastapi import Request
from fastapi.responses import JSONResponse

async def exception_logging_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # logger.exception(f"Unhandled exception for request {request.url}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )
