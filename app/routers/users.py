from fastapi import FastAPI, Depends,APIRouter, HTTPException
from ..database import get_db
from ..models import User
from ..schemas import UserCreate, UserResponse, TaskResponse

routers = APIRouter(
    prefix="/users",
    tags=["users"]
)

@routers.post("/", response_model=UserResponse,status_code=201)
def create_users(user:UserCreate , db=Depends(get_db)):
    new_user = User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@routers.get("/{user_id}/tasks", response_model=list[TaskResponse])
def get_user(user_id:int, db = Depends(get_db)):
    user =db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.tasks    