from typing import Optional

from fastapi import Form
from pydantic import BaseModel
from pydantic.schema import date


class StageCreate(BaseModel):
    id_project: int
    title: str
    date_start: date
    date_finish: date

    @classmethod
    def as_form(
            cls,
            id_project: int = Form(...),
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(id_project=id_project, title=title, date_start=date_start, date_finish=date_finish)


class StageUpdate(BaseModel):
    id_project: Optional[int] = None
    title: Optional[str] = None
    date_start: Optional[date] = None
    date_finish: Optional[date] = None

    @classmethod
    def as_form(
            cls,
            id_project: int = Form(...),
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(id_project=id_project, title=title, date_start=date_start, date_finish=date_finish)
