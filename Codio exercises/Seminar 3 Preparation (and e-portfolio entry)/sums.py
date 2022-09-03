#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:08:23 2022

@author: robertocappiello
"""


# SOURCE OF CODE: https://realpython.com/python-testing/

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")