from typing import Optional

from fastapi import Form
from pydantic import BaseModel
from pydantic.schema import date


class PhaseCreate(BaseModel):
    id_stage: int
    title: str
    date_start: date
    date_finish: date

    @classmethod
    def as_form(
            cls,
            id_stage: int = Form(...),
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(id_stage=id_stage, title=title, date_start=date_start, date_finish=date_finish)


class PhaseUpdate(BaseModel):
    id_stage: Optional[int] = None
    title: Optional[str] = None
    date_start: Optional[date] = None
    date_finish: Optional[date] = None

    @classmethod
    def as_form(
            cls,
            id_stage: int = Form(...),
            title: str = Form(...),
            date_start: date = Form(...),
            date_finish: date = Form(...)
    ):
        return cls(id_stage=id_stage, title=title, date_start=date_start, date_finish=date_finish)
