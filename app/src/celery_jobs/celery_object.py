from app.src.celery_engine import CeleryEngine
from app.src.config import Config


config = Config()
celery_engine = CeleryEngine(config)
celery = celery_engine.celery

from app.src.celery_jobs import jobs as _tasks