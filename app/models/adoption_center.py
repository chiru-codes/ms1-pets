from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base import Base


class AdoptionCenter(Base):
    __tablename__ = "adoption_center"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    city = Column(String(100), nullable=False)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)

    # Relación 1:N -> un centro de adopción tiene muchas mascotas
    pets = relationship("Pet", back_populates="adoption_center")
