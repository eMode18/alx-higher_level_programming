#!/usr/bin/python3
"""Defines a function for converting a Python object to a JSON string."""
import json

def to_json_string(my_obj):
    """Convert the provided Python object into its JSON representation.

    Args:
        my_obj (any): The Python object to be converted.
    
    Returns:
        str: The JSON representation of the input object as a string.
    """
    return json.dumps(my_obj)
