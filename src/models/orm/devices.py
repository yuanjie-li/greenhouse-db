from sqlalchemy import Column, Integer, String

class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    serial = Column(String(50), unique=True)
    type = Column(Integer)

