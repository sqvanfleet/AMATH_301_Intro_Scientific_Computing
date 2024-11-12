#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 07:05:32 2024

@author: samvanfleet
"""

import numpy as np

def fibonacci_function(F1, F2, N):
    fib = np.zeros(N)
    fib[0] = F1
    fib[1] = F2
    
    for i in range(2,N):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib