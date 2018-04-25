# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:07:08 2018

@author: Whil
Grokking Algorithms exercise 4.2

Q: Write a recursive function to count the number of items in a list.
"""
# Import array.
from array import array 

def list_len(l):
  '''
  returns the length of an array.
  '''
  if len(l) == 0:
    return 0
  if len(l) == 1:
    return 1
  else:
    l.pop()
    return 1 + list_len(l)

nums = [1,2,3,4,5]
print(list_len(nums))
things = ['cat', 'dog', 'fish', 4]
print(list_len(things))
nothing = []
print(list_len(nothing))
arr = array('f', (1,2,3,4))
print(list_len(arr))