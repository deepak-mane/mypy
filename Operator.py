#!/usr/bin/env python
from __future__ import print_function

# Script Name		: Operator
# Author			: Deepak Mane
# Created			: 8/25/2017
# Last Modified		: 8/25/2017
# Version			: 1.0
# Modifications		: 1.1 - CR - Added some extra code, to check an argument is passed to the script first of all, then check it's a valid input
# Description		: This simple script volume of sphere
'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''
__author__ = 'Deepak Mane'
__version__ = '1.0'

# Arithematic Operators

num1 = 10
num2 = 20


print("Num1 + Num2 =", num1 + num2)
print("Num1 - Num2 =", num1 - num2)
print("Num1 * Num2 =", num1 * num2)
print("Num1 / Num2 =", num1 / num2)
print('5^3 =', 5 ** 3)
print("20 % 3 =", 20 % 3)
print("22//7=", 22 // 7)
print('3.8//2', 3.8//2)

# Assignment Operator
num3 = num1 + num2
print(num3)
num3+=num2  # num3 = num3 + num2
print(num3)

# Comparison Operators
'''
print("Is num 3 > num 2?", num3 > num2)
print("Is num 2 > num 3?", num2 > num3)
print("Is num 1 == num 2?", num1 == num2)
print("Is num 1 != num 2?", num1 != num2)
'''

# Logical Operators
'''
x=True
y=False

print("X and Y", x and y)
print("X or Y", x or y)
print("not of X", not x)
'''

# Bitwise Operator

num4 = 6 # 110
num5 = 2 # 010
'''
print('bitwise and=', num4 & num5)
print('bitwise or=', num4 | num5)
print('bitwise xor=', num4 ^  num5)
'''
print("num4 rightshift by 2", num4 >> 2)
print("num5 leftshift by 2", num5 >> 2)

