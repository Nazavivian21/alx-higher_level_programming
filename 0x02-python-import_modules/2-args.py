#!/usr/bin/python3
import sys

a = sys.argv[1:]
b = len(a)
if b > 0:
    if b == 1:
        print("{} argument:".format(b))
    else:
        print("{} arguments:".format(b))
    count = 0
    for c in a:
        count = count + 1
        print("{}: {}".format(count, c))
else:
    print("{} arguments.".format(b))
