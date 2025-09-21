from pydantic import BaseModel
from typing import Optional


class AdoptionCenterBase(BaseModel):
    name: str
    address: str
    city: str
    lat: Optional[float] = None
    lon: Optional[float] = None


class AdoptionCenterCreate(AdoptionCenterBase):
    pass


class AdoptionCenterUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None


class AdoptionCenterResponse(AdoptionCenterBase):
    id: int

    class Config:
        orm_mode = True
