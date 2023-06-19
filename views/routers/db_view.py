from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from v1.routers.db import sql_post


router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@router.get('/db', tags=['db'])
async def db_view(
        request: Request,
):
    data = {
        "request": request,
        "title": "Запрос в бд"
    }
    return templates.TemplateResponse('db.html', data)


@router.post('/db', tags=['db'])
async def db_view(
        request: Request,
        result=Depends(sql_post)
):
    data = {
        "request": request,
        "title": "Запрос в бд",
        "result": result
    }
    return templates.TemplateResponse('db.html', data)
