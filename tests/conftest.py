import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient
import pytest

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from fastapi.testclient import TestClient

from src import global_config
from src.migrations.db_metadata import metadata
from src.api.auth.models import get_async_session
from src.main import app


DATABASE_URL_TEST = (
    "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
        global_config.TEST_DB_USER,
        global_config.TEST_DB_PASSWORD,
        global_config.TEST_DB_HOST,
        global_config.TEST_DB_PORT,
        global_config.TEST_DB_NAME
    )
)

test_engine = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
test_async_session_maker = async_sessionmaker(
    test_engine, expire_on_commit=False
        )
# TODO metadata.bind = test_engine


async def get_test_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with test_async_session_maker() as Session:
        yield Session

app.dependency_overrides[get_async_session] = test_async_session_maker


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    try:
        async with test_engine.begin() as conn:
            await conn.run_sync(metadata.create_all)
        yield
    finally:
        async with test_engine.begin() as conn:
            await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
async def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://api") as ac:
        yield ac
