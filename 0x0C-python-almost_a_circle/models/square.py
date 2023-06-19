#!/usr/bin/python3
"""Module containing the Square class, a subclass of Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        
        Args:
            size (int): Length of the sides of the square.
            x (int): X coordinate of the square's position (default: 0).
            y (int): Y coordinate of the square's position (default: 0).
            id (int): Unique ID of the square (default: None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        The string includes information about the square's ID,
        position ('x' and 'y' coordinates), and size (length of sides).

        Returns:
            str: String representation of the square.
        """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_square + str_id + str_xy + str_size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable length argument list. If provided, the
                order of arguments should match the order of the
                attributes ('id', 'size', 'x', 'y').
            **kwargs: Arbitrary keyword arguments. Each keyword
                should correspond to an attribute name, and the
                associated value will be assigned to that attribute.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square,
                containing attribute names as keys and attribute
                values as values.
        """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res

