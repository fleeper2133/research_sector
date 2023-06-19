from typing import Optional

from fastapi import Form
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    FIO: str
    duty: str
    qualification: str

    @classmethod
    def as_form(
            cls,
            FIO: str = Form(...),
            duty: str = Form(...),
            qualification: str = Form(...)
    ):
        return cls(FIO=FIO, duty=duty, qualification=qualification)


class EmployeeUpdate(BaseModel):
    FIO: Optional[str] = None
    duty: Optional[str] = None
    qualification: Optional[str] = None

    @classmethod
    def as_form(
            cls,
            FIO: str = Form(...),
            duty: str = Form(...),
            qualification: str = Form(...)
    ):
        return cls(FIO=FIO, duty=duty, qualification=qualification)
