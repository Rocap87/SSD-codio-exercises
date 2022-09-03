#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:29:51 2022

@author: robertocappiello
"""


#CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON



def fn_sum(num_1, num_2):
    """ A function which performs a sum """
    return num_1 + num_2

def find_optimal_route_to_my_office_from_home(start_time,expected_time,
                                              favorite_route='SBS1K',
                                              favorite_option='bus'):
    """find optimal route to return home from the office"""
    distance = (expected_time - start_time).total_seconds()/60.0

    if distance<=30:
        return 'car'

# If d>30 but <45, first drive then take metro
    if 30<distance<45:
        return ('car', 'metro')

# If d>45 there are a combination of optionsWriting Modifiable and Readable Code
    if 45<distance<60:
        # First volvo,then connecting bus
        return ('bus:335E','bus:connector')
    return ':'.join((favorite_option, favorite_route))

class Charlie():
    """ A class which does almost nothing """
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def f_function(self):
        """ Function f to return num_2 """
        return self.num_2

    def g_function_cobra(self):
        """ Function g to check """
        if self.num_1 > self.num_2:
            return self.num_1 + self.num_2
        return self.num_1 + self.num_2

class Delta(Charlie):
    """ D class """
    def __init__(self,num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def f_function(self):
        """ Function that return the value of y + x """
        if self.num_1 > self.num_2:
            return self.num_1 - self.num_2
        return self.num_1 + self.num_2

    def g_function_domino(self):
        """ Function that return the value of y - x """
        if self.num_1 > self.num_2:
            return self.num_1 + self.num_2
        return self.num_2 - self.num_1
