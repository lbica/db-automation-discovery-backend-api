from typing import Union
from app.core.logging import setup_logging
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from app.core.middleware import exception_logging_middleware

from app.core.config import settings

from app.core.database import Base, engine
from app.api.routes_user import router as user_router

# Logging setup
setup_logging()  

# FastAPI app instance
app = FastAPI(title="DB Automation Discovery Background API", version="1.0")

# Only for **first-time DB creation**
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user_router)

# Middleware for logging exceptions

app.middleware("http")(exception_logging_middleware)

