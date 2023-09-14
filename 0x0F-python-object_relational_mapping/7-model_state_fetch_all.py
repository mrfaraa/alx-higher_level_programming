#!/usr/bin/python3
"""
File: 7-model_state_fetch_all.py
Desc: a script that lists all State objects from the
        database hbtn_0e_6_usa
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 14 September 2023
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
