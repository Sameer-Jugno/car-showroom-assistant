import asyncio
from app.tools.inventory_tool import search_inventory

async def test():
    cars = await search_inventory(max_price=300000, fuel="Petrol")
    print(f"Found {len(cars)} cars")
    for c in cars[:5]:
        print(c.name, c.selling_price, c.fuel)

asyncio.run(test())