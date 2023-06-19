from fastapi import HTTPException
from core.models.employee_group import EmployeeGroup
from core.schemas.employee_group import EmployeeGroupCreate, EmployeeGroupUpdate
from sqlalchemy.orm import Session


def create_employee_group(data: EmployeeGroupCreate, db: Session):
    employee_group = EmployeeGroup(
        id_group=data.id_group,
        id_employee=data.id_employee,
        date_connect=data.date_connect,
        date_disconnect=data.date_disconnect
    )
    db.add(employee_group)
    db.commit()
    db.refresh(employee_group)

    return employee_group


def get_employee_group(id: int, db: Session):
    employee_group = db.query(EmployeeGroup).filter(EmployeeGroup.id == id).first()
    if not employee_group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return employee_group


def get_all_employee_group(db: Session):
    return db.query(EmployeeGroup).all()


def update_employee_group(data: EmployeeGroupUpdate, db: Session, id: int):
    employee_group = db.query(EmployeeGroup).filter(EmployeeGroup.id == id).first()

    if not employee_group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    employee_group_data = data.dict(exclude_unset=True)
    for key, value in employee_group_data.items():
        setattr(employee_group, key, value)
    db.add(employee_group)
    db.commit()
    db.refresh(employee_group)

    return employee_group


def remove_employee_group(id: int, db: Session):
    employee_group = db.query(EmployeeGroup).filter(EmployeeGroup.id == id).first()

    if not employee_group:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(employee_group)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


