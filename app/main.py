from fastapi import FastAPI

from app.routers import hello

app = FastAPI(title="test-ai")

app.include_router(hello.router)
