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
    state = session.query(State).filter(State.name == '{:s}'
                                        .format(sys.argv[4]))
    if not state:
        print('Not found')
    [print(state.id) for state in session.query(State).
     filter(State.name == '{:s}'.format(sys.argv[4]))]
    session.close()
