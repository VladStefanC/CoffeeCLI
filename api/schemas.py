from pydantic import BaseModel
from typing import Optional

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
        

