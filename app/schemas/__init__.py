"""
Paquete de schemas Pydantic para el microservicio de Mascotas.
Centraliza los DTOs de entrada/salida para usarlos fácilmente en routers y servicios.
"""

from app.schemas.pet_schema import PetBase, PetCreate, PetUpdate, PetResponse
from app.schemas.adoption_center_schema import (
    AdoptionCenterBase,
    AdoptionCenterCreate,
    AdoptionCenterUpdate,
    AdoptionCenterResponse,
)
from app.schemas.adoption_status_schema import (
    AdoptionStatusBase,
    AdoptionStatusCreate,
    AdoptionStatusUpdate,
    AdoptionStatusResponse,
)
from app.schemas.species_schema import SpeciesBase, SpeciesCreate, SpeciesResponse
from app.schemas.breed_schemas import BreedBase, BreedCreate, BreedResponse
from app.schemas.vaccine_schema import VaccineBase, VaccineCreate, VaccineUpdate, VaccineResponse
from app.schemas.vaccine_type_schema import VaccineTypeBase, VaccineTypeCreate, VaccineTypeResponse

__all__ = [
    # Pet
    "PetBase",
    "PetCreate",
    "PetUpdate",
    "PetResponse",
    # Adoption Center
    "AdoptionCenterBase",
    "AdoptionCenterCreate",
    "AdoptionCenterUpdate",
    "AdoptionCenterResponse",
    # Adoption Status
    "AdoptionStatusBase",
    "AdoptionStatusCreate",
    "AdoptionStatusUpdate",
    "AdoptionStatusResponse",
    # Species
    "SpeciesBase",
    "SpeciesCreate",
    "SpeciesResponse",
    # Breed
    "BreedBase",
    "BreedCreate",
    "BreedResponse",
    # Vaccine
    "VaccineBase",
    "VaccineCreate",
    "VaccineUpdate",
    "VaccineResponse",
    # Vaccine Type
    "VaccineTypeBase",
    "VaccineTypeCreate",
    "VaccineTypeResponse",
]
