#!/usr/bin/env python3

'''
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def is_multiple(n, m):
    return n % m == 0


if __name__ == "__main__":
    a, b = input("Enter two integers separated by space: ").split()
    print("is " + a + " multiple of " + b + "?\n", is_multiple(int(a), int(b)))
