#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Extract the last digit of the number
last_digit = abs(number) % 10
# Check and print the characteristics of the last digit
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print(f"less than 6 and not 0")
