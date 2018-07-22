#!/usr/bin/env python
from __future__ import print_function

# Script Name		: matplotlib_basic.py
# Author			: Deepak Mane
# Created			: 8/29/2017
# Last Modified		: 8/29/2017
# Version			: 1.0
# Modifications		: 1.1 - CR - Added some extra code, to check an argument is passed to the script first of all, then check it's a valid input
# Description		: This simple script volume of sphere
'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''
__author__ = 'Deepak Mane'
__version__ = '1.0'

from matplotlib import pyplot as plt
# Plotting to our canvas

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54,
                   44, 43, 42, 49]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

# X2 = [ 6, 9, 11]
# Y2 = [6, 15, 7]
# plt.plot(X,Y,'g',label='line one', linewidth=5)
# plt.plot(X2,Y2,'c',label='line one', linewidth=5)


plt.ylabel('y')
plt.xlabel('x')
plt.title('Histogram')
plt.legend()

# plt.grid(True,color='k')
#Showing what we plotted
plt.show()