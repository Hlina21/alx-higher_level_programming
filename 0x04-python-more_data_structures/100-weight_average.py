#!/usr/bin/python3

def weight_average(my_list=[]):
    return sum([y[0] * y[1] for y in my_list]) / \
            (sum([y[1] for y in my_list]) or 1)
