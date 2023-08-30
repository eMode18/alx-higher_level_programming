#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dvd = a / b
    except (ZeroDivisionError):
        dvd = None
    finally:
        print("Inside result: {}".format(dvd))
        return dvd
