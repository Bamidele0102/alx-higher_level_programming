#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric_difference operator ^ to find elements unique to each set
    diff_set = set_1 ^ set_2
    return diff_set
