import redis


# Redis client (можно также обернуть в async, но для простоты используем sync)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)