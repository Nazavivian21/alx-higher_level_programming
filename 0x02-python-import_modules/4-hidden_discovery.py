#!/usr/bin/python3
import hidden_4

a = dir(hidden_4)
for i in a:
    if i[0:2] == '__':
        continue
    print(i)
