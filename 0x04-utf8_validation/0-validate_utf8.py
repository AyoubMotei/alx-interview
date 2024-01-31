#!/usr/bin/python3

"""

This script defines a method to determine whether the given data represents valid UTF-8 encoding.
Method Prototype: def validUTF8(data)
Returns True if the data is a valid UTF-8 encoding; otherwise, returns False.
The dataset can contain multiple characters, and the data will be represented as a list of integers

"""


def validUTF8(data):
    """
    Method Prototype: def validUTF8(data)
    Returns True if the given data is a valid UTF-8 encoding; otherwise, returns False.

    """
    count = 0

    for bit in data:
        binary = bin(bit).replace("0b", "").rjust(8, "0")[-8:]
        if count == 0:
            if binary.startswith("110"):
                count = 1
            if binary.startswith("1110"):
                count = 2
            if binary.startswith("11110"):
                count = 3
            if binary.startswith("10"):
                return False
        else:
            if not binary.startswith("10"):
                return False
            count -= 1

    if count != 0:
        return False

    return True

