from typing import Callable, Any

from celery import Celery
from celery.result import AsyncResult

from app.src.config import Config, CelerySettings


class CeleryEngine:
    def __init__(self, celery_config: Config) -> None:
        self.celery = Celery(
            'pi_celery_engine',
            broker=celery_config.CELERY_BROKER_URL,
            backend=celery_config.CELERY_RESULT_BACKEND,
        )

        self.celery.config_from_object(CelerySettings)

    def task(self, *args: Any, **kwargs: Any) -> Callable:
        return self.celery.task(*args, **kwargs)

    def send(self, task_name: str, queue: str, *args: Any, **kwargs: Any) -> Any:
        return self.celery.send_task(task_name, queue=queue, args=list(args), kwargs=kwargs)

    def async_result(self, task_id: str) -> Any:
        return AsyncResult(task_id, app=self.celery)
