#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checks if an object is an instance or a subclass of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class type to compare against.

    Returns:
        bool: True if the object is an instance or a subclass of the 	specified class, False otherwise.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
