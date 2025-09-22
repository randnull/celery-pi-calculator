from enum import Enum


class TaskState(str, Enum):
    PROGRESS = "PROGRESS"
    FINISHED = "FINISHED"
    ERROR = "ERROR"
