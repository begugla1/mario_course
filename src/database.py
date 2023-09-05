from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import declarative_base

import global_config

DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    global_config.DB_USER,
    global_config.DB_PASSWORD,
    global_config.DB_HOST,
    global_config.DB_PORT,
    global_config.DB_NAME
)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as Session:
        yield Session
