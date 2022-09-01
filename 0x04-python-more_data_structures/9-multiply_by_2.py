#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ = a_dictionary.copy()
    list_ = list(new_.keys())

    for i in list_:
        new_[i] *= 2

    return (new_)
