from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from api.users import get_user_manager
from api.models import User
from api.schemas import UserRead, UserCreate, UserUpdate
import uuid
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import func
from . import models, schemas, crud
from .database import engine, get_async_session, init_db
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware  






load_dotenv()

SECRET = os.getenv("SECRET")

app = FastAPI()

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

jwt_auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [jwt_auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(jwt_auth_backend),
    prefix = "/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead,UserCreate),
    prefix = "/auth",
    tags = ["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix = "/users",
    tags = ["users"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
def read_root():
    return {"message" : "Coffee API is alive!"}



@app.post("/recipes/", response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_async_session)):

    return await crud.create_recipe(db, recipe = recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe])
async def read_recipes(db: Session = Depends(get_async_session)):
    result = await db.execute(select(models.Recipe).limit(20))
    recipes = result.scalars().all()
    return recipes

@app.get("/recipes/search", response_model=list[schemas.Recipe])
async def query_recipes(
    id: Optional[int] = Query(None, description = "Recipe ID"),
    method: Optional[str] = Query(None, description = "Recipe Method"),
    name: Optional[str] = Query(None, description = "Recipe Name"),
    max_time: Optional[int] = Query(None, description = "Recipe Brew Time"),
    db: AsyncSession = Depends(get_async_session)
):
    query = select(models.Recipe)
    
    if id : 
        query = query.filter((models.Recipe.id) == id)
    
    if method :
        query = query.filter(func.lower(models.Recipe.method) == method.lower())
        
    if name: 
       #split into words; all must appear( case insensitive )
       for word in name.strip().split():
           query = query.filter(models.Recipe.name.ilike(f"%{word}%"))
           
    results = await db.execute(query)
    recipes = results.scalars().all()
    
    if max_time is not None:
        limit_seconds = max_time * 60
        recipes = [r for r in recipes if r.brew_time and parse_brew_time(r.brew_time) <= limit_seconds]
    
    return recipes

@app.get("/recipes/{recipe_id}")
async def read_recipe(recipe_id: int, db: Session = Depends(get_async_session)):
    result = await db.execute(select(models.Recipe).where(models.Recipe.id == recipe_id))
    db_recipe = result.scalars().first()
    if db_recipe == None : 
        raise HTTPException(status_code=404, detail= "Recipe not found")
    
    return db_recipe




@app.get("/random-recipe", response_model=schemas.Recipe)
async def random_recipe(db: Session = Depends(get_async_session)):
    result = ( 
        select(models.Recipe)
        .filter(func.lower(models.Recipe.method) != "cold brew")
        .order_by(func.random())
        .limit(1)
    )
    result = await db.execute(result)
    recipe = result.scalars().first()
    if not recipe : 
        raise HTTPException(status_code=404, detail="No recipes availible")
    return recipe


def parse_brew_time(time_str : str) -> int:
    if "-" in time_str:
        
        time_str = time_str.split("-")[-1].strip()
    
    if "h" in time_str:
        hours = int(time_str.replace("h", "").strip())
        return hours * 3600
    
    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        return int(minutes) * 60 + int(seconds)

    return int(time_str) * 60 