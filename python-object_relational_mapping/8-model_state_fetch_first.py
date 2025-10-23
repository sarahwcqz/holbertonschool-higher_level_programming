#!/usr/bin/python3
"""
List only first result
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_res = session.query(State).order_by(State.id).first()

    if first_res:
        print("{}: {}".format(first_res.id, first_res.name))
    else:
        print("Nothing")

    session.close()
