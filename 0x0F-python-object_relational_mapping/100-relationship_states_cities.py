#!/usr/bin/python3
"""
Create State "California" and  City "San Francisco" in the DB
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    createdState = State(name='California')
    createdCity = City(name='San Francisco')
    createdState.cities.append(createdCity)

    session.add(createdState)
    session.add(createdCity)
    session.commit()
