#!/usr/bin/python3
"""Module for saving a Python object as JSON in a file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
