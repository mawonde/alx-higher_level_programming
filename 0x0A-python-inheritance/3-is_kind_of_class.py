#!/usr/bin/python3
""" A unction that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or a subclass of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class type to compare against.

    Returns:
        True if the object is an instance or a subclass of the 	specified 	class, False otherwise.
    """
    return isinstance(obj, a_class)
