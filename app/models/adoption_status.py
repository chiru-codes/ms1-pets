import enum
import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base


class AdoptionState(enum.Enum):
    available = "available"
    in_process = "in_process"
    adopted = "adopted"


class AdoptionStatus(Base):
    __tablename__ = "adoption_status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey("pet.id"), nullable=False, unique=True)

    state = Column(Enum(AdoptionState), nullable=False, default=AdoptionState.available)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    # Relación 1:1 -> cada mascota tiene un estado de adopción único
    pet = relationship("Pet", back_populates="adoption_status")

    def __init__(self, pet_id, state=None):
        self.pet_id = pet_id
        self.state = state or AdoptionState.available
        self.last_updated = datetime.datetime.utcnow()

    def __repr__(self):
        return (
            f"<AdoptionStatus(pet_id={self.pet_id}, "
            f"state={self.state.name}, "
            f"last_updated={self.last_updated})>"
        )
