#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:54:39 2024

@author: samvanfleet
"""

import numpy as np
n = 4
m = 3

def create_matrix(n,m):
    A = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            den = (i+1)*(j+1)
            A[i,j] = 1/den
    return A

A = create_matrix(n,m)

v = np.linspace(0,3.75,6)

u = np.arange(3,4.1,1/6)


A = np.array([[3,1,4],[-2,0,1],[1,2,2]])

B = np.array([[1,0,2],[-3,1,1],[2,-4,1]])

v = np.linspace(0,3.75,6)

u = np.arange(3,4.1,1/6)

w = np.array([1.0,2,4,5,6])
