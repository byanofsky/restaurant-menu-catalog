from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, Sequence('restaurant_id_seq'), primary_key=True)
    name = Column(String, nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu-items'
    id = Column(Integer, Sequence('menu_item_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    restaurant = relationship(Restaurant)
