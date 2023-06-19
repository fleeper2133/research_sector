from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from datebase import get_db
from v1.routers.employee import get_all, get, update, create, delete
from v1.routers.operation import get_all as get_all_operations, get_operation

router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/employee', tags=['employee_view'])
async def get_employees(
        request: Request,
        employees=Depends(get_all),
        operations=Depends(get_all_operations)
):

    data = {
        "request": request,
        "title": "Сотрудники",
        "employees": employees,
        "operations": operations,
        "operations_quantity": len(operations),
        "active_employee": "active"
    }
    return templates.TemplateResponse('employee.html', data)


@router.post('/employee', tags=['employee_view'])
async def add_employee(
        request: Request,
        employee=Depends(create),
        id_operations: list = Form(...),
        db: Session = Depends(get_db)

):
    for id_operation in id_operations:
        operation = get_operation(id_operation, db)
        employee.operation.append(operation)
    db.commit()

    response = RedirectResponse(router.url_path_for('get_employees'))
    response.status_code = 302

    return response


@router.get('/employee/{id}/delete', tags=['employee_view'])
async def delete_employee(
        request: Request,
        id: int,
        delete=Depends(delete)
):
    response = RedirectResponse(router.url_path_for('get_employees'))
    response.status_code = 302

    return response


@router.get('/employee/{id}/update', tags=['employee_view'])
async def update_employee(
        request: Request,
        id: int,
        employee=Depends(get),
):
    data = {
        "request": request,
        "title": "Стадии",
        "employee": employee,
        "active_employee": "active"
    }
    return templates.TemplateResponse('employee_one_update.html', data)


@router.post('/employee/{id}/update', tags=['employee_view'])
async def update_employee_put(
        request: Request,
        id: int,
        employee=Depends(update)
):
    response = RedirectResponse(router.url_path_for('get_employees'))
    response.status_code = 302

    return response


@router.get('/employee/{id}', tags=['employee_view'])
async def get_one_employee(request: Request,
                        id: int,
                        employee=Depends(get)
                        ):
    data = {
        "request": request,
        "title": "Стадии",
        "employee": employee,
        "active_employee": "active"
    }
    return templates.TemplateResponse('employee_one.html', data)