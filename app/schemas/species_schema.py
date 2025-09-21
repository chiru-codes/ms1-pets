from pydantic import BaseModel


class SpeciesBase(BaseModel):
    name: str


class SpeciesCreate(SpeciesBase):
    pass


class SpeciesResponse(SpeciesBase):
    id: int

    class Config:
        orm_mode = True
