#!/usr/bin/env python3
"""Provides XML serialization and deserialization for dictionaries."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to save to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Parameters:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
