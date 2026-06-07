from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models import Base

class Devices(Base):
    __tablename__ = 'devices'

    serial = Column(String(50), unique=True)
    type = Column(Integer)

