#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:50:51 2024

@author: samvanfleet
"""

import numpy as np


def LU_fac(A):
    n = A.shape[0]
    U = A.copy();
    L = np.zeros((n,n))
    for k in range(n):
        L[k,k] = 1; #make L the identity
    
    for j in range(n):
        for i in range(j+1,n):
            mult = -U[i,j]/U[j,j]
            L[i,j] = -mult
            for k in range(j,n):
                U[i,k] = U[i,k] + mult*U[j,k]
                
    return L,U
        



A = np.array([[1,2,3],[2,6,10],[3,14,28]])

L,U = LU_fac(A)
print(L)
print(U)
print(L@U)


                
            