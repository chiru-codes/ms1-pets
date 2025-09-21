from app.services import adoption_center_service
from app.schemas import AdoptionCenterCreate, AdoptionCenterUpdate


def test_create_center(db_session):
    schema = AdoptionCenterCreate(name="Refugio Patitas", address="Av. Siempre Viva 123", city="Springfield")
    center = adoption_center_service.create_center(db_session, schema)
    assert center.id is not None
    assert center.name == "Refugio Patitas"


def test_update_center(db_session):
    schema = AdoptionCenterCreate(name="Refugio Inicial", address="Calle 1", city="Lima")
    center = adoption_center_service.create_center(db_session, schema)

    update_schema = AdoptionCenterUpdate(name="Refugio Renovado")
    updated = adoption_center_service.update_center(db_session, center.id, update_schema)
    assert updated.name == "Refugio Renovado"
