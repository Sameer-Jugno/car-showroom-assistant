from typing import Optional

from sqlalchemy import select, func, or_

from app.db.postgres import async_session_factory
from app.models.inventory import Inventory


async def search_inventory(
    name: Optional[str] = None,
    max_price: Optional[int] = None,
    fuel: Optional[str] = None,
    transmission: Optional[str] = None,
    limit: int = 10,
):
    stmt = select(Inventory).limit(limit)

    if name is not None:
        words = name.lower().split()
        conditions = [func.lower(Inventory.name).contains(word) for word in words]
        stmt = stmt.where(or_(*conditions))

    if max_price is not None:
        stmt = stmt.where(Inventory.selling_price <= max_price)
    if fuel is not None:
        stmt = stmt.where(func.lower(Inventory.fuel) == fuel.lower())
    if transmission is not None:
        stmt = stmt.where(func.lower(Inventory.transmission) == transmission.lower())

    async with async_session_factory() as session:
        result = await session.execute(stmt)
        cars = result.scalars().all()

    return [
        {
            "name": car.name, "year": car.year, "selling_price": car.selling_price,
            "km_driven": car.km_driven, "fuel": car.fuel,
            "transmission": car.transmission, "owner": car.owner,
        }
        for car in cars
    ]