#!/usr/bin/python3

"""Module containing a function for converting a JSON representation to an object."""
import json


def from_json_string(my_str):
    """ Returns an object based on the specified JSON representation.

    Args:
        my_str: The JSON representation to be decoded.

    Raises:
        Exception: If the string cannot be decoded.

    """
    return json.loads(my_str)
