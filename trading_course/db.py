import os
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
)
from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine
)
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgres+asyncpg://{}:{}@{}:{}/{}".format(
    os.environ.get("DB_USER", "postgres"),
    os.environ.get("DB_PASSWORD", "postgres"),
    os.environ.get("DB_HOST", "database"),
    os.environ.get("DB_PORT", "5432"),
    os.environ.get("DB_NAME", "postgres"),
)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
