#!/usr/bin/python3
"""Defines a function for converting a Python class to a JSON dictionary."""

def class_to_json(obj):
    """Convert a Python class object to a dictionary representation."""
    return obj.__dict__
