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
        if len(sys.argv) != 5:
            print("the sys.argv must be 4")
            sys.exit(1)
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name_to_search = sys.argv[4]

        # create URL Connexion
        url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:3306/{database}"
        # create Engine Object
        engine = create_engine(url, pool_pre_ping=True)
        # Create table of database
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        query = (
            session.query(State)
            .filter(State.name == state_name_to_search)
            .order_by(State.id)
            .all()
        )
        if len(query) == 0:
            print("Not found")
        for state in query:
            print("{}".format(state.id))
