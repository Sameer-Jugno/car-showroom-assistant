from typing import Optional

from sqlalchemy import select, func

from app.db.postgres import async_session_factory
from app.models.inventory import Inventory


async def search_inventory(
    max_price: Optional[int] = None,
    fuel: Optional[str] = None,
    transmission: Optional[str] = None,
):
    stmt = select(Inventory)

    if max_price is not None:
        stmt = stmt.where(Inventory.selling_price <= max_price)

    if fuel is not None:
        stmt = stmt.where(func.lower(Inventory.fuel) == fuel.lower())

    if transmission is not None:
        stmt = stmt.where(func.lower(Inventory.transmission) == transmission.lower())

    async with async_session_factory() as session:
        result = await session.execute(stmt)
        cars = result.scalars().all()

    return cars