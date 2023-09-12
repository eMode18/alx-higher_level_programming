#!/usr/bin/python3
"""Define object lookup function attribute."""


def lookup(obj):
    """Return available object attributes in as a list."""
    return (dir(obj))
