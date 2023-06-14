#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Adds a new attribute to an object.

    Args:
        obj (object): The object to which the attribute will be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

