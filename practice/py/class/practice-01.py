# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:30:32 2021

@author: pandey
"""
class point:
    def printpoint(p):
        print('(%g, %g)' % (p.x, p.y))        
    
    def distbetween(a,b):
        import math
        return math.sqrt((b.y-a.y)**2 + (b.x-a.x)**2)
    m1
    # point.x = 0
    # point.y = 0
    "Point represents a point in 2D space"
    "This can also be depicted as a  2D vector"    
blank = point()
blank.x = 4
blank.y = 3
class Rectangle:
    None
    
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

# Create a function which takes rectangle as input and return point
def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

## Objects are Mutable 

box.width = box.width + 10 
box.height = box.height + 20

# We can create a copy or create another instance 
# import copy
# p1 = copy.copy(p)
# p1 is p 
# False

