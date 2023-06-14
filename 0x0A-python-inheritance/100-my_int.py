#!/usr/bin/python3
""" a class MyInt that inherits from int: """
Rectangle = __import__('9-rectangle').Rectangle


#!/usr/bin/python3
class MyInt(int):
    """ A class that inherits from the int class."""

    def __eq__(self, other):
        """ Checks if the values are not equal."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Checks if the values are equal."""
        return int.__eq__(self, other)

