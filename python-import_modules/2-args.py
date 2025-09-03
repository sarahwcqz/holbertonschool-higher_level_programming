#!/usr/bin/python3
import sys

argv = sys.argv

if __name__ == "__main__":
    # if 0 arg other than name of prgm
    if len(argv) == 1:
        print("0 arguments.")
    # if 1 arg => no 's' at the end of word
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv)))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
