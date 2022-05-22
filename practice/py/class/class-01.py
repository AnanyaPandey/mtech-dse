# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 08:28:31 2021

@author: pandey
"""
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
# can have another functions as well which will define clas's objects properties

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def tellyourname(self):
         # When we ask a person to tell name, we need to specfy 
         # which person are we asking this to, thats why self.
         # Self means object that s created from this person class
         # e.g. p = person('raj',20), then p.tellyoutname(), p is passed as self
         # self is the current instance : p
         
         print("My Name is :"+self.name)

## IMP NOTICE 
# self can be any name not necessarily self but it should be the first variable.
# of any function in the class definition.

# Discarding / deleting any property : 
    
del p1
del p1.name
del p1.age


# Class should not be emepty
class anyclass:
    None
    
Class anyclass:
    pass

class B:
	def __init__(self,a):
		self.a = a
	def __add__(self,other):
		return self.a * other.a
        
obj1 = B(5)
obj2 = B(10)

