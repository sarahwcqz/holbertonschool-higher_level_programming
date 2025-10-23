#!/usr/bin/python3
"""
List id of state passed as argument
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

    spec_name = session.query(State).filter(State.name == sys.argv[4]).first()

    if spec_name:
            print(spec_name.id)
    else:
        print("Not Found")

    session.close()
