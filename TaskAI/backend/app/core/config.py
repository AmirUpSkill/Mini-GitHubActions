from functools import lru_cache
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- App metadata ----------------------------------------------------------
    PROJECT_NAME: str = "TaskAI"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    # --- CORS ------------------------------------------------------------------
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    # --- Database -------------------------------------------------------------
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    # --- Logging ---------------------------------------------------------------
    LOG_LEVEL: str = "INFO"

@lru_cache
def get_settings() -> Settings:
    """Return a singleton settings instance."""
    return Settings()