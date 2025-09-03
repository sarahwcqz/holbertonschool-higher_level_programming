#!/usr/bin/python3
import sys

argv = sys.argv
result = 0

if __name__ == "__main__":
    for i in range(1, len(argv)):
        result = result + int(argv[i])
    print("{}".format(result))
