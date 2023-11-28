#!/usr/bin/python3
output = ""
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in ['q', 'e']:
        output += "{}".format(chr(char))
print(output, end="")
