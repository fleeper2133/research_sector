from fastapi import APIRouter, Depends

from datebase import get_db
from v1.services.operation import *

router = APIRouter()


@router.post('/', tags=['Операция'])
async def create(data: OperationCreate = Depends(OperationCreate.as_form), db: Session = Depends(get_db)):
    return create_operation(data, db)


@router.get('/{id}', tags=['Операция'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_operation(id, db)


@router.get('/',  tags=['Операция'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_operation(db)


@router.put('/{id}', tags=['Операция'])
async def update(id: int = None, data: OperationUpdate = Depends(OperationUpdate.as_form), db: Session = Depends(get_db)):
    return update_operation(data, db, id)


@router.delete('/{id}', tags=['Операция'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_operation(id, db)


