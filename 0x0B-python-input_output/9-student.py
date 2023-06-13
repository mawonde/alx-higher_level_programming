#!/usr/bin/python3
""" Module that defines the Student class.
"""


class Student:
    """ Class for creating student instances. """

    def __init__(self, first_name, last_name, age):
        """ Initialize a student instance. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return the dictionary description of the student object. """
        return self.__dict__.copy()
