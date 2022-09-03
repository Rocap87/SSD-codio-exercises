#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:45:36 2022

@author: robertocappiello
"""

#!python
import re

postcode = input("Type your postcode:")

z = re.match(r"^[a-zA-Z]{1,2}\d[a-zA-Z\d]?\s?\d[a-zA-Z]{2}$", postcode)

print(z)

if z:
    print("Valid Postcode")
else:
    print("Invalid Postcode!")