#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list
and provides a method to print the list sorted.
"""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self, key=lambda x: int(x)))
