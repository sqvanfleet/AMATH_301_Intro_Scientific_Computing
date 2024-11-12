#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:50:51 2024

@author: samvanfleet
"""

import numpy as np


def LU_fac(A):
    A = A.astype("float")
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

def forward_sub(L,b):
    L = L.astype("float")
    b = b.astype("float")
    n = L.shape[0]
    z = np.zeros(n)
    z[0] = b[0]
    for i in range(1,n):
        sum = b[i]
        for j in range(0,i):
            sum = sum - L[i,j]*z[j]
        z[i] = sum
    return z
    

def backward_sub(U,z):
    U = U.astype("float")
    z = z.astype("float")
    n = U.shape[0]
    x = np.zeros(n)
    x[n-1] = z[n-1]/U[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = z[i]
        for j in range(i+1,n):
            sum = sum - U[i,j]*x[j]
        x[i] = sum/U[i,i]
    return x




A1 = np.array([[1,2,3],[2,6,10],[3,14,28]])

b1 = np.array([1,0,-8])

L1,U1 = LU_fac(A1)

z1 = forward_sub(L1,b1)

x1 = backward_sub(U1,z1)




A2 = np.array([[3,-1,0,0],[-1,3,-1,0],[0,-1,3,-1],[0,0,-1,3]])

t0 = np.array([10,15,15,10])

L2,U2 = LU_fac(A2)

z2 = forward_sub(L2,t0)

t1 = backward_sub(U2,z2)

print(t1)

z3 = forward_sub(L2,t1)

t2 = backward_sub(U2,z3)

print(t2)

z4 = forward_sub(L2,t2)

t3 = backward_sub(U2,z4)

print(t3)

z5 = forward_sub(L2,t3)

t4 = backward_sub(U2,z5)

print(t4)