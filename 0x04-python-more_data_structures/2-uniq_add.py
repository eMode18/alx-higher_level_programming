#!/usr/bin/python3
def uniq_add(my_list=[]):
    custom_list = set(my_list)
    _add = 0

    for d in custom_list:
        _add += d

    return (_add)
