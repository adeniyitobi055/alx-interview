#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    def is_valid_following_byte(byte):
        """
        Checks if a byte starts with `10`
        """
        return byte & 0b11000000 == 0b10000000

    # Variable to keep track of remaining bytes in the current character
    remaining_bytes = 0

    for num in data:
        if remaining_bytes == 0:
            if num & 0b10000000 == 0:  # Single-byte character
                continue
            elif num & 0b11100000 == 0b11000000:  # Two-byte character
                remaining_bytes = 1
            elif num & 0b11110000 == 0b11100000:  # Three-byte character
                remaining_bytes = 2
            elif num & 0b11111000 == 0b11110000:  # Four-byte character
                remaining_bytes = 3
            else:
                return False
        else:
            if not is_valid_following_byte(num):
                return False

        remaining_bytes -= 1

    # If all bytes have been used, it's a valid UTF-8 encoding
    return remaining_bytes == 0
