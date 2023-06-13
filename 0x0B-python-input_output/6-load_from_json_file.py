#!/usr/bin/python3
"""Module for loading an object from a JSON file."""
import json

def load_from_json_file(filename):
    """ Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file.

    Raises:
        Exception: If the object cannot be encoded.

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
