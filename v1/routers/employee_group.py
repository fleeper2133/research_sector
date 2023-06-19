from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from datebase import get_db
from core.schemas.employee_group import EmployeeGroupCreate, EmployeeGroupUpdate
from v1.services.employee_group import create_employee_group, get_employee_group, get_all_employee_group, update_employee_group, remove_employee_group

router = APIRouter()


@router.post('/', tags=['Сотрудник-группа'])
async def create(data: EmployeeGroupCreate = Depends(EmployeeGroupCreate.as_form), db: Session = Depends(get_db)):
    return create_employee_group(data, db)


@router.get('/{id}', tags=['Сотрудник-группа'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_employee_group(id, db)


@router.get('/',  tags=['Сотрудник-группа'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_employee_group(db)


@router.put('/{id}', tags=['Сотрудник-группа'])
async def update(id: int = None, data: EmployeeGroupUpdate = Depends(EmployeeGroupUpdate.as_form), db: Session = Depends(get_db)):
    return update_employee_group(data, db, id)


@router.delete('/{id}', tags=['Сотрудник-группа'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_employee_group(id, db)


