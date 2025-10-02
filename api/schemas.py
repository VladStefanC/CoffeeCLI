from pydantic import BaseModel
from typing import Optional
from fastapi_users import schemas
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
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass


