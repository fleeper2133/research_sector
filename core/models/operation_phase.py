from sqlalchemy import Column, Integer, ForeignKey, Table
from datebase import Base

OperationPhase = Table('operation_phase',
                       Base.metadata,
                       Column('id', Integer, primary_key=True),
                       Column('id_operation', Integer, ForeignKey('operation.id'), nullable=False),
                       Column('id_phase', Integer, ForeignKey('phase.id'), nullable=False))
