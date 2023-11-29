#!/usr/bin/python3
for tens_digit in range(9):
    for units_digit in range(tens_digit + 1, 10):
        print("{:02d}".format(tens_digit * 10 + units_digit), end=", ")
print("{:02d}".format(89))
