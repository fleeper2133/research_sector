from fastapi import APIRouter, Depends

from datebase import get_db
from v1.services.stage import *

router = APIRouter()


@router.post('/', tags=['Стадия'])
async def create(data: StageCreate = Depends(StageCreate.as_form), db: Session = Depends(get_db)):
    return create_stage(data, db)


@router.get('/{id}', tags=['Стадия'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_stage(id, db)


@router.get('/',  tags=['Стадия'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_stage(db)


@router.put('/{id}', tags=['Стадия'])
async def update(id: int = None, data: StageUpdate = Depends(StageUpdate.as_form), db: Session = Depends(get_db)):
    return update_stage(data, db, id)


@router.delete('/{id}', tags=['Стадия'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_stage(id, db)


