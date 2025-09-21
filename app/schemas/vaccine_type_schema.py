from pydantic import BaseModel


class VaccineTypeBase(BaseModel):
    name: str


class VaccineTypeCreate(VaccineTypeBase):
    pass


class VaccineTypeResponse(VaccineTypeBase):
    id: int

    class Config:
        orm_mode = True
