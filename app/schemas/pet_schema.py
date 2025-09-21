from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from app.schemas.adoption_status_schema import AdoptionStatusResponse
from app.schemas.vaccine_schema import VaccineResponse

class PetBase(BaseModel):
    name: str
    species_id: int
    breed_id: int
    birth_date: date
    adoption_center_id: int


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    name: Optional[str] = None
    breed_id: Optional[int] = None
    adoption_center_id: Optional[int] = None


class PetResponse(PetBase):
    id: int
    created_at: datetime
    adoption_status: Optional[AdoptionStatusResponse] = None
    vaccines: list[VaccineResponse] = []

    class Config:
        orm_mode = True