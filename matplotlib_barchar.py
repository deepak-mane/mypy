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
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="example two", color='g')

# X2 = [ 6, 9, 11]
# Y2 = [6, 15, 7]
#
# plt.plot(X,Y,'g',label='line one', linewidth=5)
# plt.plot(X2,Y2,'c',label='line one', linewidth=5)

plt.title("Bar Chart Info")
plt.ylabel("Yaxis")
plt.xlabel("Xaxis")
plt.legend()

plt.grid(True,color='k')
#Showing what we plotted
plt.show()