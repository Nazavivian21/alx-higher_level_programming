#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = sys.argv
    sum = 0
    for a in i[1:]:
        j = int(a)
        sum = sum + j
    print("{}".format(sum))
