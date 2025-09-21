from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index, Date
from sqlalchemy.orm import relationship
from app.db.base import Base
import datetime


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)
    breed_id = Column(Integer, ForeignKey("breed.id"), nullable=False)
    birth_date = Column(Date, nullable=False)
    adoption_center_id = Column(Integer, ForeignKey("adoption_center.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)

    # Relación 1:N -> una mascota pertenece a un centro de adopción
    adoption_center = relationship("AdoptionCenter", back_populates="pets")

    # Relación 1:N -> una mascota puede tener varias vacunas
    vaccines = relationship("Vaccine", back_populates="pet", cascade="all, delete-orphan")

    # Relación 1:1 -> cada mascota tiene un único estado de adopción actual
    adoption_status = relationship("AdoptionStatus", back_populates="pet", uselist=False)

    # Relación 1:1 -> cada mascota tiene una especie única
    species = relationship("Species", back_populates="pets")

    # Relación 1:1 -> cada mascota tiene una raza
    breed = relationship("Breed", back_populates="pets")

    __table_args__ = (
        Index("idx_pet_species_birthdate", "species_id", "birth_date"),
        Index("idx_pet_center", "adoption_center_id"),
    )

    def __repr__(self):
        species_name = self.species.name if self.species else "?"
        breed_name = self.breed.name if self.breed else "?"
        return f"<Pet(id={self.id}, name='{self.name}', species='{species_name}', breed='{breed_name}')>"

    @property
    def age(self) -> str:
        today = datetime.date.today()
        months = (today.year - self.birth_date.year) * 12 + (today.month - self.birth_date.month)

        if months < 12:
            return f"{months} months"
        else:
            years = months // 12
            return f"{years} years"

    @property
    def age_category(self) -> str:
        today = datetime.date.today()
        years = today.year - self.birth_date.year - (
               (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

        if years < 1:
            return "puppy"
        elif 1 <= years <= 7:
            return "adult"
        return "senior"
