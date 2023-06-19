from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from datebase import Base


class Phase(Base):
    __tablename__ = 'phase'

    id = Column(Integer, primary_key=True, index=True)
    id_stage = Column(Integer, ForeignKey('stage.id', ondelete='CASCADE'), nullable=False)
    title = Column("Название", String)
    date_start = Column("Дата_начала", Date)
    date_finish = Column("Дата_сдачи", Date)
    # operations = relationship('Operation', secondary=OperationPhase)
    # group = relationship('Group', secondary=GroupPhase)
    stage = relationship('Stage')
