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


test_suite = [
    {
         "test_name": "Problem 1a",
         "variable_name": "A1",
         "score": .25,
         "description": "Create A1",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
          "test_name": "Problem 1b",
         "variable_name": "b1",
         "score": .25,
         "description": "Create b1",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 1c part 1",
         "variable_name": "L1",
         "score": .25,
         "description": "L1 from LU factorization",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size",
     },
     {
         "test_name": "Problem 1c part 2",
         "variable_name": "U1",
         "score": .25,
         "description": "U1 from LU factorization",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 1d",
         "variable_name": "z1",
         "score": .5,
         "description": "forward substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 1e",
         "variable_name": "x1",
         "score": .25,
         "description": "backward substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2a",
         "variable_name": "A2",
         "score": .25,
         "description": "Create A2",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2b part 1",
         "variable_name": "L2",
         "score": .25,
         "description": "L2 in LU factorization",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2b part 2",
         "variable_name": "U2",
         "score": .25,
         "description": "U2 in LU factorization",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 2D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2c",
         "variable_name": "t0",
         "score": .25,
         "description": "Set up t0",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2d",
         "variable_name": "z2",
         "score": .5,
         "description": "Forward substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2e",
         "variable_name": "t1",
         "score": .25,
         "description": "Backward substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2f",
         "variable_name": "z3",
         "score": .5,
         "description": "Forward substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2g",
         "variable_name": "t2",
         "score": .25,
         "description": "Backward Substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2h",
         "variable_name": "z4",
         "score": .5,
         "description": "forward Substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     },
     {
         "test_name": "Problem 2i",
         "variable_name": "t3",
         "score": .25,
         "description": "backwards Substitution",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a 1D numpy array",
         "hint_wrong_size": "Check that your variable is the correct size"
     }
]


supported_platforms = ["python"]#, "matlab"]
#matlab_credentials = "~/gspack_uw_amath_matlab_credentials"
requirements = ["numpy"]





                
            