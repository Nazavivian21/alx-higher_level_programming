#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    else:
        return [replace if search == n else n for n in my_list]
