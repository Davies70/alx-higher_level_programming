#!/usr/bin/python3

"""
 python file that contains the class definition of \
         a State and an instance Base = declarative_base() \
         creates a relationship between class State and City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ class State """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship('City', backref='states', cascade='all, delete')
