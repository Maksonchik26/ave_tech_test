from fastapi import Depends
from redis.asyncio.client import Redis

from app.db.redis_client import get_redis


class CRUD:
    def __init__(self, r: Redis = Depends(get_redis)):
        """
        Initializes the CRUD class with the provided redis client.

        Parameters:
            r (Redis): The redis client to use for database operations.
        """
        self.r = r
