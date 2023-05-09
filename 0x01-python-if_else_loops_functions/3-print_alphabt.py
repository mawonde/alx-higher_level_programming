#!/usr/bin/python3
for ascii_char in range(97, 123):
    if chr(ascii_char) != 'q' and chr(ascii_char) != 'e':
        print("{}".format(chr(ascii_char)), end="")
