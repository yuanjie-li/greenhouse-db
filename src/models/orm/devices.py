from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from src.models import Base

class Devices(Base):
    __tablename__ = 'devices'

    serial = Column(String(20), unique=False,
                        doc='Device Serial Number, NOT unique.',
                        comment='Device Serial Number, NOT unique.'
    )

    # If the device gets moved to a  new location / gets a new plant,
    # set the previous to inactive and create a new entry.
    inactive = Column(DateTime, nullable=True,
                    doc='%Y-%m-%d %H:%M:%S. Set by API, not the sensor.',
                    comment='%Y-%m-%d %H:%M:%S. Set by API, not the sensor.'
    )

    type = Column(Integer, 
                  ForeignKey(f'{Base.metadata.schema}.devices_ref.id', 
                             ondelete='CASCADE'),
                        doc='FK to reference table with metadata.',
                        comment='FK to reference table with metadata.'
    )
    
    plant_id = Column(Integer, 
                  ForeignKey(f'{Base.metadata.schema}.plants.id', 
                             ondelete='CASCADE'),
                        doc='The plant being observed.',
                        comment='The plant being observed.'
    )

    location_id = Column(Integer, 
                  ForeignKey(f'{Base.metadata.schema}.locations.id', 
                             ondelete='CASCADE'),
                        doc='The location where the sensor is based.',
                        comment='The location where the sensor is based.'
    )



