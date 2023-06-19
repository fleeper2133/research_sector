from typing import Optional

from fastapi import Form
from pydantic import BaseModel
from pydantic.schema import date


class OperationCreate(BaseModel):
    title: str
    date_start: date
    date_finish: date

    @classmethod
    def as_form(
            cls,
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(title=title, date_start=date_start, date_finish=date_finish)


class OperationUpdate(BaseModel):
    title: Optional[str] = None
    date_start: Optional[date] = None
    date_finish: Optional[date] = None

    @classmethod
    def as_form(
            cls,
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(title=title, date_start=date_start, date_finish=date_finish)
