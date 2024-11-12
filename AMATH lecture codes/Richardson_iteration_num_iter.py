#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:16:22 2024

@author: samvanfleet
"""

import numpy as np 
import math

f = lambda x : x - x**3 + 1

a = 0.0 
b = 2.0

n = 1000 #number of iterations

error = b-a # The first error value
for k in range(n):
    c = .5*(b+a) # get the midpoint 
    
    y1 = f(a) # get the function value at a
    y2 = f(c) # get the function value at c
    y3 = f(b) # get the function value at b
    
    if y2*y3 < 0:
        a = c
        y1 = y2
    elif y1*y2 < 0:
        b = c
        y3 = y2
    else:
        break
    error = b-a
print(c)
