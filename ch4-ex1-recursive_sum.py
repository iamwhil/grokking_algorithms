# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:00:45 2018

@author: Whil

Grokking Algorithms Exercise 4.1
"Write out the code for the earlier sum function."
* The earlier sum function was a recursive function to add numbers 
  together found in an array / list.
  
"""

def sum(numbers):
  if len(numbers) == 0:
    return 0
  if len(numbers) == 1:
    return numbers[0]
  else:
    return numbers.pop() + sum(numbers)

# Test cases
numbers = [1,2]
print(sum(numbers))
numbers = [1]
print(sum(numbers))
numbers = []
print(sum(numbers))
numbers = [1,2,3,4,5]
print(sum(numbers))