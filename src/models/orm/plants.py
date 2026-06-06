from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.models import Base

class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)

    # Referenced by 
    locations = relationship('Locations')

