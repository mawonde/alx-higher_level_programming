#!/usr/bin/python3
"""Module containing a function for reading from a file."""

def read_file(filename=""):
    """Reads content from a specified file.


    Args:
        filename (str): The name of the file to read.

    Raises:
        Exception: If the file cannot be opened.

    Returns:
        None

    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
