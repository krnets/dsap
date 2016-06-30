#!/usr/bin/env python3

'''
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''

def minmax(data):
    d_min = d_max = data[0]
    for x in data[1:]:
        if x < d_min:
            d_min = x
        if x > d_max:
            d_max = x
    return d_min, d_max


if __name__ == "__main__":
    in_str = input("Enter numbers separated by space:\n\n")
    data = [int(d) for d in in_str.split()]
    data_minmax = minmax(data)
    print("min: {} max: {}".format(data_minmax[0], data_minmax[1]))
