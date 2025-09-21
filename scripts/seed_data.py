from faker import Faker
from sqlalchemy.orm import Session
from app.db import session
from app.models.reference_models import VaccineType, Breed, Species

fake = Faker("es_ES")


def seed_data():
    session.init_db()
    db: Session = session.SessionLocal()

    species_list = [
        "Perro",
        "Gato",
        "Conejo",
        "Hámster",
        "Periquito",
        "Loro",
        "Cuy"
    ]

    species_objects = {}
    for s in species_list:
        obj = Species(name=s)
        db.add(obj)
        species_objects[s] = obj

    db.flush()

    breeds_by_species = {
        "Perro": [
            "Mestizo", "Sin raza definida",
            "Labrador Retriever", "Pastor Alemán", "Bulldog", "Poodle", "Chihuahua",
            "Beagle", "Husky Siberiano", "Golden Retriever", "Boxer", "Shar Pei",
            "Dálmata", "Shih Tzu", "Doberman", "Rottweiler"
        ],
        "Gato": [
            "Mestizo", "Sin raza definida",
            "Persa", "Siames", "Maine Coon", "Bengalí", "Sphynx",
            "Europeo Común", "Angora", "Azul Ruso",
            "Blanco", "Negro", "Atigrado", "Carey"
        ],
        "Conejo": [
            "Mestizo", "Sin raza definida",
            "Mini Lop", "Rex", "Angora", "Holandés enano", "Cabeza de León",
            "Blanco", "Marrón", "Manchado"
        ],
        "Hámster": [
            "Mestizo", "Sin raza definida",
            "Sirio", "Ruso", "Roborovski", "Chino",
            "Blanco", "Dorado", "Gris"
        ],
        "Periquito": [
            "Común", "Inglés", "Arcoíris",
            "Verde", "Amarillo", "Azul", "Manchado"
        ],
        "Loro": [
            "Amazona", "Guacamayo", "Cacatúa", "Youyou", "Eclectus",
            "Verde", "Rojo", "Azul"
        ],
        "Cuy": [
            "Mestizo", "Sin raza definida",
            "Peruano", "Abyssinian", "Americano", "Sheltie", "Texel",
            "Corto", "Largo", "Tricolor", "Blanco", "Marrón"
        ]
    }

    for species_name, breed_list in breeds_by_species.items():
        species_obj = species_objects[species_name]
        for breed_name in breed_list:
            db.add(Breed(name=breed_name, species_id=species_obj.id))

    vaccine_types = [
        # Perros
        "Rabia (Perros y Gatos)",
        "Parvovirus",
        "Moquillo",
        "Hepatitis infecciosa canina",
        "Leptospirosis",

        # Gatos
        "Leucemia felina",
        "Panleucopenia felina",
        "Calicivirus felino",
        "Herpesvirus felino",

        # Conejos
        "Mixomatosis",
        "Enfermedad vírica hemorrágica (EVH)",

        # Aves
        "Poliomavirus (aves)",
        "Psitacosis",

        # Roedores
        "Pasteurelosis (roedores)"
    ]

    for v in vaccine_types:
        db.add(VaccineType(name=v))

    db.commit()
    db.close()
    print("Datos iniciales insertados correctamente.")


if __name__ == "__main__":
    seed_data()
