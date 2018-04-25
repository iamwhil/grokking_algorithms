# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:34:26 2018

@author: Whil
Grokking Algorithms example 4.4

Binary search with regression.
* Assumes that list provided is sorted.
"""

def search(target, num_list, low, high):
  ''' Simple binary search.
      Target: number ot find
      num_list: sorted list of numbers
      low: low index to utilize.
      high: high index to utilize.
  '''
  if num_list[low] == target:
    return low
  if low == high:
    return None
  else:
    mid = (low + high // 2)
    if num_list[mid] == target:
      return mid
    elif num_list[mid] > target :
      # target is smaller than the middle value, set high to mid.
      return search(target, num_list, low, mid - 1)
    else:
      # target is larger than middle value, set low to middle.
      return search(target, num_list, mid + 1, high)
      

# Test runs
num_list = [1,3,5,7,9,11,13,15]
find_me = 15
print(search(find_me, num_list, 0, len(num_list) - 1))
find_me = 4
print(search(find_me, num_list, 0, len(num_list) - 1))