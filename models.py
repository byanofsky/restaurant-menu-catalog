from sqlalchemy import Column, Integer, String, Sequence
from database import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, Sequence('restaurant_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
