from sqlalchemy import Column, Integer, ForeignKey, Date, Table
from sqlalchemy.orm import relationship

from datebase import Base


class EmployeeGroup(Base):
    __tablename__ = 'employee_group'

    id = Column(Integer, primary_key=True, index=True)
    id_group = Column(Integer, ForeignKey('group.id', ondelete='CASCADE'), nullable=False)
    id_employee = Column(Integer, ForeignKey('employee.id', ondelete='CASCADE'), nullable=False)
    date_connect = Column("Дата вступления в группу", Date)
    date_disconnect = Column("Дата исключения из группы")
    employee = relationship('Employee')
    group = relationship('Group')

