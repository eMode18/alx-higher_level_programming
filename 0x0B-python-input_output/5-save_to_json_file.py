#!/usr/bin/python3
"""Defines a function for saving a Python object to a JSON file."""
import json

def save_to_json_file(my_obj, filename):
    """Serialize and write a Python object to a JSON file.

    Args:
        my_obj (any): The Python object to be saved.
        filename (str): The name of the JSON file to be created or overwritten.
    """
    with open(filename, "w") as fi_le:
        json.dump(my_obj, fi_le)
