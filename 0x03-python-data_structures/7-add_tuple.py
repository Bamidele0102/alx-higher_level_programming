#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuples are smaller than 2, pad with 0
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Return a new tuple with the sums
    return (a[0] + b[0], a[1] + b[1])
