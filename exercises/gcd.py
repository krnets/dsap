#!/usr/bin/env python3

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


if __name__ == '__main__':
    a, b = input("Enter a number to find greatest common divisor: ").split()
    print(gcd(int(a), int(b)))
