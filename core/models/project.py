from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from datebase import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    title = Column("Название", String)
    direction = Column("Направление", String)
    date_start = Column("Дата_начала", Date)
    date_finish = Column("Дата_сдачи", Date)
    stages = relationship('Stage')
