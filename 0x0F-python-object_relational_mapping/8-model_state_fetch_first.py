#!/usr/bin/python3
"""
File: 8-model_state_fetch_first.py
Desc: a script that prints the first State object from
        the database hbtn_0e_6_usa
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 15 September 2023
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
    fstate = session.query(State).order_by(State.id).first()
    if fstate:
        print("{}: {}".format(fstate.id, fstate.name))
    else:
        print("Nothing")
    session.close()
