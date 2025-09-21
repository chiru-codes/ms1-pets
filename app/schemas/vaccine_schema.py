from pydantic import BaseModel
from datetime import date
from typing import Optional


class VaccineBase(BaseModel):
    pet_id: int
    type_id: int
    date: date


class VaccineCreate(VaccineBase):
    pass


class VaccineUpdate(BaseModel):
    type_id: Optional[int] = None
    date: Optional[date] = None


class VaccineResponse(VaccineBase):
    id: int

    class Config:
        orm_mode = True
