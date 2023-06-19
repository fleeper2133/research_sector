from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from v1.routers.stage import get_all, get, update, create, delete
from v1.routers.project import get_all as get_all_projects

router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/stage', tags=['stage_view'])
async def get_stages(
        request: Request,
        stages=Depends(get_all),
        projects=Depends(get_all_projects)
):

    data = {
        "request": request,
        "title": "Стадии",
        "stages": stages,
        "projects": projects,
        "active_stage": "active"
    }
    return templates.TemplateResponse('stage.html', data)


@router.post('/stage', tags=['stage_view'])
async def add_stage(
        request: Request,
        stage=Depends(create)
):
    response = RedirectResponse(router.url_path_for('get_stages'))
    response.status_code = 302

    return response


@router.get('/stage/{id}/delete', tags=['stage_view'])
async def delete_stage(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_stages'))
    response.status_code = 302

    return response


@router.get('/stage/{id}/update', tags=['stage_view'])
async def update_stage(
        request: Request,
        id: int,
        stage=Depends(get),
        projects=Depends(get_all_projects)
):
    data = {
        "request": request,
        "title": "Стадии",
        "stage": stage,
        "projects": projects,
        "active_stage": "active"
    }
    return templates.TemplateResponse('stage_one_update.html', data)


@router.post('/stage/{id}/update', tags=['stage_view'])
async def update_stage_put(
        request: Request,
        id: int,
        stage=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_stages'))
    response.status_code = 302

    return response


@router.get('/stage/{id}', tags=['stage_view'])
async def get_one_stage(request: Request,
        id: int,
        stage=Depends(get)
):
    data = {
        "request": request,
        "title": "Стадии",
        "stage": stage,
        "active_stage": "active"
    }
    return templates.TemplateResponse('stage_one.html', data)


