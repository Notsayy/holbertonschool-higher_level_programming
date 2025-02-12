#!/usr/bin/python3
"""Module for loading a Python object from a JSON file"""


import json


def load_from_json_file(filename):
    """
    Loads a Python object from a file containing JSON data.

    Args:
        filename (str): The name of the file to load the JSON data from.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
