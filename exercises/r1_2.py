#!/usr/bin/env python3

'''
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):
    return not k & 1

if __name__ == "__main__":
    n = input("Enter a number to see if it's even: ")
    print(is_even(int(n)))
