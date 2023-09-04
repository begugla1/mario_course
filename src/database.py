from typing import AsyncGenerator
import os

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    os.environ.get("DB_USER", "postgres"),
    os.environ.get("DB_PASSWORD", "postgres"),
    os.environ.get("DB_HOST", "database"),
    os.environ.get("DB_PORT", "5432"),
    os.environ.get("DB_NAME", "postgres"),
)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as Session:
        yield Session
