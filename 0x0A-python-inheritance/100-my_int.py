#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """MyInt class that inherits from int"""

    def __eq__(self, other):
        """The equal to method to check equality"""
        if int.__eq__(self, other) == True:
            return False
        else:
            return True

    def __ne__(self, other):
        """The not equal to method to check not equality"""
        if int.__ne__(self, other) == False:
            return True
        else:
            return False
