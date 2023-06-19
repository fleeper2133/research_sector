from fastapi import HTTPException
from core.models.employee import Employee
from core.schemas.employee import EmployeeCreate, EmployeeUpdate
from sqlalchemy.orm import Session


def create_employee(data: EmployeeCreate, db: Session):
    employee = Employee(
        FIO=data.FIO,
        duty=data.duty,
        qualification=data.qualification
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_employee(id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return employee


def get_all_employee(db: Session):
    return db.query(Employee).all()


def update_employee(data: EmployeeUpdate, db: Session, id: int):
    employee = db.query(Employee).filter(Employee.id == id).first()

    if not employee:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    employee_data = data.dict(exclude_unset=True)
    for key, value in employee_data.items():
        setattr(employee, key, value)
    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def remove_employee(id: int, db: Session):
    employee = db.query(Employee).filter(Employee.id == id).first()

    if not employee:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(employee)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


