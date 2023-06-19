from fastapi import HTTPException
from core.models.operation import Operation
from core.schemas.operation import OperationCreate, OperationUpdate
from sqlalchemy.orm import Session



def create_operation(data: OperationCreate, db: Session):
    operation = Operation(
        title=data.title,
        date_start=data.date_start,
        date_finish=data.date_finish
    )
    db.add(operation)
    db.commit()
    db.refresh(operation)

    return operation


def get_operation(id: int, db: Session):
    operation = db.query(Operation).filter(Operation.id == id).first()
    if not operation:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")
    return operation


def get_all_operation(db: Session):
    return db.query(Operation).all()


def update_operation(data: OperationUpdate, db: Session, id: int):
    operation = db.query(Operation).filter(Operation.id == id).first()

    if not operation:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    operation_data = data.dict(exclude_unset=True)
    for key, value in operation_data.items():
        setattr(operation, key, value)
    db.add(operation)
    db.commit()
    db.refresh(operation)

    return operation


def remove_operation(id: int, db: Session):
    operation = db.query(Operation).filter(Operation.id == id).first()

    if not operation:
        raise HTTPException(status_code=404, detail=f"Item with id = {id} not found!")

    db.delete(operation)
    db.commit()
    return {f"Пользователь с id = {id} успешно удален!"}


