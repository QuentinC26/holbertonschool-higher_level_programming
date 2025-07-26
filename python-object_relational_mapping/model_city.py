#!/usr/bin/python3
'''
Write a python file that contains the class definition of a cities
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class State(Base):
    '''
    Write a python file that contains the class definition of a cities
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), primary_key=False)
    state_id = Column("State.id", Integer, foreign_key=True)
