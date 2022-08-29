#!/usr/bin/python3

def no_c(my_string):
    length = len(my_string)

    x = 0

    current = my_string[:]

    for i in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            current = current[:(i - x)] + my_string[(i + 1):]
            x += 1

    return (current)
