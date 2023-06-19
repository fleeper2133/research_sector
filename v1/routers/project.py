from fastapi import APIRouter, Depends

from core.schemas.project import ProjectCreate
from datebase import get_db
from v1.services.project import *

router = APIRouter()


@router.post('/', tags=['Проект'])
async def create(data: ProjectCreate = Depends(ProjectCreate.as_form), db: Session = Depends(get_db)):
    return create_project(data, db)


@router.get('/{id}', tags=['Проект'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_project(id, db)


@router.get('/',  tags=['Проект'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_project(db)


@router.put('/{id}', tags=['Проект'])
async def update(id: int = None, data: ProjectUpdate = Depends(ProjectUpdate.as_form), db: Session = Depends(get_db)):
    return update_project(data, db, id)


@router.delete('/{id}', tags=['Проект'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_project(id, db)


