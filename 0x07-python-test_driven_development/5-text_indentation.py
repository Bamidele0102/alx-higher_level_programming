#!/usr/bin/python3
"""
Module 5-text_indentation
Contains method that prints text with 2 new lines after each ".", "?", and ":"
Takes in a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    lines = [line.strip() for line in text.split('\n')]
    revised_text = "\n".join(lines)
    print(revised_text, end="")
