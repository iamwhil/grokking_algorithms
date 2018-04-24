# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23, 2018

@author: Whil

Following along in the Grokking Algorithms book.
This is not so much a problem as it is an example given in the book.

* The author continues to consider python lists as arrays, where as
the array.array in python is a wrapper around the C array, which functions
as an array. :/
"""

def find_smallest(arr):
  # Initialize the smallest value.
  smallest = arr[0]
  smallest_index = 0 
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i 
  return smallest_index# find_smallest

def selection_sort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
  return new_arr

# Run an example sort
arr = [5,6,98,3,1,0,117,8,17]
print(selection_sort(arr))
