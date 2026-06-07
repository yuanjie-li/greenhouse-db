from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.models import Base

class Plants(Base):
    __tablename__ = 'plants'

    type = Column(Integer)


