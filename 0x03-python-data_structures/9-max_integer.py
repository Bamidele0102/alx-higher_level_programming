#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None
    # Initialize the max_value with the first element of the list
    max_value = my_list[0]
    # Iterate through the list to find the maximum value
    for number in my_list:
        if number > max_value:
            max_value = number
    return max_value
