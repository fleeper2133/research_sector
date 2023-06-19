from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from datebase import get_db
from v1.routers.group import get_all, get, update, create, delete
from v1.routers.phase import get_all as get_all_phases
from v1.services.phase import get_phase


router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/group', tags=['group_view'])
async def get_groups(
        request: Request,
        groups=Depends(get_all),
        phases=Depends(get_all_phases)
):

    data = {
        "request": request,
        "title": "Группы",
        "groups": groups,
        "phases": phases,
        "phases_quantity": len(phases),
        "active_group": "active"
    }
    return templates.TemplateResponse('group.html', data)


@router.post('/group', tags=['group_view'])
async def add_group(
        db: Session = Depends(get_db),
        group=Depends(create),
        id_phases: list = Form(...)
):

    for id_phase in id_phases:
        phase = get_phase(id_phase, db)
        group.phase.append(phase)
    db.commit()

    response = RedirectResponse(router.url_path_for('get_groups'))
    response.status_code = 302

    return response


@router.get('/group/{id}/delete', tags=['group_view'])
async def delete_group(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_groups'))
    response.status_code = 302

    return response


@router.get('/group/{id}/update', tags=['group_view'])
async def update_group(
        request: Request,
        id: int,
        group=Depends(get),
):
    data = {
        "request": request,
        "title": "Стадии",
        "group": group,
        "active_group": "active"
    }
    return templates.TemplateResponse('group_one_update.html', data)


@router.post('/group/{id}/update', tags=['group_view'])
async def update_group_put(
        request: Request,
        id: int,
        group=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_groups'))
    response.status_code = 302

    return response


@router.get('/group/{id}', tags=['group_view'])
async def get_one_group(request: Request,
                        id: int,
                        group=Depends(get)
                        ):
    data = {
        "request": request,
        "title": "Стадии",
        "group": group,
        "active_group": "active"
    }
    return templates.TemplateResponse('group_one.html', data)



