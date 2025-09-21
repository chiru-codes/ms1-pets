import datetime
from app.models.pet import Pet
from app.models.reference_models import Species, Breed


def test_pet_repr_and_age_category():
    birth_date = datetime.date.today().replace(year=datetime.date.today().year - 3)
    pet = Pet(
        id=1,
        name="Buddy",
        species_id=1,
        breed_id=1,
        birth_date=birth_date,
        adoption_center_id=1,
    )

    assert "years" in pet.age

    assert pet.age_category == "adult"

    text = repr(pet)
    assert "Buddy" in text
    assert "species" in text


def test_species_repr():
    s = Species(id=1, name="Dog")
    text = repr(s)
    assert "Dog" in text


def test_breed_repr():
    b = Breed(id=1, name="Bulldog", species_id=1)
    text = repr(b)
    assert "Bulldog" in text
    assert "species_id=1" in text
