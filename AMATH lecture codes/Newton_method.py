#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:05:36 2024

@author: samvanfleet
"""


def Newton_method(f,df,x0,n): #Notice functions can 
#be passed as arguments
    for i in range(n):
        x = x0 - f(x0)/df(x0) #newtons update step
        x0 = x # set x0 = x for the next step in newtons method
        
    return x

f = lambda x: x**4 + 2*x**3-7*x**2 + 3 # The function
# we want to use Newton's method on

df = lambda x: 4*x**3 + 6*x**2 - 14*x # The derivative of 
# the funciton we want to take the derivative of

n = 3

x0 = 1

x = Newton_method(f, df, x0, n)

print("x = ",x)




