from pydantic import BaseModel, constr, Field


class AddressIn(BaseModel):
    phone: str = Field(
        ...,
        pattern=r'^\+7\d{10}$',
        example='+71234567890'
    )
    address: str = Field(..., example="ул. Ленина, д. 10")


class AddressOut(BaseModel):
    phone: str = Field(example='+71234567890')
    address: str = Field(..., example="ул. Ленина, д. 10")

    class ConfigDict:
        from_attributes = True
