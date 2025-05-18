from pydantic import BaseModel, constr

class AddressIn(BaseModel):
    phone: constr(min_length=10, max_length=15)
    address: str


class AddressOut(BaseModel):
    phone: str
    address: str

    class ConfigDict:
        from_attributes = True
