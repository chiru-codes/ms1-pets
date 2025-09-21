from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Vaccine(Base):
    __tablename__ = "vaccine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey("pet.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("vaccine_type.id"), nullable=False)
    date = Column(Date, nullable=False)

    # Relación N:1 -> una vacuna pertenece a una mascota
    pet = relationship("Pet", back_populates="vaccines")
    type = relationship("VaccineType", back_populates="vaccines")

    def __repr__(self):
        type_name = self.type.name if self.type else "?"
        return f"<Vaccine(id={self.id}, type='{type_name}', date={self.date}, pet_id={self.pet_id})>"
