#!/usr/bin/python3
""" a class Square that inherits from Rectangle (9-rectangle.py) """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a Square based on the Rectangle class."""

    def __init__(self, size):
        """Initializes a Square with a given size.

        Args:
            size (int): The size of the Square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return super().area()

