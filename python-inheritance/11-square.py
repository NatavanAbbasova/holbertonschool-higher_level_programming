#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize private size with validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description"""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
