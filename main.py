from fastapi import FastAPI
from pydantic import BaseModel

from database import engine, Base, SessionLocal
from models import Task

class TaskCreate(BaseModel):
    title : str

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/tasks")
def get_task():
    db = SessionLocal()
    tasks= db.query(Task).all()
    db.close()
    return tasks

@app.post("/tasks")
def add_task(task : TaskCreate):
    db = SessionLocal()
    new_task = Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.close()
    return new_task    

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id:int):
    db =SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    db  = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return {"message": "Task deleted successfully"}
    else:
        db.close()
        return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id:int, task: TaskCreate):
    db = SessionLocal()
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task:
        existing_task.title = task.title
        db.commit()
        db.close()
        return existing_task
    else:
        db.close()
        return {"message": "Task not found"}