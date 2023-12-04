#!/usr/bin/python3
def no_c(my_string):
    # Filter out characters 'c' and 'C'
    filtered_string = ''.join(char for char in my_string if char.lower() not in {'c'})
    return filtered_string
