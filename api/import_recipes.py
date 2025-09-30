from api import crud, models, schemas
from api.database import SessionLocal
from api.recipes import recipes

db = SessionLocal()

for r in recipes:
    recipe_data = schemas.RecipeCreate(
        name=r["name"],
        method=r["method"],
        ingredients=r["ingredients"],
        steps=r["steps"],
        brew_time=r["brew_time"]
    )
    crud.create_recipe(db, recipe_data)

db.close()

print("✅ All recipes imported into the database.")