from typing import Optional

from fastapi import Form
from pydantic import BaseModel


class GroupCreate(BaseModel):
    title: str
    quantity_people: int
    func_list: str

    @classmethod
    def as_form(
            cls,
            title: str = Form(...),
            quantity_people: int = Form(...),
            func_list: str = Form(...)
    ):
        return cls(title=title, quantity_people=quantity_people, func_list=func_list)


class GroupUpdate(BaseModel):
    title: Optional[str] = None
    quantity_people: Optional[int] = None
    func_list: Optional[str] = None

    @classmethod
    def as_form(
            cls,
            title: str = Form(...),
            quantity_people: int = Form(...),
            func_list: str = Form(...)
    ):
        return cls(title=title, quantity_people=quantity_people, func_list=func_list)
