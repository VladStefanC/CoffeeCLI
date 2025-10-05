from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
import uuid


class Recipe(Base):
    __tablename__ = "recipes"
   
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index= True)
    method: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    steps: Mapped[str] = mapped_column(Text,nullable=False)
    brew_time : Mapped[str] = mapped_column(String(50), nullable=False) 
    
class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    username : Mapped[str] = mapped_column(String(100), nullable = True, unique=True)

    
    
    