import uuid
from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_async_session
from api.models import User
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET")

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
    
class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    
async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
    