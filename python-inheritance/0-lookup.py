#!/usr/bin/python3
"""
Function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Function look up to return the list of available attributes
    args: obj
    Return: list of avaible attributes
    """
    return dir(obj)
