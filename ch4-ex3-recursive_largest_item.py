# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:25:16 2018

@author: Whil
Grokking Algorithsm Exercise 4.3

Find the maximum number in a list.
* As this is in the recursive chapter, I assume it wants a 
  recursive solution.
  If not we can just scan through the list once and find the largest number.
"""

def loopy_largest(lst):
  if len(lst) == 0:
    return "Can not search empty list."
  else:
    largest = lst[0]
    for i in range(1, len(lst)):
      if lst[i] > largest:
        largest = lst[i]
      # end, hahahaha oh me. Ruby.
    # end
    return largest
  # end
# end
  
def largest(lst):
  if len(lst) == 0:
    return "Can not search empty list."
  if len(lst) == 1:
    return lst[0]
  else:
    num = lst.pop()
    lrgst = largest(lst)
    if num > lrgst:
      return num
    else:
      return lrgst
  
lst = [1,5,6,2]
print("The largest number: ",largest(lst))
    
    