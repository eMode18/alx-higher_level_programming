#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_lib = a_dictionary.copy()
    key_list = list(new_lib.keys())

    for m in list key_list:
        new_lib[m] *= 2

    return (new_lib)
