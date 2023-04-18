#!/usr/bin/python3

"""
ALX-Interview Prep - UTF-8 Validation
"""


def validUTF8(data) -> bool:
    """
    Validating UTF-8 encoding in data
    """
    valid: bool = True

    for n in data:
        if n in range(0, 128):
            continue
        elif n in range(128, 2048, 2):
            continue
        elif n in range(2048, 65536, 3):
            continue
        elif n in range(65536, 1114112, 4):
            continue
        else:
            valid = False
            break

    return valid
