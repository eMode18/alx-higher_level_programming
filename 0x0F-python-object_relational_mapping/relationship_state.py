#!/usr/bin/python3
"""
Habours State class and Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, MetaData

init_metadata = MetaData()
Base = declarative_base(metadata=init_metadata)

class State(Base):
    """
    This class holds the id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
