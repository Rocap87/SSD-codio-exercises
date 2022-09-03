#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:56:58 2022

@author: robertocappiello
"""


"""corrected version of stylelint code"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Input a number to see the factorial : ")) #receive input from user
print(factorial(n)) # printing the result