from sqlalchemy import Column, Integer, String

from src.models import Base

class Plants(Base):
    __tablename__ = 'plants'

    # Naming and classification 
    name_common = Column(String(20),
                    doc='Common name.',
                    comment='Common name.'
    )
    class_common = Column(String(10),
                    doc='Common classification like fruit, herb.',
                    comment='Common classification like fruit, herb.'
    )
    name_family = Column(String(20),
                    doc='Scientific name of the family.',
                    comment='Scientific name of the family.'
    )
    name_genus = Column(String(20),
                    doc='Scientific name of the genus.',
                    comment='Scientific name of the genus.'
    )
    name_species = Column(String(20),
                    doc='Scientific name of the species.',
                    comment='Scientific name of the species.'
    )

    # Preferences 
    planting_season = Column(String(10),
                    doc='String season, e.g., spring, winter.',
                    comment='String season, e.g., spring, winter.'
    )
    soil_quality = Column(Integer,
                    doc='0-10 where 0 is poor and 10 is fertile.',
                    comment='0-10 where 0 is poor and 10 is fertile.'
    )
    soil_moisture = Column(Integer,
                    doc='0-10 where 0 is dry and 10 is wet.',
                    comment='0-10 where 0 is dry and 10 is wet.'
    )
    sunlight = Column(Integer,
                    doc='0-10 where 0 is no direct and 10 is full sun.',
                    comment='0-10 where 0 is no direct and 10 is full sun.'
    )
    wind = Column(Integer,
                    doc='0-10 where 0 is sheltered and 10 is open.',
                    comment='0-10 where 0 is sheltered  and 10 is open.'
    )
    pests = Column(String(100),
                    doc='Known pests and diseases.',
                    comment='Known pests and diseases.'
    )


