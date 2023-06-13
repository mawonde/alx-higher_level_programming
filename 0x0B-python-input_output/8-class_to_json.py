#!/usr/bin/python3
""" Module for returning the dictionary description of an object for JSON serialization.
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
