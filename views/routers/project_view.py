from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from v1.routers.project import get_all as get_all_projects, create as create_project, delete as delete_project, get as get_project, update as update_project


router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/project', tags=['project_view'])
async def get_projects(
        request: Request,
        projects=Depends(get_all_projects),
):

    data = {
        "request": request,
        "title": "Проекты",
        "projects": projects,
        "active_project": "active"
    }
    return templates.TemplateResponse('project.html', data)


@router.post('/project', tags=['project_view'])
async def add_project(
        request: Request,
        project=Depends(create_project)
):
    response = RedirectResponse(router.url_path_for('get_projects'))
    response.status_code = 302

    return response


@router.get('/project/{id}/delete', tags=['project_view'])
async def delete_project(
        request: Request,
        id: int,
        delete=Depends(delete_project)
):
    response = RedirectResponse(router.url_path_for('get_projects'))
    response.status_code = 302

    return response


@router.get('/project/{id}/update', tags=['project_view'])
async def update_project1(
        request: Request,
        id: int,
        project=Depends(get_project)
):
    data = {
        "request": request,
        "title": "Проекты",
        "project": project,
        "active_project": "active"
    }
    return templates.TemplateResponse('project_one_update.html', data)


@router.post('/project/{id}/update', tags=['project_view'])
async def update_project_put(
        request: Request,
        id: int,
        project=Depends(update_project)
):
    response = RedirectResponse(router.url_path_for('get_projects'))
    response.status_code = 302

    return response


@router.get('/project/{id}', tags=['project_view'])
async def get_one_project( request: Request,
        id: int,
        project=Depends(get_project)
):
    data = {
        "request": request,
        "title": "Проекты",
        "project": project,
        "active_project": "active"
    }
    return templates.TemplateResponse('project_one.html', data)

