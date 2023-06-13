#!/usr/bin/python3
"""Module containing a function for converting an object to its JSON representation."""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of the specified object.

    Args:
        my_obj: The object to be converted to JSON.

    Raises:
        Exception: If the object cannot be encoded.

    """
    return json.dumps(my_obj)
