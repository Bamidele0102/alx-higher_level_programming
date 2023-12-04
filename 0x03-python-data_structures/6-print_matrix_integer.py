#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Join the integers in the row using ' ' and print
        print(' '.join("{:d}".format(num) for num in row))
