#!/usr/bin/env python3
"""
Module to serialize & deserialize custom Python objects with the pickle module.
"""


import pickle


class CustomObject:
    def __init__(self, age, is_student, name):
        """
        Initialize a CustomObject instance.

        Args:
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
            name (str): The name of the person.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to a file.

        Args:
            filename(str):The name of the file where the object will be saved.

        Returns:
            None: Returns None if an exception occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return it.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject or None: The deserialized object if successful,
                                  otherwise None in case of an error.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
