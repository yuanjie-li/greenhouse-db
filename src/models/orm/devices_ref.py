from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.models import Base

class DevicesRef(Base):
    __tablename__ = 'devices_ref'

    ### Metadata fields 
    description = Column(String(100), nullable=False,
                        doc='Common way to describe this sensor.',
                        comment='Common way to describe this sensor.'
    )
    communication_type = Column(String(10), nullable=False,
                        doc='From list: e.g., serial.',
                        comment='From list: e.g., serial.'
    )

    reading_units = Column(String(10), nullable=True,
                        doc='From list: e.g., farad, volts, celsius.',
                        comment='From list: e.g., farad, volts, celsius.'
    )
    reading_min = Column(Float(3), nullable=True,
                        doc='Minimum possible reading value.',
                        comment='Minimum possible reading value.'
    )
    reading_max = Column(Float(3), nullable=True,
                        doc='Maximum possible reading value.',
                        comment='Maximum possible reading value.'
    )
    reading_precision = Column(Float(3), nullable=True,
                        doc='Possible variance in reading.',
                        comment='Possible variance in reading.'
    )

