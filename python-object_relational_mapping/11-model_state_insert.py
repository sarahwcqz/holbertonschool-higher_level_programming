#!/usr/bin/python3
"""
Create a new item in table State
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana_state = State(name='Louisiana')
    session.add(louisiana_state)
    session.commit()

    new_state = (
        session.query(State.id)
        .filter(State.name == 'Louisiana')
        .first()
    )

    if new_state:
        print("{}".format(new_state.id))

    session.close()
