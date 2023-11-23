#!/usr/bin/python3
""" Give us the State object from the hbtn_0e_6_usa database based
on the named argument provided
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    for occurrence in db_session.query(State).filter(State.name.like('%a%')):
        db_session.delete(occurrence)
    db_session.commit()
