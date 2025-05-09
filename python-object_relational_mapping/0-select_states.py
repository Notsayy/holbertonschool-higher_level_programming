#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states
from the `states` table, ordered by their `id` in ascending order.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


# Ensures the script runs only if executed directly
if __name__ == "__main__":
    # Check if all required arguments are provided
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

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Loop through the results and print each row
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
