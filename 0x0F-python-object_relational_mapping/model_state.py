#!/usr/bin/python3
"""Module that works with ORM """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
    __table_name__(str): name of the table
    id(int): id column of table
    name(str): the name of the State class
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
