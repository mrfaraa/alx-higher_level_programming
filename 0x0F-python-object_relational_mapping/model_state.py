#!/usr/bin/python3
"""
File: model_state.py
Desc: contains the class definition of a State and an
        instance Base = declarative_base()
Author: EL Mehdi Faraa (mrfaraa)
Date Created: 16 September 2023
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    An SQL table called states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
