#!/usr/bin/python3
'''
Write a python file that contains the class definition of a State and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''
    Write a python file that contains the class definition of a State and an instance Base = declarative_base()
    '''
    __tablename__ = 'states'
    id = Column("states_id", Integer, primary_key=True)
    name = Column("states_name", String(128), primary_key=False)

Base.metadata.create_all(engine)
