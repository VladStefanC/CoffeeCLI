from pydantic import BaseModel
from typing import Optional
from fastapi_users import schemas
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import  Mapped, mapped_column
from .database import Base
import uuid


class RecipeBase(BaseModel):
    id : int
    name: str
    method: str
    ingredients: str
    steps: str
    brew_time: Optional[str] = None

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    
    class Config:
        orm_mode = True

class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str | None = None 
    
class UserCreate(schemas.BaseUserCreate):
    username: str | None = None 
    
class UserUpdate(schemas.BaseUserUpdate):
    username: str | None = None
