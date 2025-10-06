from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Column, ForeignKey, Table
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
import uuid

# Association table for many-to-many (favorites)
favorites_table = Table(
    "favorites",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
)

class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    method: Mapped[str] = mapped_column(String(50), nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    steps: Mapped[str] = mapped_column(Text, nullable=False)
    brew_time: Mapped[str] = mapped_column(String(50), nullable=True)

    # ✅ Add foreign key
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship("User", back_populates="recipes")

    # ✅ Reverse relation for favorites
    favorited_by = relationship("User", secondary=favorites_table, back_populates="favorites")


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)

    # ✅ One-to-many with Recipe
    recipes = relationship("Recipe", back_populates="user")

    # ✅ Many-to-many favorites
    favorites = relationship("Recipe", secondary=favorites_table, back_populates="favorited_by")