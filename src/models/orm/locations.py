from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src.models import Base

class Locations(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)

    # FKs
    plant_id = Column(Integer, 
                      ForeignKey("plants.id", ondelete='CASCADE'))
    plants = relationship("Plants", back_populates='locations')

    # Referenced by 
    measurements = relationship("Measurements")

