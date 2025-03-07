#!/usr/bin/python3
"""
Script that deletes all State objects from the database hbtn_0e_6_usa
where the name contains the letter 'a'.
"""

import sys  # Import sys for command-line arguments
from model_state import Base, State  # Import State and Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Ensure the script is provided with the correct arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
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

    # Query the State table for states where the name contains 'a'
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state with 'a' in its name
    for state in state_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session to release resources
    session.close()
