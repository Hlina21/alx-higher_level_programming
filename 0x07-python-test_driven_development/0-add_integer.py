#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(x, y=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(x, int) and not isinstance(x, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(y, int) and not isinstance(y, float))):
        raise TypeError("b must be an integer")
    return (int(x) + int(y))
