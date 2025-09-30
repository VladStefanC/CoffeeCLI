from sqlalchemy.orm import Session
from . import models, schemas

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def create_recipes_bulk(db: Session, recipes: list[schemas.RecipeCreate]):
    db_recipes = [models.Recipe(**r.dict()) for r in recipes]
    db.add_all(db_recipes)
    db.commit()
    return db_recipes