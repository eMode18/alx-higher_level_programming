#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        tally = 0
        for ele in my_list:
            if tally < x:
                print(ele, end=" ")
                tally += 1
        print() """print new line"""
        return tally
    except:
        return tally
