from collections.abc import AsyncIterator
import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


load_dotenv()

DB_URL = os.getenv(
    "DB_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
)


async_engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
