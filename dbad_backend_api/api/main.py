from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine


from dbad_backend_api.api.middleware import  exception_logging_middleware
from dbad_backend_api.api.routes.router import api_router
from dbad_backend_api.core.database import Base, engine
from dbad_backend_api.core.utils.logging import setup_logging

# Logging setup
setup_logging()  

# FastAPI app instance
app = FastAPI(title="DB Automation Discovery Background API", version="1.0")

# Only for **first-time DB creation**
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(api_router, prefix="/api")

# Middleware for logging exceptions
app.middleware("http")(exception_logging_middleware)

