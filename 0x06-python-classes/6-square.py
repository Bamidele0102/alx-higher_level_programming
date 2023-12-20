#!/usr/bin/python3
"""
This is a Square class with private instance attributes,
size and position validation,
properties, area method, and a method to print the square.
"""


class Square:
    """
    The Square class represents a geometric square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square.
        Defaults to 0.
        - position (tuple, optional): The position of the square.
        Defaults to (0, 0).

        Raises:
        - TypeError: If size is not an integer or
        position is not a tuple of 2 positive integers.
        - ValueError: If size is less than 0 or position values are
        not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        - value (int): The size to set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        - value (tuple): The position to set.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If position values are not positive integers.
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)
                ):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is 0, prints an empty line.
        Position is used to adjust the starting position of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
