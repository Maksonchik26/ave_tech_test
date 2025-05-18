from pydantic import BaseModel


class PhoneData(BaseModel):
    phone: str
    address: str
