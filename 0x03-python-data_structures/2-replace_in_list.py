#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        b = element
        my_list[idx] = b
        return my_list
