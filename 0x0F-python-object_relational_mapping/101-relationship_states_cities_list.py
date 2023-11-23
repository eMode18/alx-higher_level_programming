#!/usr/bin/python3
""" Display the State object using the named argument from the database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id):
        print(result.id, result.name, sep=": ")
        for cinstance in result.cities:
            print("    ", end="")
            print(cinstance.id, cinstance.name, sep=": ")
