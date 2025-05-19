import os

from redis.asyncio.client import Redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r: Redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


async def get_redis() -> Redis:
    return r
