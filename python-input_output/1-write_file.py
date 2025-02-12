#!/usr/bin/python3
"""Module for writing text to a file"""


def write_file(filename="", text=""):
    """
    Writes text to a file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
