#!/usr/bin/env python3
"""
Module to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format.

    Args:
        filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(filename, "r") as f:
            new_list = csv.DictReader(f)
            data = [row for row in new_list]
        with open("data.json", "w") as g:
            json.dump(data, g, indent=4)
        return True

    except Exception:
        return False
