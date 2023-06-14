#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: An instance of the class.

    Returns:
        A list of attributes.
    """
    return dir(obj)
