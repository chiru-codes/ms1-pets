"""
Paquete de modelos SQLAlchemy para el microservicio de Mascotas.
Aquí se importan todos los modelos para que puedan ser registrados
en el metadata de SQLAlchemy y usados fácilmente en otros módulos.
"""

from app.models.pet import Pet
from app.models.adoption_center import AdoptionCenter
from app.models.adoption_status import AdoptionStatus, AdoptionState
from app.models.vaccine import Vaccine
from app.models.reference_models import Species, Breed, VaccineType

__all__ = [
    "Pet",
    "AdoptionCenter",
    "AdoptionStatus",
    "AdoptionState",
    "Vaccine",
    "VaccineType",
    "Species",
    "Breed",
]
