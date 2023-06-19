from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas.phase import PhaseCreate
from datebase import get_db
from v1.services.phase import *

router = APIRouter()


@router.post('/', tags=['Этап'])
async def create(data: PhaseCreate = Depends(PhaseCreate.as_form), db: Session = Depends(get_db)):
    return create_phase(data, db)


@router.get('/{id}', tags=['Этап'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return get_phase(id, db)


@router.get('/',  tags=['Этап'])
async def get_all(db: Session = Depends(get_db)):
    return get_all_phase(db)


@router.put('/{id}', tags=['Этап'])
async def update(id: int = None, data: PhaseUpdate = Depends(PhaseCreate.as_form), db: Session = Depends(get_db)):
    return update_phase(data, db, id)


@router.delete('/{id}', tags=['Этап'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return remove_phase(id, db)


