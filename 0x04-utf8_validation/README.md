# 0x04-utf8_validation

## Description
Writes a method that determines if a given data set represents a valid UTF-8 encoding.

<ul>
<li>Prototype: def validUTF8(data)</li>
<li>Return: True if data is a valid UTF-8 encoding, else return False</li>
<li>A character in UTF-8 can be 1 to 4 bytes long</li>
<li>The data set can contain multiple characters</li>
<li>The data will be represented by a list of integers</li>
<li>Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer</li>
</ul>

## Files
[0-validate_utf8.py](0-validate_utf8.py)
[0-main.py](0-main.py)
