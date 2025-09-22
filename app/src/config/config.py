from pydantic_settings import BaseSettings
import os

class Config(BaseSettings):
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")
    PI_HOST: str = os.getenv("PI_HOST", "127.0.0.1")
    PI_PORT: int = os.getenv("PI_USER", "8080")
