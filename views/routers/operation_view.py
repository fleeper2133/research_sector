from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from datebase import get_db
from v1.routers.operation import get_all, get, update, create, delete
from v1.routers.phase import get_all as get_all_phases
from v1.services.phase import get_phase


router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/operation', tags=['operation_view'])
async def get_operations(
        request: Request,
        operations=Depends(get_all),
        phases=Depends(get_all_phases)
):

    data = {
        "request": request,
        "title": "Операции",
        "operations": operations,
        "phases": phases,
        "phases_quantity": len(phases),
        "active_operation": "active"
    }
    return templates.TemplateResponse('operation.html', data)


@router.post('/operation', tags=['operation_view'])
async def add_operation(
        db: Session = Depends(get_db),
        operation=Depends(create),
        id_phases: list = Form(...)
):

    for id_phase in id_phases:
        phase = get_phase(id_phase, db)
        operation.phase.append(phase)
    db.commit()

    response = RedirectResponse(router.url_path_for('get_operations'))
    response.status_code = 302

    return response


@router.get('/operation/{id}/delete', tags=['operation_view'])
async def delete_operation(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_operations'))
    response.status_code = 302

    return response


@router.get('/operation/{id}/update', tags=['operation_view'])
async def update_operation(
        request: Request,
        id: int,
        operation=Depends(get),
):
    data = {
        "request": request,
        "title": "Стадии",
        "operation": operation,
        "active_operation": "active"
    }
    return templates.TemplateResponse('operation_one_update.html', data)


@router.post('/operation/{id}/update', tags=['operation_view'])
async def update_operation_put(
        request: Request,
        id: int,
        operation=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_operations'))
    response.status_code = 302

    return response


@router.get('/operation/{id}', tags=['operation_view'])
async def get_one_operation(request: Request,
        id: int,
        operation=Depends(get)
):
    data = {
        "request": request,
        "title": "Стадии",
        "operation": operation,
        "active_operation": "active"
    }
    return templates.TemplateResponse('operation_one.html', data)

