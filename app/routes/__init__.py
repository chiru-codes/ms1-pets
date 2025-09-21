"""
Paquete de routers de FastAPI para el microservicio de Mascotas.
Centraliza todos los endpoints disponibles.
"""

from app.routes import pets
from app.routes import centers
from app.routes import vaccines
from app.routes import status

__all__ = ["pets", "centers", "vaccines", "status"]
