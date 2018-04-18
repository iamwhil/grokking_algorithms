# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19
@author: Whil
Following along with the Grokking Algorithms book.
Exercise 1 - Binary Search

Searches through a list for a given item.
Returns the index the item is located at.
* Note: I think the author is familiar with Ruby as he keeps mixing nil and null
* and calls what is in Python a "list" an array, and then corrects himself.
** See `print("list class:", type(my_list))` output.
"""

def binary_search(list, item): 
  low = 0 
  high = len(list) - 1
  
  while low <= high: 
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list = [1,3,5,7,9]
# Display the class of my_list (list, not array).
print("list class: ", type(my_list))

# Run 3 examples
print(binary_search(my_list, 3))
print(binary_search(my_list,4))
print(binary_search(my_list,1))