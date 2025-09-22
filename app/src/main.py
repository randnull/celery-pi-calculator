from fastapi import FastAPI
import uvicorn

from app.src.config import Config
from app.src.controllers import pi_router

tags = [
    {
        "name": "pi",
        "description": "Simple pi calculator API",
    }
]

app = FastAPI(openapi_tags=tags)
app.include_router(pi_router)

if __name__ == '__main__':
    config = Config()
    uvicorn.run("app.src.main:app", host=config.PI_HOST, port=int(config.PI_PORT))
