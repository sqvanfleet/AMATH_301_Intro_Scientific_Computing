#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 07:10:39 2024

@author: samvanfleet
"""

import numpy as np 

def Richardson_iter(A,b,num_iter):
    n = A.shape[0]
    A = A.astype("float")
    b = b.astype("float")
    Ident = np.identity(n)
    x_old = np.zeros(n)
    x_new = x_old.copy()
    
    for k in range(num_iter):
        x_new = (Ident-A)@x_old + b
        x_old = x_new.copy()
    
    return x_new






A = np.array([[5,-1,0],[-1,3,-1],[0,-1,-2]])

A1 = np.array([[1,.5],[.5,1]])

b = np.array([7,4,5])

b1 = np.array([3,3])

num_iter = 4

x = Richardson_iter(A1, b1, num_iter)

print(x)


