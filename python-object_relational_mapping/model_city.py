#!/usr/bin/python3
'''
Write a python file that contains the class definition of a cities
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    '''
    Write a python file that contains the class definition of a cities
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), primary_key=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
