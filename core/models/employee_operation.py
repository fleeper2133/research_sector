from sqlalchemy import Column, Integer, ForeignKey, Table
from datebase import Base

EmployeeOperation = Table('employee_operation',
                          Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('id_operation', Integer, ForeignKey('operation.id'), nullable=False),
                          Column('id_employee', Integer, ForeignKey('employee.id'), nullable=False))
