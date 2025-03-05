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

    # Retrieve command-line arguments (MySQL username, password, database name)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
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

        # Define the SQL query
        query = "SELECT * FROM states ORDER BY id ASC;"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all results from the executed query
        results = cursor.fetchall()

        # Loop through the results and print each row
        for row in results:
            print(row)

        # Close the cursor
        cursor.close()

        # Close the database connection
        db.close()

    except MySQLdb.Error as e:
        # Print an error message if an exception occurs
        print(f"Error MySQL: {e}")
