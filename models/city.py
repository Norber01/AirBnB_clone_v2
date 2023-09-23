#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


<<<<<<< HEAD
class City(BaseModel, Base):
    """This is the class for the City
    Attributes:
        state_id: The state id
        name: the input name
=======

class City(BaseModel, Base):
    """This is a class for City
    Attributes:
        state_id: The state id
        name: input your  name
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
