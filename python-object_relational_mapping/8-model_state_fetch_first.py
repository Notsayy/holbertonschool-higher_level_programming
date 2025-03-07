#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys  # Importing sys to handle command-line arguments
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database),
        pool_pre_ping=True)  # Use pool_pre_ping to avoid connection issues

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()  # Create session instance to interact with database

    # Query the 'State' table and retrieve the first state ordered by 'id'
    state = session.query(State).order_by(State.id).first()

    # If no state was found, print 'Nothing'
    if state is None:
        print("Nothing")
    else:
        # Print the first state's id and name
        print(f"{state.id}: {state.name}")

    # Close the session to release resources
    session.close()
