from fastapi import FastAPI
from .database import engine, Base
from .models import Task
from .routers.tasks import router as task_router
from .routers.users import routers as user_router

app = FastAPI(
    title="TaskForge API",
    description="Task management API built with FastAPI",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(task_router)
app.include_router(user_router)