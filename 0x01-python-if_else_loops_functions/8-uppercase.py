#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase character to uppercase using ASCII values
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            # Print the character as is if it's not lowercase
            print("{}".format(char), end="")
    print()
