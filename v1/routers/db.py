from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from sqlalchemy import text

from datebase import get_db

router = APIRouter()


@router.post('/db', tags=['db'])
async def sql_post(db: Session = Depends(get_db), sql: str = Form(default='')):
    try:
        sql1 = text(sql)
        result = db.execute(sql1)

        db.commit()
    except Exception:
        result = ["Ошибка в запросе!"]

    if "INSERT" in sql or "DELETE" in sql or "UPDATE" in sql:
        return []
    return result
