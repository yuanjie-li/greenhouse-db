from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Locations(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    sub_id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    plants = relationship("Plants", back_populates='locations')

