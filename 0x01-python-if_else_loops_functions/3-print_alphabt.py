#!/usr/bin/python3
for a in range(97, 123):
    if a == 101:
        continue
    elif a == 113:
        continue
    else:
        print("{}".format(chr(a)), end='')
