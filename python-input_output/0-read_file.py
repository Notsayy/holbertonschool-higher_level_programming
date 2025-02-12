#!/usr/bin/python3
"""Module for reading a text file"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it to the console.

    Args:
        filename(str):The name of the file to read.Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
