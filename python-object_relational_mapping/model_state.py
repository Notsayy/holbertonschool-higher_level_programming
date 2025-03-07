#!/usr/bin/python3
"""
Module defining the State class, mapped to the `states` table
in the MySQL database using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for class definitions
Base = declarative_base()


class State(Base):
    """
    Represents a state record in the `states` table.

    Inherits from `Base` and links to the `states` table in the database,
    mapping class attributes to table columns.

    Attributes:
        id (int): Unique identifier for each state (Primary Key).
        name (str): Name of the state, up to 128 characters, cannot be null.
    """
    __tablename__ = 'states'  # Table name in the database

    # The primary key column for the state table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Column to store the state name, with a maximum length of 128 characters
    name = Column(String(128), nullable=False)  # 'name' cannot be null
