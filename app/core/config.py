from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # App
    app_name: str = Field(default="FastAPI CRUD Example", env="APP_NAME")
    app_env: str = Field(default="development", env="APP_ENV")

    # Database
    database_url: str = Field(..., env="DATABASE_URL")

    # Secrets
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = Field(default=60, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
