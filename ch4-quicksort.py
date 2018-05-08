# -*- coding: utf-8 -*-
"""
Created on Mon May 7, 2018

@author: Whil

Grokking Algorithm Quicksort.
Following along with the book, or rather going back and doing this, as I somehow skipped this.
This has 2 quick sort else: blocks.
The first one I constructed from memory.
The second was copied from the book. 
I changed 'less' to 'ltoet' and 'greater' to 'greater_than' to work with my return statement.
"""

# Rnadomly picking the pivot.
import random

def quicksort(array):
  if len(array) < 2: 
    return array
  
  # This was my method not copied from the book, rather just following the algorithm as I imagined it.
  else:
    pivot = array.pop(random.randrange(0, len(array) - 1))
    ltoet = [] # Less than or equal to - array for numbers less than the pivot.
    greater_than = [] # Greater than - array for numbers greater than the pivot.
    for i in array:
      if i <= pivot:
        ltoet.append(i)
      else:
        greater_than.append(i)
    
#  # This is the code from the book.  I like the way this array is constructed, I had no idea of this syntax.
#  else:
#    pivot = array[0]
#    ltoet = [i for i in array[1:] if i <= pivot]
#    greater_than = [i for i in array[1:] if i > pivot]
    
    # Recursive call to sort the greater than and less than arrays.
    return quicksort(ltoet) + [pivot] + quicksort(greater_than) 
  
# Test cases.
array = [1,5,3,7,11,9,13,15]
print(quicksort(array))

array = []
print(quicksort(array))

array = [0]
print(quicksort(array))

array = [1]
print(quicksort(array))

array = [1,0,-1]
print(quicksort(array))