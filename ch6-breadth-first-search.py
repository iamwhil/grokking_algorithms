# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:44:31 2018

@author: Whil

Grokking Algorithsm - ch 6 - breadth first search
Copy of code from book.
"""

from collections import deque

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False

def person_is_seller(person):
  return person == "tom"
  
graph = {}
graph['you'] = ['alice', "bob", "claire"]
graph['alice'] = ['peggy']
graph['bob'] = ['tom']
graph['claire'] = []
graph['peggy'] = []

search('you')