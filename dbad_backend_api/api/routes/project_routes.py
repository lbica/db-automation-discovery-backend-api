from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dbad_backend_api.api.dtos.project_dto import ProjectResponse
from dbad_backend_api.core.database import get_db
from dbad_backend_api.core.services.project_service import ProjectService


router = APIRouter()

@router.post("/projects", response_model=list[ProjectResponse])
def list_users(db: Session = Depends(get_db)):
    return ProjectService.list_projects(db)