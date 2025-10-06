from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from . auth import hash_password
from . models import User

async def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

async def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

async def create_recipe(db: AsyncSession, recipe: schemas.RecipeCreate, user: User):
    db_recipe = models.Recipe(**recipe.dict(), user_id = user.id)
    db.add(db_recipe)
    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe

async def get_user_by_username(db : AsyncSession, username: str):
    result = await db.execute(select(models.User).filter(models.User.username == username))
    return result.scalars().first()

async def create_user(db : AsyncSession, user: schemas.UserCreate):
    hashed = hash_password(user.password)
    db_user = models.User(username = user.username, hashed_password = hashed)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user