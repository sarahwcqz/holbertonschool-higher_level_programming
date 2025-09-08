#!/bin/usr/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx > 0 and idx <= element:
        new_list[idx] = element
    return new_list
