#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use set to remove duplicates, then sum the unique integers
    unique_sum = sum(set(my_list))
    return unique_sum
