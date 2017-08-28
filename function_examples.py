#!/usr/bin/env python
from __future__ import print_function

# Script Name		: function_examples
# Author			: Deepak Mane
# Created			: 8/26/2017
# Last Modified		: 8/26/2017
# Version			: 1.0
# Modifications		: 1.1 - CR - Added some extra code, to check an argument is passed to the script first of all, then check it's a valid input
# Description		: This simple script volume of sphere
'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''
__author__ = 'Deepak Mane'
__version__ = '1.0'


def fibo(n):
    a = 0
    b = 1
    for x in range(n):
        a = b
        b = a + b
        print(a, '\n')
    return b


def main():
    num = int(input("Enter the value of n:"))
    print(fibo(num))


if __name__ == '__main__':
    main()
