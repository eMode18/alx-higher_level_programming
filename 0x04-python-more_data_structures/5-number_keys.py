#!/usr/bin/python3
def number_keys(a_dictionary):
    total = 0
    key_list = list(a_dictionary.keys())

    for k in key_list:
        total += 1

    return (total)
