from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src.models import Base

class Measurements(Base):
    __tablename__ = 'measurements'

    timestamp = Column(DateTime,
                    doc='%Y-%m-%d %H:%M:%S. Set by API, not the sensor.',
                    comment='%Y-%m-%d %H:%M:%S. Set by API, not the sensor.'
    )
    value = Column(Float(5),
                    doc='Sensor raw reading.',
                    comment='Sensor raw reading.'
    )
    
    # FKs
    device_id = Column(Integer, 
                    ForeignKey(f'{Base.metadata.schema}.devices.id'),
                    doc='FK to the device that made the reading.',
                    comment='FK to the device that made the reading.'
    )

