from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from datebase import Base
from core.models.employee_group import EmployeeGroup
from core.models.group_phase import GroupPhase


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True, index=True)
    title = Column("Название", String)
    quantity_people = Column("Кол-во людей", Integer)
    func_list = Column("Функциональный список", String)
    phase = relationship("Phase", secondary=GroupPhase)

