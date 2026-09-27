from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    user_id: int


class TaskResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str

class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True