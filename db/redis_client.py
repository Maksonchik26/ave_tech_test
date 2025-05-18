from redis.asyncio.client import Redis

r: Redis = Redis(host='localhost', port=6379, decode_responses=True)


async def get_redis() -> Redis:
    return r
