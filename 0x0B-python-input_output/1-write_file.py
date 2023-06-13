#!/usr/bin/python3
""" Module containing a function for writing to a text file."""


def write_file(filename="", text=""):
    """ Writes the specified text to a text file.

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: If the file cannot be opened.

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
