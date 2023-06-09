#!/usr/bin/python3

""" Definition of a square class for size type checking"""
class Square:
    """ A square class definition by the square size
    """
    def __init__(self, size=0):
        """Initialization of the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
