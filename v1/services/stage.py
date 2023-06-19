from fastapi import HTTPException

from core.models.stage import Stage
from core.schemas.stage import StageCreate, StageUpdate
from sqlalchemy.orm import Session


def create_stage(data: StageCreate, db: Session):
    stage = Stage(
        id_project=data.id_project,
        title=data.title,
        date_start=data.date_start,
        date_finish=data.date_finish
    )
    db.add(stage)
    db.commit()
    db.refresh(stage)

    return stage


def get_stage_by_id_project(id_project: int, db: Session):
    stages = db.query(Stage).filter(Stage.id_project == id_project)


def get_stage(id: int, db: Session):
    stage = db.query(Stage).filter(Stage.id == id).first()
    if not stage:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return stage


def get_all_stage(db: Session):
    return db.query(Stage).all()


def update_stage(data: StageUpdate, db: Session, id: int):
    stage = db.query(Stage).filter(Stage.id == id).first()

    if not stage:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    stage_data = data.dict(exclude_unset=True)
    for key, value in stage_data.items():
        setattr(stage, key, value)
    db.add(stage)
    db.commit()
    db.refresh(stage)

    return stage


def remove_stage(id: int, db: Session):
    stage = db.query(Stage).filter(Stage.id == id).first()

    if not stage:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(stage)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


