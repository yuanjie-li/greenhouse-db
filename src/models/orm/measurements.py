from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src.models import Base

class Measurements(Base):
    __tablename__ = 'measurements'

    timestamp = Column(DateTime)
    value = Column(Float)
    
    # FKs
    device_id = Column(Integer, 
                    ForeignKey(f'{Base.metadata.schema}.devices.id'))
    location_id = Column(Integer, 
                    ForeignKey(f'{Base.metadata.schema}.locations.id'))

    #devices = relationship('devices', 
    #                    back_populates='measurements')
    #locations = relationship('locations', 
    #                    back_populates='measurements')

