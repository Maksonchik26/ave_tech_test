from fastapi import APIRouter, Query, Depends, status

from app.crud.addresses import AddressCRUD
from app.schemas.addresses import AddressIn, AddressOut


router = APIRouter(
    prefix='',
    tags=['addresses']
)


@router.post(
    "/write_data",
    response_model=AddressOut,
    status_code=status.HTTP_200_OK,
    summary="Добавить или обновить адрес по номеру телефона",
    description="Принимает номер телефона и адрес, сохраняет или обновляет запись в Redis по номеру телефона.",
    responses={
        200: {"description": "Адрес успешно добавлен или обновлён"},
        422: {"description": "Ошибка валидации данных"},
    }

)
async def write_data(
    data: AddressIn,
    addresses_crud: AddressCRUD = Depends(),
):
    address = await addresses_crud.write_or_update(data)

    return address


@router.get(
    "/check_data",
    response_model=AddressOut,
    status_code=status.HTTP_200_OK,
    summary="Получить адрес по номеру телефона",
    description="Ищет и возвращает адрес, связанный с указанным номером телефона. Если номер не найден — 404.",
    responses={
        200: {"description": "Адрес найден и возвращён"},
        404: {"description": "Телефон не найден"},
        422: {"description": "Ошибка валидации параметра phone"},
    }
)
async def check_data(
    phone: str = Query(..., min_length=10, max_length=15),
    addresses_crud: AddressCRUD = Depends(),
):
    address = await addresses_crud.read(phone)

    return address
