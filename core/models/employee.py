from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from datebase import Base
from core.models.employee_operation import EmployeeOperation


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    FIO = Column("ФИО", String)
    duty = Column("Обязанность", String)
    qualification = Column("Квалификация", String)
    operation = relationship("Operation", secondary=EmployeeOperation)

