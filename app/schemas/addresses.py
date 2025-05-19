from pydantic import BaseModel, constr, Field


class AddressIn(BaseModel):
    phone: str = Field(
        ...,
        pattern=r'^8\d{10}$',
        example='89990005555'
    )
    address: str = Field(..., example="ул. Ленина, д. 10")


class AddressOut(BaseModel):
    phone: str = Field(example='89990005555')
    address: str = Field(..., example="ул. Ленина, д. 10")

    class ConfigDict:
        from_attributes = True
