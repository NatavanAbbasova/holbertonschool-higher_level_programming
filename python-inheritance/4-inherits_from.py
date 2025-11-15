#!/usr/bin/python3
"""
This module defines a function that checks
if an object is an instance of a class that
inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class,
    otherwise returns False.
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
