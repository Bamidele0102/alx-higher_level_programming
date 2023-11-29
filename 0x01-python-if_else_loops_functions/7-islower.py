#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')


# Test the function
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('7'))  # False
