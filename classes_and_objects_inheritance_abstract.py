#!/usr/bin/env python
from __future__ import print_function

# Script Name		: classes-objects.py
# Author			: Deepak Mane
# Created			: 8/28/2017
# Last Modified		: 8/28/2017
# Version			: 1.0
# Modifications		: 1.1 - CR - Added some extra code, to check an argument is passed to the script first of all, then check it's a valid input
# Description		: This simple script volume of sphere
'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''
__author__ = 'Deepak Mane'
__version__ = '1.0'

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod

    def caclulate_salary(self, sal):

        pass
# This below code will not work of Creating Object from Abstract class.
# Only you can inherit certain features from Base Class to Child Class (e.g Developer) and then you can create object from the Child class
# emp_2 = Employee()
# emp2.sal = 10000
# print(emp_2.sal)

class Developer(Employee):

    def caclulate_salary(self, sal):

        finalsalary = sal * 1.10

        return finalsalary

    def position_1(self, position):

        self.position = position

        return position

emp_1 = Developer()
# print(emp_1.caclulate_salary(10000))
print(emp_1.position_1('Web developer'))