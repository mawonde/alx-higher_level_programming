#!/usr/bin/python3

"""
This module contains a class that restricts dynamically created attributes.
"""


class LockedClass:
    """
    Class that restricts dynamically created attributes.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes an instance of LockedClass.
        """
        pass

