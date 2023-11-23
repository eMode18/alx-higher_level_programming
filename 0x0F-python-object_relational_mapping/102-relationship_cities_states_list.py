#!/usr/bin/python3
""" Display the State object using named argument from the database
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id):
        for cty_instance in result.cities:
            print(cty_instance.id, cty_instance.name, sep=": ", end="")
            print(" -> " + result.name)
