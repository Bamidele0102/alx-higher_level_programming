#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = [True if number % 2 == 0 else False for number in my_list]
    return result_list
