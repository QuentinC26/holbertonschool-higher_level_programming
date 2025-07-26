#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
from sqlalchemy import create_engine, Column, String, Integer
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import requests


class hbtn_0e_0_usa():
    '''
    script that lists all states from the database hbtn_0e_0_usa
    '''
    if __name__ == "__main__":
        user=sys.argv[1]
        password=sys.argv[2]
        database=sys.argv[3]
        url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:3306/{database}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        if len(sys.argv) != 4:
            print("the sys.argv must be 3")
            sys.exit(1)
        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State).order_by(State.id).limit(1):
            if state is None:
                print("Nothing")
            print("{}: {}".format(state.id, state.name))
