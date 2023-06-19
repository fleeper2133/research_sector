from fastapi import HTTPException

from core.models.phase import Phase
from core.schemas.phase import PhaseCreate, PhaseUpdate
from sqlalchemy.orm import Session


def create_phase(data: PhaseCreate, db: Session):
    phase = Phase(
        id_stage=data.id_stage,
        title=data.title,
        date_start=data.date_start,
        date_finish=data.date_finish
    )
    db.add(phase)
    db.commit()
    db.refresh(phase)

    return phase


def get_phase(id: int, db: Session):
    phase = db.query(Phase).filter(Phase.id == id).first()
    if not phase:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return phase


def get_all_phase(db: Session):
    return db.query(Phase).all()


def update_phase(data: PhaseUpdate, db: Session, id: int):
    phase = db.query(Phase).filter(Phase.id == id).first()

    if not phase:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    phase_data = data.dict(exclude_unset=True)
    for key, value in phase_data.items():
        setattr(phase, key, value)
    db.add(phase)
    db.commit()
    db.refresh(phase)

    return phase


def remove_phase(id: int, db: Session):
    phase = db.query(Phase).filter(Phase.id == id).first()

    if not phase:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(phase)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


