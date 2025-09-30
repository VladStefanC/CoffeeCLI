from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
#IMPORT MODULES FOR DB
from api import crud, models, schemas
from api.database import engine, get_db

#TYPING IMPORT FOR OPTIONAL FIELD VALIDATION
from typing import Optional
#CORS MIDDLE WARE
from fastapi.middleware.cors import CORSMiddleware
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
#random import for math random thats it probably dont need
import random

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message" : "Coffee API is alive!"}


@app.post("/recipes/", response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe = recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe])
async def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)

@app.get("/recipes/search", response_model=list[schemas.Recipe])
async def query_recipes(
    id: Optional[int] = None,
    method: Optional[str] = None,
    name: Optional[str] = None,
    max_time: Optional[int] = None,
    db:Session= Depends(get_db)
):
    q = db.query(models.Recipe)
    
    if method :
        q = q.filter(func.lower(models.Recipe.method) == method.lower())
        
    if name: 
       #split into words; all must appear( case insensitive )
       for word in name.strip().split():
           q = q.filter(models.Recipe.name.ilike(f"%{word}%"))
           
    results = q.all()
    
    if max_time is not None:
        limit_seconds = max_time * 60
        results = [r for r in results if r.brew_time and parse_brew_time(r.brew_time) <= limit_seconds]
    
    return results


@app.get("/recipes/{recipe_id}")
async def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id= recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code = 404, detail="Recipe not found")
    return db_recipe




@app.get("/random-recipe", response_model=schemas.Recipe)
async def random_recipe(db: Session = Depends(get_db)):
    result = ( 
        db.query(models.Recipe)
            .filter(func.lower(models.Recipe.method) != "cold brew")
            .order_by(func.random())
            .first()
    )
    if not result : 
        raise HTTPException(status_code=404, detail="No recipes availible")
    return result


def parse_brew_time(time_str : str) -> int:
    #parse brew time string and return time in seconds
    if "-" in time_str:
        
        time_str = time_str.split("-")[-1].strip()
    
    if "h" in time_str:
        hours = int(time_str.replace("h", "").strip())
        return hours * 3600
    
    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        return int(minutes) * 60 + int(seconds)

    return int(time_str) * 60 