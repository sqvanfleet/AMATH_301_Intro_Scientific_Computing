#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:20:30 2024

@author: samvanfleet
"""

import numpy as np

n = 3
m = 4
A = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        A[i,j] = 2 + min(i,j) 
print(A)


        
for k in range(n):
    if A[k,k] < 3:
        A[k,k] = 1
    elif A[k,k] < 4:
        A[k,k] = 0
    else:
        A[k,k] = -1
print(A)

