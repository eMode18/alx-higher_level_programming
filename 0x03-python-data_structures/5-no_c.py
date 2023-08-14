#!/usr/bin/python3

def no_c(my_string):
    _str = [_char for _char in my_string if _char != 'c' and _char != 'C']
    return ("".join(_str))
