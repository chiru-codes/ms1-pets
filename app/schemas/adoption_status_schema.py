from pydantic import BaseModel
from datetime import datetime
from app.models.adoption_status import AdoptionState


class AdoptionStatusBase(BaseModel):
    estado: AdoptionState


class AdoptionStatusCreate(AdoptionStatusBase):
    pet_id: int


class AdoptionStatusUpdate(BaseModel):
    estado: AdoptionState


class AdoptionStatusResponse(AdoptionStatusBase):
    id: int
    pet_id: int
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
