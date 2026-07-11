import asyncio

from app.db.postgres import engine, Base
from app.models.inventory import Inventory  # noqa: F401 — import so it registers with Base.metadata


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")


asyncio.run(create_tables())