import asyncio
from app.db.redis import redis_client


async def test_connection():
    pong = await redis_client.ping()
    print("Redis connection successful:", pong)


asyncio.run(test_connection())