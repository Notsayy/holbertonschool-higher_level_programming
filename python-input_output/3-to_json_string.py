#!/usr/bin/python3
"""Module for converting a Python object to JSON"""


import json


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON string representation.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
