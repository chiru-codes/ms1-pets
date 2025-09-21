import random
from faker import Faker
from sqlalchemy.orm import Session
from app.db import session
from app.models.reference_models import Species, VaccineType
from app.models import AdoptionCenter, AdoptionStatus, AdoptionState, Pet, Vaccine

fake = Faker("es_ES")

NUM_CENTERS = 200
NUM_PETS = 20000


def seed_massive():
    session.init_db()
    db: Session = session.SessionLocal()

    centers = []
    for _ in range(NUM_CENTERS):
        center = AdoptionCenter(
            name=fake.company(),
            address=fake.address(),
            city=fake.city(),
            lat=float(fake.latitude()),
            lon=float(fake.longitude())
        )
        db.add(center)
        centers.append(center)

    db.flush()

    species_list = db.query(Species).all()
    breeds_by_species = {
        s.id: [b.id for b in s.breeds] for s in species_list
    }
    vaccine_types = db.query(VaccineType).all()

    pets = []
    for _ in range(NUM_PETS):
        species = random.choice(species_list)
        breed_id = random.choice(breeds_by_species[species.id]) if breeds_by_species[species.id] else None

        birth_date = fake.date_between(start_date="-15y", end_date="today")
        pet = Pet(
            name=fake.first_name(),
            species_id=species.id,
            breed_id=breed_id,
            birth_date=birth_date,
            adoption_center_id=random.choice(centers).id,
        )
        db.add(pet)
        pets.append(pet)

    db.flush()

    for pet in pets:
        status = AdoptionStatus(
            pet_id=pet.id,
            estado=random.choice(list(AdoptionState)),
            fecha_actualizacion=fake.date_time_between(start_date="-2y", end_date="now"),
        )
        db.add(status)

    db.flush()

    for pet in pets:
        num_vaccines = random.randint(0, 5)
        for _ in range(num_vaccines):
            vt = random.choice(vaccine_types)
            vaccine = Vaccine(
                pet_id=pet.id,
                type_id=vt.id,
                date=fake.date_between(start_date=pet.birth_date, end_date="today"),
            )
            db.add(vaccine)

    db.commit()
    db.close()
    print(f"Se generaron {NUM_CENTERS} centros, {NUM_PETS} mascotas, estados y vacunas.")


if __name__ == "__main__":
    seed_massive()
