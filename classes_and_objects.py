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


class Student:
    perc_rise = 1.05

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + '@school.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)


Std_1 = Student("Neel", "Verma", 60)
Std_2 = Student("Hemant", "Sharma", 90)


class Dumb(Student):

    perc_rise = 1.10

    def __init__(self, first, last, marks, prog_lang):
        super().__init__(first, last, marks)
        self.prog_lang = prog_lang

Std_1 = Dumb('Neel', 'Verma', 60, 'Python')
print(Std_1.prog_lang)


# Std_1 = Dumb('Neel', 'Verma', 60)
# print(Std_1.perc_rise)
# Std_1 = Student('Neel', 'Verma', 60)
# print(Std_1.perc_rise)
# # print(help(Dumb))
# Std_2 = Student('Hemant', 'Sharma', 90)
# print(Std_1.first)
# print(Std_1.email)
# print(Std_1.fullname())
# print(Std_1.marks)
# Std_1.apply_raise()
# print(Std_1.marks)
#
# print(Std_2.first)
# print(Std_2.email)
# print(Std_2.fullname())
# print(Std_2.marks)
# print(Std_2.marks)
# Std_2.apply_raise()
# print(Std_2.__dict__)
# print(Student.__dict__)
