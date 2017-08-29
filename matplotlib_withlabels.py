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
X = [ 5, 8, 10]
Y = [12, 16, 6]

plt.plot(X,Y)

plt.title("Info")
plt.ylabel("Yaxis")
plt.xlabel("Xaxis")


#Showing what we plotted
plt.show()