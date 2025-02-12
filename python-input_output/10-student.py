#!/usr/bin/python3
"""Module defining a Student class"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs(list):A list of attribute names to include in the dictionary.
            If None, all attributes are included.
        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
