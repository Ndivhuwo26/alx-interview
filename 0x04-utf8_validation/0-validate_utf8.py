#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    a valid UTF-8 encoding. The function validUTF8(data) processes a list of integers, each representing a byte, and checks if the byte sequence adheres to the rules of UTF-8 encoding, which allows for characters represented in one to four bytes. It effectively handles multiple characters in a single dataset and returns True for valid UTF-8 sequences and False for invalid ones.


    """
    number_bytes = 0

    for byte in data:
        
        if number_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                number_bytes += 1
                mask >>= 1

           
            if number_bytes == 0:
                continue  

            if number_bytes == 1 or number_bytes > 4:
                return False  

        else:
            
            if not (byte & (1 << 7)) or (byte & (1 << 6)):
                return False

        number_bytes -= 1

    return number_bytes == 0  

