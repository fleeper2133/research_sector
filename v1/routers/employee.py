from fastapi import APIRouter, Depends

from datebase import get_db
from v1.services.employee import *

router = APIRouter()


@router.post('/', tags=['Сотрудник'])
async def create(data: EmployeeCreate = Depends(EmployeeCreate.as_form), db: Session = Depends(get_db)):

    return create_employee(data, db)


@router.get('/{id}', tags=['Сотрудник'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_employee(id, db)


@router.get('/',  tags=['Сотрудник'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_employee(db)


@router.put('/{id}', tags=['Сотрудник'])
async def update(id: int = None, data: EmployeeUpdate = Depends(EmployeeUpdate.as_form), db: Session = Depends(get_db)):
    return update_employee(data, db, id)


@router.delete('/{id}', tags=['Сотрудник'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_employee(id, db)


