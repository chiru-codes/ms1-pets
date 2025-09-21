from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    breeds = relationship("Breed", back_populates="species")
    pets = relationship("Pet", back_populates="species")

    def __repr__(self):
        return f"<Species(id={self.id}, name='{self.name}')>"


class Breed(Base):
    __tablename__ = "breed"

    id = Column(Integer, primary_key=True, autoincrement=True)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)
    name = Column(String(50), nullable=False)

    species = relationship("Species", back_populates="breeds")
    pets = relationship("Pet", back_populates="breed")

    def __repr__(self):
        return f"<Breed(id={self.id}, name='{self.name}', species_id={self.species_id})>"


class VaccineType(Base):
    __tablename__ = "vaccine_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    # Relación 1:N -> un tipo de vacuna puede estar en muchas vacunas aplicadas
    vaccines = relationship("Vaccine", back_populates="type")

    def __repr__(self):
        return f"<VaccineType(id={self.id}, name='{self.name}')>"
