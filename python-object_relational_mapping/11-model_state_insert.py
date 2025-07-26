#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
from sqlalchemy import create_engine, Column, String, Integer, insert
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import requests


class hbtn_0e_6_usa():
    '''
    script that lists all states from the database hbtn_0e_0_usa
    '''
    if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("the sys.argv must be 4")
            sys.exit(1)
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # create URL Connexion
        url = f"mysql+mysqldb://{user}:{password}@127.0.0.1:3306/{database}"
        # create Engine Object
        engine = create_engine(url, pool_pre_ping=True)
        # Create table of database
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
    state = session.query(State).order_by(State.id).first()
    new_state = State(
        name="Louisiana"
        )
    session.add(new_state)
    session.commit()
    print(new_state.id)
