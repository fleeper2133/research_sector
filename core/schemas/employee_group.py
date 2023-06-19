from typing import Optional

from fastapi import Form
from pydantic import BaseModel
from pydantic.schema import date


class EmployeeGroupCreate(BaseModel):
    id_employee: int
    id_group: int
    date_connect: date
    date_disconnect: Optional[date] = None

    @classmethod
    def as_form(
            cls,
            id_employee: int = Form(...),
            id_group: int = Form(...),
            date_connect: date = Form(...),
            date_disconnect: date = Form(default=None)
    ):
        return cls(id_employee=id_employee, id_group=id_group, date_connect=date_connect, date_disconnect=date_disconnect)


class EmployeeGroupUpdate(BaseModel):
    id_employee: Optional[int] = None
    id_group: Optional[int] = None
    date_connect: Optional[date] = None
    date_disconnect: Optional[date] = None

    @classmethod
    def as_form(
            cls,
            id_employee: int = Form(...),
            id_group: int = Form(...),
            date_connect: date = Form(...),
            date_disconnect: date = Form(default=None)
    ):
        return cls(id_employee=id_employee, id_group=id_group, date_connect=date_connect,
                   date_disconnect=date_disconnect)

