#!/usr/bin/python3
""" Give us the first State object from the hbtn_0e_6_usa database
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
    occurrence = db_session.query(State).first()
    if occurrence is None:
        print("Nothing")
    else:
        print(occurrence.id, occurrence.name, sep=": ")
