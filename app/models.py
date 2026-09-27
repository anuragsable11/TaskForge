from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="tasks")

class User(Base):
    __tablename__ = "users"
    id =Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    tasks = relationship("Task", back_populates="user")