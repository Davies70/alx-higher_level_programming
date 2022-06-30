#!/usr/bin/python3
import sys
if __name__ == "__main__":
    y = 0
    for i in range(1, len(sys.argv)):
        y += int(sys.argv[i])
    print(y)
