from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.reference_models import Species, Breed, VaccineType
from app.models.pet import Pet
from app.models.vaccine import Vaccine
from app.models.adoption_center import AdoptionCenter
from app.models.adoption_status import AdoptionStatus