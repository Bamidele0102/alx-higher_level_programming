#!/usr/bin/python3
"""
This is a simple Square class with a private instance attribute.
"""


class Square:
    """
    The Square class represents a geometric square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.

        Note:
        The size parameter is not type or value verified.
        """
        self.__size = size
