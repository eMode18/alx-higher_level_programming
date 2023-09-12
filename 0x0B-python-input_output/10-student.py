#!/usr/bin/python3
"""Defines a class named Student."""

class Student:
    """Represents a student's information."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): student's first name.
            last_name (str): student's last name.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the Student object into a dictionary representation.

        If attrs is a list of strings, it represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to include in the dictionary.
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
