#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:03:46 2024

@author: samvanfleet
"""

import numpy as np
size = 12
A = np.zeros((size,size))



for i in range(size):
    for j in range(size):
        A[i,j] = (i+1)/(j+1)
        
        
print(A)