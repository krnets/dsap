#!/usr/bin/env python3

'''
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def sum_squares(n):
    sum = 0
    for x in n:
        sum = sum + (n * n)
    return sum

if __name__ == "__main__":
    a = input("Enter a positive integer: ")
    print("Sum of squares", sum(int(a)))
