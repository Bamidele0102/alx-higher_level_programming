#!/usr/bin/python3

"""
Define a class MagicClass that represents a magic class with
methods to calculate area and circumference based on the radius.
"""

import math


class MagicClass:
    """
    The MagicClass represents a magic class with methods to
    calculate area and circumference based on the radius.
    """

    def __init__(self, radius=0):
        """
        Initialize a new MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
