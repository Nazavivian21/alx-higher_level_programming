#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list):
        return None
    a = my_list[idx]
    if idx > 0:
        return a
    elif idx < 0:
        return None
