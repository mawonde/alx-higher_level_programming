#!/usr/bin/python3

"""A square class for working with objects"""

class Square:
    """ A square class definition the sqaures's size
    """
    def __init__(self, size=0):
        """ Initialization of the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)
