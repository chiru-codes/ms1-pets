import datetime
from app.models.adoption_status import AdoptionStatus, AdoptionState


def test_default_adoption_status():
    status = AdoptionStatus(pet_id=1)
    assert status.pet_id == 1
    assert status.state == AdoptionState.available
    assert isinstance(status.last_updated, datetime.datetime)


def test_repr_contains_fields():
    status = AdoptionStatus(pet_id=2, state=AdoptionState.in_process)
    text = repr(status)
    assert "pet_id=2" in text
    assert "state=in_process" in text
