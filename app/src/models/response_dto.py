from pydantic import BaseModel

from app.src.models.enums import TaskState


class PiResponse(BaseModel):
    task_id: str


class TaskStatusResponse(BaseModel):
    state: TaskState
    progress: float
    result: str | None
