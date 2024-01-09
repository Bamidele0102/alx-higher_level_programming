#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a file and prints its content."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
