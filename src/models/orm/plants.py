from sqlalchemy import Column, Integer, String

class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)

