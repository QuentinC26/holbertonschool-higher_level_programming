#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
from sqlalchemy import create_engine, Column, String, Integer
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import requests

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("quentin", "Break012", "hbtn_0e_6_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)


class hbtn_0e_0_usa():
    '''
    script that lists all states from the database hbtn_0e_0_usa
    '''
    if __name__ == "__main__":
        the_db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )
        if len(sys.argv) != 4:
            print("the sys.argv must be 3")
            sys.exit(1)
        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State).order_by(State.id).limit(1):
            if session.query(State).first() is None:
                print("Nothing")
            print("{}: {}".format(state.id, state.name))
        session.close()
