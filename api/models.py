from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text

class Base(DeclarativeBase):
    pass


class Recipe(Base):
    __tablename__ = "recipes"
   
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index= True)
    method: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    steps: Mapped[str] = mapped_column(Text,nullable=False)
    brew_time : Mapped[str] = mapped_column(String(50), nullable=False) 
    