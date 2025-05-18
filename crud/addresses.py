from schemas.addresses import AddressIn, AddressOut
from fastapi import HTTPException

from crud.common import CRUD


class AddressCRUD(CRUD):
    async def write_or_update(self, data: AddressIn) -> AddressOut:
        await self.r.set(data.phone, data.address)

        return AddressOut(phone=data.phone, address=data.address)

    async def read(self, phone: str) -> AddressOut:
        address = await self.r.get(phone)
        if not address:
            raise HTTPException(status_code=404, detail="Телефон не найден")

        return AddressOut(phone=phone, address=address)
