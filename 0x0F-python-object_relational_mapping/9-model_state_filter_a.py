#!/usr/bin/python3
""" Module using crud with orm """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    list all state objects from
    specified database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    states = (session.query(State).filter(State.name.like('%a%'))
              .order_by(State.id).all())

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
