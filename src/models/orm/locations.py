from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy import ForeignKey

from src.models import Base

class Locations(Base):
    __tablename__ = 'locations'

    ### Location metadata 
    '''
    Actual location data of the location, left nullable for privacy
    but no reason they can't be filled out with aliases known to the 
    user.
    '''
    nickname = Column(String(15),
              nullable=True,
              default=None,
              doc="Name for the location, e.g. 'Kitchen', 'Garden'.",
              comment="Name for the location, e.g. 'Kitchen', 'Garden'.",
    )
    group_nickname = Column(String(15),
              nullable=True,
              default=None,
              doc="Higher level to group locations, if necessary.",
              comment="Higher level to group locations, if necessary.",
    )
    owner = Column(String(50),
              nullable=True,
              default=None,
              doc="Owner of the location, e.g. 'Me', 'Public'.",
              comment="Owner of the location, e.g. 'Me', 'Public'.",
    )
    gps_lat = Column(Float(8),
                  nullable=True,
                  default=None,
                  doc="GPS Latitude value",
                  comment="GPS Latitude value",
    )
    gps_long = Column(Float(8),
                  nullable=True,
                  default=None,
                  doc="GPS Latitude value",
                  comment="GPS Latitude value",
    )

    '''
    Since read/write will happen through API, casing and spelling of
    individual types should be consistent. Slower query, so change to int
    with ref table later.
    '''
    type = Column(String(10), 
                  nullable=False, 
                  default="outdoor",
                  doc="String description of location",
                  comment="String description of location",
    )
    

