#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:09:06 2022

@author: robertocappiello
"""

from cmd import Cmd
import os


 
class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
 
    def do_exit(self, inp):
        print("Bye")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def do_add(self, inp):
        num_1 = int(input("Insert the first number:"))
        num_2 = int(input("Insert the second number:"))
        sum = num_1+num_2
        print("sum is: ", sum)
 
    def help_add(self):
        print("Add a new entry to the system.")
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
    #list all the contents of the current directory when is inserted the command: list    
    def do_list(self, inp):
        list = os.listdir('.')
        print(list)
    
 
    
    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()