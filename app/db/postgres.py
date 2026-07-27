from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator
from app.config import settings
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URL = (
    settings.postgres_url
    .replace("postgresql://", "postgresql+asyncpg://", 1)
    .split("?")[0]  # strip query params like ?sslmode=require
)

engine = create_async_engine(
    url=DATABASE_URL,
    echo=(settings.environment == "development"),
    connect_args={"ssl": "require"},
)

async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session