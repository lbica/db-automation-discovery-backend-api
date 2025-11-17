from fastapi import APIRouter
from dbad_backend_api.api.routes.user_routes import router as user_router
from dbad_backend_api.api.routes.project_routes import router as project_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(project_router, prefix="/projects", tags=["Projects"])
