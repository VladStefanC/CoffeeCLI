from pydantic import BaseModel, ConfigDict
from typing import Optional
import uuid
from fastapi_users import schemas as fa_schemas

class RecipeBase(BaseModel):
    name: str
    method: str
    ingredients: str
    steps: str
    brew_time: Optional[str] = None

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    user_id: Optional[uuid.UUID] = None
    model_config = ConfigDict(from_attributes=True)

class UserRead(fa_schemas.BaseUser[uuid.UUID]):
    username: str | None = None

class UserCreate(fa_schemas.BaseUserCreate):
    username: str | None = None

class UserUpdate(fa_schemas.BaseUserUpdate):
    username: str | None = None