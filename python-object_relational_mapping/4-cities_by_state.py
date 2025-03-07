#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all cities
from the `cities` table and their corresponding states,
ordered by `id` of the cities in ascending order.
"""

import MySQLdb
import sys


# Ensures the script runs only if executed directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments (MySQL username, password, database name)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the SQL query with proper spacing
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Loop through the results and print each row
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
