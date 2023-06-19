from sqlalchemy import Column, Integer, ForeignKey, Table
from datebase import Base

GroupPhase = Table('group_phase',
                   Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('id_group', Integer, ForeignKey('group.id'), nullable=False),
                   Column('id_phase', Integer, ForeignKey('phase.id'), nullable=False))
