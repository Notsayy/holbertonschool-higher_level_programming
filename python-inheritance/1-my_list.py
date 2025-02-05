#!/usr/bin/python3
"""
Module containing the MyList class, a custom list class
that inherits from the built-in list class.
"""


class MyList(list):
    """
    Class MyList that inherits from list

    Arg: list (builtin list)

    """
    def print_sorted(self):
        """
        Function that prints the list, but sorted (ascending sort)
        """
        my_list = self.copy()
        my_list.sort()
        print(my_list)
