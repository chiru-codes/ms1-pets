from pydantic import BaseModel
from datetime import datetime
from app.models.adoption_status import AdoptionState


class AdoptionStatusBase(BaseModel):
    state: AdoptionState


class AdoptionStatusCreate(AdoptionStatusBase):
    pet_id: int


class AdoptionStatusUpdate(BaseModel):
    state: AdoptionState


class AdoptionStatusResponse(AdoptionStatusBase):
    id: int
    pet_id: int
    last_updated: datetime

    class Config:
        orm_mode = True
