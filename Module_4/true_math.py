"""
    True math operation
"""
from math import inf


def divide(first, second):
    """
        True math divide function
    """
    if second == 0:
        if first > 0:
            return inf
        elif second < 0:
            return -inf
        else:
            return 0
    else:
        return first/second
