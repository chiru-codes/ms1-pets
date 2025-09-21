from sqlalchemy.orm import Session
from typing import Optional
from app.models.adoption_status import AdoptionStatus
from app.schemas import AdoptionStatusCreate, AdoptionStatusUpdate


def get_adoption_status(db: Session, pet_id: int) -> Optional[AdoptionStatus]:
    return db.query(AdoptionStatus).filter(AdoptionStatus.pet_id == pet_id).first()


def create_adoption_status(db: Session, status: AdoptionStatusCreate) -> AdoptionStatus:
    db_status = AdoptionStatus(**status.model_dump())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def update_adoption_status(
        db: Session, pet_id: int, status_update: AdoptionStatusUpdate
) -> Optional[AdoptionStatus]:
    db_status: Optional[AdoptionStatus] = (
        db.query(AdoptionStatus).filter(AdoptionStatus.pet_id == pet_id).first()
    )
    if not db_status:
        return None

    for key, value in status_update.model_dump(exclude_unset=True).items():
        setattr(db_status, key, value)

    db.commit()
    db.refresh(db_status)
    return db_status


def delete_adoption_status(db: Session, pet_id: int) -> bool:
    db_status = db.query(AdoptionStatus).filter(AdoptionStatus.pet_id == pet_id).first()
    if not db_status:
        return False

    db.delete(db_status)
    db.commit()
    return True
