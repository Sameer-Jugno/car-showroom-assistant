# scripts/load_inventory.py

import asyncio

import pandas as pd

from app.db.postgres import async_session_factory
from app.models.inventory import Inventory


async def load_inventory():
    df = pd.read_csv("data/processed/inventory_clean.csv")
    records = df.to_dict(orient="records")

    async with async_session_factory() as session:
        inventory_objects = [Inventory(**record) for record in records]
        session.add_all(inventory_objects)
        await session.commit()

    print(f"Loaded {len(inventory_objects)} records into inventory table.")


asyncio.run(load_inventory())