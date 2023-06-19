from sqlalchemy import Column, Integer, ForeignKey, Table
from datebase import Base


EmployeeGroupOperationPhase = Table('employeegroup_operationphase',
                                    Base.metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('id_employee_group', Integer, ForeignKey('employee_group.id'),
                                           nullable=False),
                                    Column('id_operation_phase', Integer, ForeignKey('operation_phase.id'),
                                           nullable=False))
