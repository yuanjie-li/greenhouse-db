from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from src.models import Base

class Devices(Base):
    __tablename__ = 'devices'

    serial = Column(String(20), unique=True,
                        doc='Device Serial Number, unique but not PK.',
                        comment='Device Serial Number, unique but not PK.'
    )
    type = Column(Integer, 
                  ForeignKey(f'{Base.metadata.schema}.devices_ref.id', 
                             ondelete='CASCADE'),
                        doc='FK to reference table with metadata.',
                        comment='FK to reference table with metadata.'
    )



