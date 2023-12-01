#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    size = len(args)

    if size != 1:
        plural = "s" if size != 0 else ""
        print("{} argument{}:".format(size, plural))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, args[0]))
