from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env dacă există
load_dotenv()

class Settings(BaseSettings):
    MODE: str = os.getenv("DBAD_MODE", "developer")

    # DB configuration depends on the mode
    @property
    def database_url(self) -> str:
        if self.MODE == "developer":
            return f"sqlite:///./dbad_repository.db"
        else:
            return os.getenv("DATABASE_URL", "postgresql://user:pass@host/db")

settings = Settings()

