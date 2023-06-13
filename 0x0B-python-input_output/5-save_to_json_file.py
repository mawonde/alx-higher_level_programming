#!/usr/bin/python3
"""Module for saving an object to a text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """ Writes the specified object to a text file using JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename: The name of the text file.

    Raises:
        Exception: If the object cannot be encoded.

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
