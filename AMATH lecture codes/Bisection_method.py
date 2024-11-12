#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:38:08 2024

@author: samvanfleet
"""

import numpy as np 
import math # we need this for the math.ceil() function

def Bisection(func, a, b, num_iter): 
    # The func argument is a function that we want the root of 
    # a and b are the left and right endpoints of the interval 
    # epsilon is the desired length of the interval 
    
    # There is no need to assign a and b to x1 and x3.

    error = b-a # The first error value
    c = .5*(b+a)
    for k in range(num_iter):
        
        
        y1 = func(a) # get the function value at a
        print("y1 = ",y1)
        y2 = func(c) # get the function value at c
        print("y2 = " , y2)
        y3 =  func(b) # get the function value at b
        print("y3 = " , y3)
        error = .5*error # overwrite error as the new error
        
        if y2*y3 < 0:
            a = c
            y1 = y2
        elif y1*y2 < 0:
            b = c
            y3 = y2
        else:
            break
        c = .5*(b+a) # get the midpoint 
        print("iteration ",k+1," is ", c)
        
    return c




f = lambda x : x**3-9*x+2

a = 1
b = 5
num_iter = 4


r = Bisection(f, a, b, 4)

print(r)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    