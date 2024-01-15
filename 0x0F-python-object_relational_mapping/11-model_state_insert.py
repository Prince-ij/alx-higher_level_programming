#!/usr/bin/python3
""" Module using crud with orm """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Add a new state to the
    database and print it's id
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
