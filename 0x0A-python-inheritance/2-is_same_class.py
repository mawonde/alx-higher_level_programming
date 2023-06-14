#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class (class): The class type to compare against.

    Returns:
        True if the type of the object is the same as the specified class, 	False otherwise.
    """
    return type(obj) is a_class
