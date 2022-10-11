#!/usr/bin/python3
"""
Filter by state passed by an argument

"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    state = session.query(State).filter(State.name ==
                                        '{:s}'.format(sys.argv[4]))
    for row in state:
        print(row.id)
        found = True
    if found is False:
        print('Not found')
