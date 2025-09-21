import datetime
from app.models.vaccine import Vaccine
from app.models.reference_models import VaccineType


def test_vaccine_repr_without_type():
    v = Vaccine(id=1, pet_id=10, type_id=2, date=datetime.date.today())
    text = repr(v)
    assert "pet_id=10" in text
    assert "type='?'" in text


def test_vaccine_type_repr():
    vt = VaccineType(id=1, name="Rabies")
    text = repr(vt)
    assert "Rabies" in text
