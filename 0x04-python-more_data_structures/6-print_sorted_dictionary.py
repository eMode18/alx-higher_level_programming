#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = list(a_dictionary.keys())
    ord_list.sort()
    for k in ord_list:
        print("{}: {}".format(k, a_dictionary.get(k)))
