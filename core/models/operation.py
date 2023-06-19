from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from datebase import Base
from core.models.employee_operation import EmployeeOperation
from core.models.operation_phase import OperationPhase


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True, index=True)
    title = Column("Название", String)
    date_start = Column("Дата_начала", Date)
    date_finish = Column("Дата_сдачи", Date)
    phase = relationship('Phase', secondary=OperationPhase)
    employee = relationship('Employee', secondary=EmployeeOperation)
