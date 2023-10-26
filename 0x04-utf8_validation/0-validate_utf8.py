<<<<<<< HEAD
#!/usr/bin/python3
"""UFT-8 Encoding"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Check if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    count = 0  # Initialize a variable to keep track of the number of bytes
    # remaining for the current character

    for num in data:
        if count == 0:
            # Determine the number of bytes required for the current character
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                # If the 8th bit is set, it's not a valid start of a character
                return False
        else:
            # For continuation bytes, the 2nd highest bit should be '10'
            if (num >> 6) != 0b10:
                return False
            count -= 1  # Decrement the count of remaining bytes for
            # the current character

    return count == 0  # All characters are valid if count is back to 0
=======
#!usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer
"""


def validUTF8(data):
    """_summary_

    Args:
            data (list[int]): a list of integers
    """
    expected_continuation_bytes = 0

    # Define bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        # Initialize a mask to check for leading
        # 1's in the current byte
        leading_one_mask = 1 << 7

        # If we are not currently expecting any
        # continuation bytes
        if expected_continuation_bytes == 0:
            # Count the number of leading 1's in the
            # current byte to determine the number of
            # continuation bytes
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # If the byte is not a multi-byte sequence,
            # move to the next byte
            if expected_continuation_bytes == 0:
                continue

            # If the number of continuation bytes is not
            # between 2 and 4, the sequence is invalid
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False

        # If we are expecting continuation bytes
        else:
            # Check that the byte starts with a "10"
            # prefix and not a "11" prefix
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # Decrement the expected number of continuation bytes
        expected_continuation_bytes -= 1

    # If we have processed all bytes and are not expecting
    # any more continuation bytes, the sequence is valid
    if expected_continuation_bytes == 0:
        return True
    else:
        return False
>>>>>>> 0d391d806e85686aa8b48df1edea52b1a305f5ac
