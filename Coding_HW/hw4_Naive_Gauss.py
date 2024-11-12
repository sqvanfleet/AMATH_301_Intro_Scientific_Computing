#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:55:23 2024

@author: samvanfleet
"""

import numpy as np


#function for Naive Gaussian Elimination based on the pseudocode on page 
#77.



def Naive_Gauss(A,b):
    #A is a 2D array of shape (n,n)
    #b is a 1D array of shape (n,)
    
    n = A.shape[0] # Gets the number of rows of A
    
    #Forward Elimination
    

    xmult = 0 #Initialize xmult
    #Forward Elimination 
    for k in #fill in the range():
        for i in #fill in the range():
            xmult =  #fill in the multiplier of the replacement operation
            for j in #fill in the range():
                A[i,j] = #fill in the right hand side
            b[i] = #fill in the right hand side
    
    #backwards substitution 
    x = np.zeros(n) #initialize a 1D array of zeros for x
    
    x[n-1] = b[n-1]/A[n-1,n-1] # This corresponds to the last row in our system
    
    sum = 0 #initialize the sum variable
    for i in #fill in the range():
        sum =  #fill in the first term in the formula for x_i
        
        for j in #fill in the range():
            sum = #fill in the right hand side
            
        x[i] = #fill in the right hand side
    
    
    return x



#Now use the Naive_Gauss() function to complete problems 1,2, and 3.

















