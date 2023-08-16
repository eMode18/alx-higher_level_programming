#!/usr/bin/python3
def minus(num_list):
    neg = 0
    list_max = max(num_list)

    for n in num_list:
        if list_max > n:
            neg += n

    return (list_max - neg)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    in_romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key_list = list(in_romans.keys())

    rom = 0
    last_num = 0
    num_list = [0]

    for d in roman_string:
        for n in key_list:
            if n == d:
                if in_romans.get(d) <= last_num:
                    rom += minus(num_list)
                    num_list = [in_romans.get(d)]
                else:
                    num_list.append(in_romans.get(d))

                last_num = in_romans.get(d)

    rom += minus(num_list)

    return (rom)

