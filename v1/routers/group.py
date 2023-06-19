from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from datebase import get_db
from core.schemas.group import GroupCreate, GroupUpdate
from v1.services.group import create_group, get_group, get_all_group, update_group, remove_group

router = APIRouter()


@router.post('/', tags=['Группа'])
async def create(data: GroupCreate = Depends(GroupCreate.as_form), db: Session = Depends(get_db)):
    return create_group(data, db)


@router.get('/{id}', tags=['Группа'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_group(id, db)


@router.get('/',  tags=['Группа'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_group(db)


@router.put('/{id}', tags=['Группа'])
async def update(id: int = None, data: GroupUpdate = Depends(GroupUpdate.as_form), db: Session = Depends(get_db)):
    return update_group(data, db, id)


@router.delete('/{id}', tags=['Группа'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_group(id, db)


