from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Task
from ..schemas import TaskCreate, TaskResponse

router =APIRouter(
    prefix ="/tasks",
    tags =["tasks"]
)

@router.get("/", response_model =list[TaskResponse])
def get_task(db=Depends(get_db)):
    tasks= db.query(Task).all()
    return tasks

@router.post("/", response_model=TaskResponse, status_code=201)
def add_task(task : TaskCreate, db = Depends(get_db)):
    new_task = Task(title=task.title, user_id=task.user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task    

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id:int , db=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id:int , db=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}")
def update_task(task_id:int, task: TaskCreate, db=Depends(get_db)):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if existing_task:
        existing_task.title = task.title
        db.commit()
        return existing_task
    else:
        raise HTTPException(status_code=404, detail="Task not found")