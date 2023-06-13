#!/usr/bin/python3
""" Module containing a function for appending to a text file.
"""


def append_write(filename="", text=""):
    """ Appends the specified text to a text file.

    Args:
        filename: The name of the file to append.
        text: he text to be appended to the file.

    Raises
        Exception: If the file cannot be opened.

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
