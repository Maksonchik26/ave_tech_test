from fastapi import APIRouter, HTTPException, Query

from schemas.addresses import PhoneData
from db.redis_client import r

router = APIRouter(
    prefix='',
    tags=['addresses']
)

@router.post("/write_data")
def write_data(data: PhoneData):
    """Добавляет или обновляет адрес по телефону"""

    r.set(data.phone, data.address)
    return {"message": "Данные записаны", "data": data}

@router.get("/check_data")
def check_data(phone: str = Query(..., min_length=10, max_length=15)):
    """Получает адрес по номеру телефона"""

    address = r.get(phone)
    if not address:
        raise HTTPException(status_code=404, detail="Телефон не найден")
    return {"phone": phone, "address": address}