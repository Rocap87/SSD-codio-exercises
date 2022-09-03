#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 10:32:46 2022

@author: robertocappiello
"""

#runcount set initially as zero because of no moves done
runcount = 0 

#define function for tower of Hanoi
def TowerOfHanoi(n, origin_peg, destination_peg, auxilary_peg):

    #if number of disk is greater than zero the diskd will be moved
    if n > 0:
        global runcount
        runcount += 1 
        TowerOfHanoi(n - 1, origin_peg, auxilary_peg, destination_peg)
        print("Move disk", n, "from peg", origin_peg, "to peg", destination_peg)
        TowerOfHanoi(n - 1, auxilary_peg, destination_peg, origin_peg)

#ask user how many disks has the tower of hanoi
n = int(input("How many disk has the tower of Hanoi?"))
TowerOfHanoi(n, 'A', 'C', 'B')

#it prints the moves and the number of moves necessary to move the disks
#from the origin peg to the destination peg
print (runcount)