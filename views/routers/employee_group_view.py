from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from v1.routers.employee_group import get_all, get, update, create, delete
from v1.routers.employee import get_all as get_all_employees
from v1.routers.group import get_all as get_all_groups


router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/employee_group', tags=['employee_group_view'])
async def get_employee_groups(
        request: Request,
        employee_groups=Depends(get_all),
        employees=Depends(get_all_employees),
        groups=Depends(get_all_groups)
):

    data = {
        "request": request,
        "title": "Сотрудники в группах",
        "employee_groups": employee_groups,
        "groups": groups,
        "employees": employees,
        "active_employee_group": "active"
    }
    return templates.TemplateResponse('employee_group.html', data)


@router.post('/employee_group', tags=['employee_group_view'])
async def add_employee_group(
        request: Request,
        employee_group=Depends(create)
):
    response = RedirectResponse(router.url_path_for('get_employee_groups'))
    response.status_code = 302

    return response


@router.get('/employee_group/{id}/delete', tags=['employee_group_view'])
async def delete_employee_group(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_employee_groups'))
    response.status_code = 302

    return response


@router.get('/employee_group/{id}/update', tags=['employee_group_view'])
async def update_employee_group(
        request: Request,
        id: int,
        employee_group=Depends(get),
        employees=Depends(get_all_employees),
        groups=Depends(get_all_groups)
):
    data = {
        "request": request,
        "title": "Стадии",
        "employee_group": employee_group,
        "employees": employees,
        "groups": groups,
        "active_employee_group": "active"
    }
    return templates.TemplateResponse('employee_group_one_update.html', data)


@router.post('/employee_group/{id}/update', tags=['employee_group_view'])
async def update_employee_group_put(
        request: Request,
        id: int,
        employee_group=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_employee_groups'))
    response.status_code = 302

    return response


@router.get('/employee_group/{id}', tags=['employee_group_view'])
async def get_one_employee_group(request: Request,
                        id: int,
                        employee_group=Depends(get)
                        ):
    data = {
        "request": request,
        "title": "Стадии",
        "employee_group": employee_group,
        "active_employee_group": "active"
    }
    return templates.TemplateResponse('employee_group_one.html', data)