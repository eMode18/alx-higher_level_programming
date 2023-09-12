#!/usr/bin/python3
"""Defines a function for loading a Python object from a JSON file."""
import json

def load_from_json_file(filename):
    """Read and deserialize a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be read.
    
    Returns:
        any: The Python object loaded from the JSON file.
    """
    with open(filename) as fi_le:
        return json.load(fi_le)
