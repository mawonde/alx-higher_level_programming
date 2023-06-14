#!/usr/bin/python3
""" A function that returns the list of available attributes and methods of an object:
    """
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: An instance of the class.

    Returns:
        A list of attributes.
    """
    return dir(obj)
