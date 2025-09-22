from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.src.celery_jobs import celery_engine
from app.src.models.response_dto import PiResponse, TaskStatusResponse

pi_router = APIRouter()

@pi_router.post("/calculate_pi", tags=["pi"], response_model=PiResponse, status_code=status.HTTP_201_CREATED)
async def calculate_pi(n: int):
    """
    Get pi value with n length.

    :param n: length of pi
    :return: task_id
    """

    if n <= 0 or n > 500_000:
        return JSONResponse(content={"error": "N not in [1, 500_000]"}, status_code=status.HTTP_400_BAD_REQUEST)

    action = celery_engine.send("pi.calculate", "pi", int(n))
    return {"task_id": action.id}


@pi_router.get("/check_progress", tags=["pi"], response_model=TaskStatusResponse)
async def check_progress(task_id: str):
    """
    Check the progress of a task.

    :param task_id: id of the task
    :return: current state and result of task
    """

    result = celery_engine.async_result(task_id)
    state = result.state

    if state in ["PENDING", "STARTED"]:
        return {"state": "PROGRESS", "progress": 0.0, "result": None}
    elif state == "PROGRESS":
        progress = float((result.info or {}).get("progress", 0.0))
        return {"state": "PROGRESS", "progress": progress, "result": None}
    elif state == "SUCCESS":
        pi_value = result.result
        return {"state": "FINISHED", "progress": 1.0, "result": pi_value}
    elif state == "FAILURE":
        raise HTTPException(status_code=500, detail="Error with task")

    raise HTTPException(status_code=500, detail=f"Unknown state: {state}")
