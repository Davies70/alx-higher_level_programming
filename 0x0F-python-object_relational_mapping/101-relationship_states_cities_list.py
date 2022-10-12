#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database

"""
import sys
from relationship_state import Base, City, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, joinedload, lazyload

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
