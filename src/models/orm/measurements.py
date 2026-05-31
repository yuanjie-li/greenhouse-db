from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Measurements(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    value = Column(Float)
    
    device_id = Column(Integer, ForeignKey("devices.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))

    device = relationship("Devices", back_populates='measurements')
    locaiton = relationship("Locations", back_populates='measurements')

