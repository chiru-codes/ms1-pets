from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str
    species_id: int


class BreedCreate(BreedBase):
    pass


class BreedResponse(BreedBase):
    id: int

    class Config:
        orm_mode = True
