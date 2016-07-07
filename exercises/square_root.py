#!/usr/bin/env python3

def square_root(n):
    root = n / 2  # initial guess will be 1/2 of n
    for k in range(20):
        root = (1 / 2) * (root + (n / root))

    return root

if __name__ == '__main__':
    a = input("Square root of: ")
    print(square_root(float(a)))
