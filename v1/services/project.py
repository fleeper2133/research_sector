from fastapi import HTTPException
from core.models.project import Project
from core.schemas.project import ProjectCreate, ProjectUpdate
from sqlalchemy.orm import Session


def create_project(data: ProjectCreate, db: Session):
    project = Project(
        title=data.title,
        direction=data.direction,
        date_start=data.date_start,
        date_finish=data.date_finish
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_project(id: int, db: Session):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return project


def get_all_project(db: Session):
    return db.query(Project).all()


def update_project(data: ProjectUpdate, db: Session, id: int):
    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    project_data = data.dict(exclude_unset=True)
    for key, value in project_data.items():
        setattr(project, key, value)
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def remove_project(id: int, db: Session):
    project = db.query(Project).filter(Project.id == id).first()

    if not project:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(project)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


