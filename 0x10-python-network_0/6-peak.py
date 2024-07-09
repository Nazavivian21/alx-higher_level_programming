#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): A list of unsorted integers.

    Returns:
    int: A peak element from the list. If the list is empty, returns None.
    """
    if not list_of_integers:
        return None

    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_helper(arr, low, high):
    """
    Helper function to find a peak element using binary search.

    Args:
    arr (list): A list of unsorted integers.
    low (int): The lower index of the current sublist.
    high (int): The upper index of the current sublist.

    Returns:
    int: A peak element from the sublist.
    """
    mid = (low + high) // 2

    if (mid == 0 or arr[mid] >= arr[mid - 1]) and (
        mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]
    ):
        return arr[mid]
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_helper(arr, low, mid - 1)
    else:
        return find_peak_helper(arr, mid + 1, high)
