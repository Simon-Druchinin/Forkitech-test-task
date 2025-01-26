import asyncio

import pytest
from fastapi.testclient import TestClient

from config.database import Base, engine
from main import app


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    asyncio.run(init_models())


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
