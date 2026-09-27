from fastapi import FastAPI, Depends,APIRouter, HTTPException
from ..database import get_db
from ..models import User
from ..schemas import UserCreate, UserResponse

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