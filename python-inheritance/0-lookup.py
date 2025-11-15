#!/usr/bin/python3
"""
This module provides the lookup function which returns
a list of available attributes and methods of an object.
"""

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
