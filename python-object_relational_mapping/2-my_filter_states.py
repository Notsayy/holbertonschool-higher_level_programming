#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states
from the `states` table where the name matches the given argument,
ordered by `id` in ascending order.
"""

import MySQLdb
import sys

# Ensures the script runs only if executed directly
if __name__ == "__main__":

    # Retrieve command-line arguments.
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]  # The state name to search for

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    query = query.format(state_name)
    cursor.execute(query)

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Print each row in the result set
    for row in results:
        print(row)

    # Close the cursor after execution
    cursor.close()

    # Close the database connection
    db.close()
