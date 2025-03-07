#!/usr/bin/python3
"""
This script lists all cities of a given state from the database `hbtn_0e_4_usa`
ordered by `id` in ascending order.
"""

import MySQLdb
import sys

# Ensures the script runs only if executed directly
if __name__ == "__main__":
    # Verify the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> "
              "<state name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Prepare and execute the SQL query
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Print city names in a single line, separated by commas
    print(", ".join(row[0] for row in results))

    # Close cursor and database connection
    cursor.close()
    db.close()
