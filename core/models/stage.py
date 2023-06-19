from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from datebase import Base


class Stage(Base):
    __tablename__ = 'stage'

    id = Column(Integer, primary_key=True, index=True)
    id_project = Column(Integer, ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    title = Column("Название", String)
    date_start = Column("Дата_начала", Date)
    date_finish = Column("Дата_сдачи", Date)
    phases = relationship('Phase')
    project = relationship('Project')
