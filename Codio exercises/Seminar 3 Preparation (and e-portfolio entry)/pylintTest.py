#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:07:19 2022

@author: robertocappiello
"""


# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string
 
shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
  for letter in word:
    if letter == ' ':
      encoded = encoded + ' '
    else:
      x = letters.index(letter) + shift
      encoded=encoded + letters[x]
    if choice == "decode":
      for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
          x = letters.index(letter) - shift
          encoded = encoded + letters[x]

print (encoded)