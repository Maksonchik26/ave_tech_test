import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from fakeredis.aioredis import FakeRedis

from main import app
from db.redis_client import get_redis


@pytest.mark.asyncio
async def test_write_and_read_address():
    fake_redis = FakeRedis(decode_responses=True)

    app.dependency_overrides[get_redis] = lambda: fake_redis

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {
            "phone": "1234567890",
            "address": "Test street"
        }

        # Тест на запись адреса
        post_resp = await client.post("/write_data", json=payload)
        assert post_resp.status_code == 200
        assert post_resp.json() == payload

        # Тест на чтение адреса
        get_resp = await client.get("/check_data", params={"phone": "1234567890"})
        assert get_resp.status_code == 200
        assert get_resp.json() == payload

    app.dependency_overrides.clear()
    await fake_redis.aclose()


@pytest.mark.asyncio
async def test_not_found_address():
    fake_redis = FakeRedis(decode_responses=True)

    app.dependency_overrides[get_redis] = lambda: fake_redis

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/check_data", params={"phone": "0000000000"})
        assert resp.status_code == 404
        assert resp.json()["detail"] == "Телефон не найден"

    app.dependency_overrides.clear()
    await fake_redis.aclose()


@pytest.mark.asyncio
async def test_invalid_phone_length():
    fake_redis = FakeRedis(decode_responses=True)

    app.dependency_overrides[get_redis] = lambda: fake_redis

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/check_data", params={"phone": "123"})
        assert resp.status_code == 422
        assert any(
            "String should have at least 10 characters" in err["msg"] for err in resp.json().get("detail", [])
        )

    app.dependency_overrides.clear()
    await fake_redis.aclose()
