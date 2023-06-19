from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from v1.routers.phase import get_all, get, update, create, delete
from v1.routers.stage import get_all as get_all_stages

router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/phase', tags=['phase_view'])
async def get_phases(
        request: Request,
        phases=Depends(get_all),
        stages=Depends(get_all_stages)
):

    data = {
        "request": request,
        "title": "Этапы",
        "phases": phases,
        "stages": stages,
        "active_phase": "active"
    }
    return templates.TemplateResponse('phase.html', data)


@router.post('/phase', tags=['phase_view'])
async def add_phase(
        request: Request,
        phase=Depends(create)
):
    response = RedirectResponse(router.url_path_for('get_phases'))
    response.status_code = 302

    return response


@router.get('/phase/{id}/delete', tags=['phase_view'])
async def delete_phase(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_phases'))
    response.status_code = 302

    return response


@router.get('/phase/{id}/update', tags=['phase_view'])
async def update_phase(
        request: Request,
        id: int,
        phase=Depends(get),
        stages=Depends(get_all_stages)
):
    data = {
        "request": request,
        "title": "Стадии",
        "phase": phase,
        "stages": stages,
        "active_phase": "active"
    }
    return templates.TemplateResponse('phase_one_update.html', data)


@router.post('/phase/{id}/update', tags=['phase_view'])
async def update_phase_put(
        request: Request,
        id: int,
        phase=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_phases'))
    response.status_code = 302

    return response


@router.get('/phase/{id}', tags=['phase_view'])
async def get_one_phase(request: Request,
        id: int,
        phase=Depends(get)
):
    data = {
        "request": request,
        "title": "Стадии",
        "phase": phase,
        "active_phase": "active"
    }
    return templates.TemplateResponse('phase_one.html', data)


