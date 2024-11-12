#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:50:51 2024

@author: samvanfleet
"""

import numpy as np


def LU_fac(A):
    A = A.astype("float")
    n = A.shape[0] #get the number of rows of A
    U = A.copy(); #initialize U as A
    L = np.zeros((n,n)) #Initialize L
    for k in range(n):
        L[k,k] = 1; #make L the identity
    
    for j in range(n):  #These loops build L and U.  This is similar to the 
    #forward substitution process of Gaussian Elimination
        for i in range(j+1,n):
            mult = -U[i,j]/U[j,j]
            L[i,j] = -mult
            for k in range(j,n):
                U[i,k] = U[i,k] + mult*U[j,k]
                
    return L,U

def forward_sub(L,b): #Forward substitution is similar to 
    #backwards substitution
    L = L.astype("float")
    b = b.astype("float")
    n = L.shape[0] #gets the number of rows in L
    z = np.zeros(n) #initializes the z vector
    z[0] = b[0] # this is solving the first row of Lz = b
    # The following loop solves remaining rows of Lz = b
    for i in #fill in the range:  We need to go from row 2 to row n 
    #mathematically.  Remeber that python start its indexing at 0 
        sum = # fill
        for j in #fill in the range: The end value for this range depends 
        # on i (the row we are solving for) becasue L is lower triangular
            sum = #fill 
        z[i] = #fill
    return z
    

def backward_sub(U,z):  # this is the backward substitution form the Gaussian 
#elimination code but written using U and z as arguments
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

"""
Example problem for reference on how to input your A1, b1 arrays 



Additionally how to call the functions LU_fac(), forward_sub(), and
backward_sub(), for the variables L1, U1, z1, and x1 arrays
"""

A1 = np.array([[1,2,3],[2,6,10],[3,14,28]])

b1 = np.array([1,0,-8])

L1,U1 = LU_fac(A1)

z1 = forward_sub(L1,b1)

x1 = backward_sub(U1,z1)

#print("x1 = ",x1)














