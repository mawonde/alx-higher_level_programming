#!/usr/bin/python3

"""A square class definition to calculate position of a square"""

class Square:
    """ A square class  definition by the square size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of the square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to return the value of the size 
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the  value of the size of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Method that returns a position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that returns the square area of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square 
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
