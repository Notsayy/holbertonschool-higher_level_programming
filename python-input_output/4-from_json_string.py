#!/usr/bin/python3
"""Module for converting JSON data into a Python object"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
