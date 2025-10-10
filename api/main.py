from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers, BaseUserManager
from fastapi_users.jwt import generate_jwt
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from typing import Optional
import uuid
import os
from dotenv import load_dotenv

from api.database import get_async_session, init_db
from api.users import get_user_manager
from api import models, schemas, crud
from api.models import User
from fastapi import Response, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users.authentication import CookieTransport 
from fastapi import Cookie
from fastapi_users.jwt import decode_jwt


# ──────────────────────────────────────────────────────────────
# Setup
# ──────────────────────────────────────────────────────────────

load_dotenv()

SECRET = os.getenv("SECRET")

app = FastAPI(title="Coffee Recipes API", version="2.0")
auth_router = APIRouter()
# JWT authentication setup
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


cookie_transport = CookieTransport(
    cookie_max_age=3600 * 24 * 7,
    cookie_secure = True, # development set it to False 
    cookie_httponly=True,
    cookie_samesite="none") # development set it to lax 

auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

# ──────────────────────────────────────────────────────────────
# Authentication & Users Routers
# ──────────────────────────────────────────────────────────────

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(schemas.UserRead, schemas.UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(schemas.UserRead, schemas.UserUpdate),
    prefix="/users",
    tags=["users"],
)

@auth_router.post("/auth/logout")
async def logout(response: Response):
    cookie_transport.remove_login_cookie(response)
    return {"message": "Logged out"}
    


# ──────────────────────────────────────────────────────────────
# Middleware
# ──────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173", "https://coffeecli-frontend.onrender.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────────────────────
# Startup
# ──────────────────────────────────────────────────────────────

@app.on_event("startup")
async def on_startup():
    """Initialize database connection."""
    await init_db()

@app.get("/")
def read_root():
    return {"message": "☕ Coffee API is alive!"}

# ──────────────────────────────────────────────────────────────
# Recipes Endpoints
# ──────────────────────────────────────────────────────────────

@app.post("/recipes", response_model=schemas.Recipe, status_code=201, tags=["recipes"])
async def create_recipe(
    recipe: schemas.RecipeCreate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Create a new recipe owned by the current user."""
    return await crud.create_recipe(db, recipe, user)


@app.get("/recipes", response_model=list[schemas.Recipe], tags=["recipes"])
async def list_recipes(db: AsyncSession = Depends(get_async_session)):
    """List all available recipes."""
    result = await db.execute(select(models.Recipe))
    return result.scalars().all()


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["recipes"])
async def get_recipe(recipe_id: int, db: AsyncSession = Depends(get_async_session)):
    """Retrieve a single recipe by ID."""
    recipe = await db.get(models.Recipe, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@app.get("/recipes/search", response_model=list[schemas.Recipe], tags=["recipes"])
async def search_recipes(
    name: Optional[str] = Query(None, description="Filter by recipe name"),
    method: Optional[str] = Query(None, description="Filter by brewing method"),
    max_time: Optional[int] = Query(None, description="Filter by maximum brew time (minutes)"),
    db: AsyncSession = Depends(get_async_session),
):
    """Search for recipes by name, method, or brew time."""
    query = select(models.Recipe)
    if name:
        for word in name.strip().split():
            query = query.filter(models.Recipe.name.ilike(f"%{word}%"))
    if method:
        query = query.filter(func.lower(models.Recipe.method) == method.lower())

    result = await db.execute(query)
    recipes = result.scalars().all()

    if max_time:
        recipes = [r for r in recipes if r.brew_time and parse_brew_time(r.brew_time) <= max_time * 60]

    return recipes


@app.get("/recipes/random", response_model=schemas.Recipe, tags=["recipes"])
async def random_recipe(db: AsyncSession = Depends(get_async_session)):
    """Get a random recipe (excluding cold brew)."""
    result = await db.execute(
        select(models.Recipe)
        .filter(func.lower(models.Recipe.method) != "cold brew")
        .order_by(func.random())
        .limit(1)
    )
    recipe = result.scalars().first()
    if not recipe:
        raise HTTPException(status_code=404, detail="No recipes available")
    return recipe


# ──────────────────────────────────────────────────────────────
# User-Specific Recipes
# ──────────────────────────────────────────────────────────────

@app.get("/users/me/recipes", response_model=list[schemas.Recipe], tags=["users"])
async def get_my_recipes(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),
):
    """List recipes created by the logged-in user."""
    result = await db.execute(select(models.Recipe).filter(models.Recipe.user_id == user.id))
    return result.scalars().all()


# ──────────────────────────────────────────────────────────────
# Favorites Endpoints
# ──────────────────────────────────────────────────────────────

@app.post("/users/me/favorites/{recipe_id}", status_code=201, tags=["favorites"])
async def add_favorite(
    recipe_id: int,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),
):
    """Add a recipe to your favorites."""
    # Check if recipe already favorited via async query
    result = await db.execute(
        select(models.favorites_table).where(
            models.favorites_table.c.user_id == user.id,
            models.favorites_table.c.recipe_id == recipe_id,
        )
    )
    existing_fav = result.first()
    if existing_fav:
        raise HTTPException(status_code=400, detail="Already in favorites")

    # Add to favorites manually
    await db.execute(
        models.favorites_table.insert().values(user_id=user.id, recipe_id=recipe_id)
    )
    await db.commit()

    return {"message": f"'{recipe.name}' added to favorites."}


@app.delete("/users/me/favorites/{recipe_id}", status_code=204, tags=["favorites"])
async def remove_favorite(
    recipe_id: int,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),
):
    """Remove a recipe from your favorites."""
    recipe = await db.get(models.Recipe, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    result = await db.execute(
        select(models.favorites_table).where(
            models.favorites_table.c.user_id == user.id,
            models.favorites_table.c.recipe_id == recipe_id,
        )
    )
    if not result.first():
        raise HTTPException(status_code=400, detail="Not in favorites")

    await db.execute(
        models.favorites_table.delete().where(
            models.favorites_table.c.user_id == user.id,
            models.favorites_table.c.recipe_id == recipe_id,
        )
    )
    await db.commit()
    return {"message": f"'{recipe.name}' removed from favorites."}


@app.get("/users/me/favorites", response_model=list[schemas.Recipe], tags=["favorites"])
async def list_favorites(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_async_session),
):
    """List all favorite recipes for the current user."""
    result = await db.execute(
        select(models.Recipe)
        .join(models.favorites_table)
        .where(models.favorites_table.c.user_id == user.id)
    )
    return result.scalars().all()



# ──────────────────────────────────────────────────────────────
# Utility
# ──────────────────────────────────────────────────────────────

def parse_brew_time(time_str: str) -> int:
    """Convert brew time string (e.g. '2:30', '3m', '1h') to seconds."""
    if "-" in time_str:
        time_str = time_str.split("-")[-1].strip()

    if "h" in time_str:
        return int(time_str.replace("h", "").strip()) * 3600

    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        return int(minutes) * 60 + int(seconds)

    return int(time_str) * 60


app.include_router(auth_router)