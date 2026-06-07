from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src.models import Base

class Locations(Base):
    __tablename__ = 'locations'

    # FKs
    plant_id = Column(Integer, 
                      ForeignKey(f'{Base.metadata.schema}.plants.id', 
                                 ondelete='CASCADE'))
    #plants = relationship('plants', back_populates='locations')

