#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:00:47 2022

@author: robertocappiello
"""

def factorial(n):
    if n < 0:
        return("Number cannot be negative!")
    elif n == 0:
        return 1

    else:
        n * factorial(n - 1)
#insert number whihc must be an integer otherwise will be get an error
n=int(input("Input a number to see the factorial : "))
print(factorial(n))