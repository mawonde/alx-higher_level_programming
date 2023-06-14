#!/usr/bin/python3
""" Method that raises an Exception with the message area() is not implemented
"""
class BaseGeometry:
    """A class that defines the attributes and methods of geometric shapes."""

    def area(self):
        """Calculates the area of a geometric shape.

        Raises:
            Exception: This method is not implemented in the base class and must be overridden in the derived classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value for a given property.

        Args:
            name (str): The name of the object/property.
            value (int): The value of the property.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

