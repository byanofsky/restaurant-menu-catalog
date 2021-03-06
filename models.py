from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from database import Base, db_session
from sqlalchemy.orm import relationship


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, Sequence('restaurant_id_seq'), primary_key=True)
    name = Column(String, nullable=False)

    def update(self, name):
        self.name = name
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @classmethod
    def create(cls, name):
        db_session.add(Restaurant(name=name))
        return db_session.commit()

    @classmethod
    def get_by_id(cls, id):
        return db_session.query(Restaurant).filter(Restaurant.id == id).one()

    @classmethod
    def get_all(cls):
        return db_session.query(Restaurant).all()


class MenuItem(Base):
    __tablename__ = 'menu-items'
    id = Column(Integer, Sequence('menu_item_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    restaurant = relationship(Restaurant)

    def update(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

    @classmethod
    def create(cls, name, description, price, restaurant_id):
        db_session.add(
            MenuItem(
                name=name,
                description=description,
                price=price,
                restaurant_id=restaurant_id
            )
        )
        return db_session.commit()

    @classmethod
    def get_by_id(cls, id):
        return db_session.query(MenuItem)\
                         .filter(MenuItem.id == id)\
                         .one()

    @classmethod
    def get_by_restaurant_id(cls, restaurant_id):
        return db_session.query(MenuItem)\
                         .filter(MenuItem.restaurant_id == restaurant_id)\
                         .all()
