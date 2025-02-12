#!/usr/bin/env python3
"""
Module for serializing Python dictionaries to JSON and deserializing JSON files.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
