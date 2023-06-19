from fastapi import HTTPException
from core.models.group import Group
from core.schemas.group import GroupCreate, GroupUpdate
from sqlalchemy.orm import Session


def create_group(data: GroupCreate, db: Session):
    group = Group(
        title=data.title,
        quantity_people=data.quantity_people,
        func_list=data.func_list
    )
    db.add(group)
    db.commit()
    db.refresh(group)

    return group


def get_group(id: int, db: Session):
    group = db.query(Group).filter(Group.id == id).first()
    if not group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return group


def get_all_group(db: Session):
    return db.query(Group).all()


def update_group(data: GroupUpdate, db: Session, id: int):
    group = db.query(Group).filter(Group.id == id).first()

    if not group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    group_data = data.dict(exclude_unset=True)
    for key, value in group_data.items():
        setattr(group, key, value)
    db.add(group)
    db.commit()
    db.refresh(group)

    return group


def remove_group(id: int, db: Session):
    group = db.query(Group).filter(Group.id == id).first()

    if not group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(group)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


