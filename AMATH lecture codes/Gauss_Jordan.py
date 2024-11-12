#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:14:53 2024

@author: samvanfleet
"""

import numpy as np


#function for Naive Gaussian Elimination based on the pseudocode on page 
#77.



def Gauss_Jordan(A,b):
    #A is a 2D array of shape (n,n)
    #b is a 1D array of shape (n,)
    A = A.astype("float") #Cast any array of ints to a float array
    b = b.astype("float") #Cast any array of ints to a float array
    n = A.shape[0] #Gets the number of rows of A

    #Row Reduce A to a Diagonal matrix
    for k in range(n): #Outermost step of the algorithm that corresponds
        #to kth step of Gauss_Jordan Eilimination.
        if A[k,k] == 0:
            print("Divison by zero without pivoting")
        for i in range(n): #Middle loop corresponding to the row of the
            #elementary row replacment operation.
            if i != k:
                
                xmult = A[i,k]/A[k,k] #multiplier of the elementary
                #row replacement operation
                for j in range(k,n): #Inner loop corresponding to the column of 
                #elementary row replacment operation
                    A[i,j] = A[i,j] - xmult*A[k,j]
                b[i] = b[i] - xmult*b[k]
    #obtain the solution
    x = np.zeros(n) #initialize a 1D array of zeros for x
    

    #Scale the elements of b by the diagonal elements of A
    for i in range(n): #loop for obtaining our answer x
        x[i] = b[i]/A[i,i]
    return x
        

#First test

A1 = np.array([[1,2,3],[2,6,10],[3,14,28]])
b1 = np.array([1,0,-8])



x1 = Gauss_Jordan(A1,b1)


print("x1 = ", x1)