#!/usr/bin/python3
"""
Function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Arg: obj , a_class

    Return: True or False
    """
    return (type(obj) is a_class)
