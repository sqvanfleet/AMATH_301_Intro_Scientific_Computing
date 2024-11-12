#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:09:42 2024

@author: samvanfleet
"""

def Newton_method(f,df,x0,epsilon): #Notice functions can 
#be passed as arguments
    num_steps = 0 #initialize the number of steps
    while abs(f(x0)) > epsilon:
        x = x0 - f(x0)/df(x0) #newtons update step
        x0 = x # set x0 = x for the next step in 
        #newtons method
        num_steps = num_steps + 1 #update the number 
        #of steps
        print("x = ",x)
    return x,num_steps

f = lambda x: x**3 - 2*x - 5 # The function
# we want to use Newton's method on

df = lambda x: 3*x**2 - 2 # The derivative of 
# the funciton we want to take the derivative of

epsilon = 10**-8

x0 = 1

x,n = Newton_method(f,df,x0,epsilon)

print("x = ",x)
print("f(x) = ", f(x))
print("the number of steps is ", n)


test_suite = [
    {
         "test_name": "Problem 1a",
         "variable_name": "x",
         "score": 2,
         "description": "Approximate root",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float "
     },
    {
         "test_name": "Problem 1b",
         "variable_name": "n",
         "score": 1,
         "description": "number of iterations",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float "
     }
    ]


supported_platforms = ["python"]#, "matlab"]
#matlab_credentials = "~/gspack_uw_amath_matlab_credentials"
requirements = ["numpy"]