#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:18:36 2024

@author: samvanfleet
"""

import numpy as np


def trap_rule(f,a,b,n):
    #This function approximates the definate integral
    #from a to b of f(x).  
    #The arguments of this function are:
    # 1.) f is the function that is being estimated 
    # 2.) a is the left endpoint of the interval 
    # 3.) b is the right enpoint of the interval 
    # 4.) n is the number of subintervals we have.
    

    #Creat the n+1 evenly spaced points from a to b
    x_partition = np.linspace(a,b,n+1) 

    
    #The formula for the length of the evenly 
    # spaced sub-intervals 
    h = (b-a)/n

    
    
    #For the trapazoid rule we add the first and last heights 
    #in the partition separately.
    
    #The foor loop should calculate the sum of all of the 
    #elements on the interior of our partition
    trap_rule_sum = 0
    for i in range(1,n):
        trap_rule_sum = trap_rule_sum + f(x_partition[i])

    
    trap_rule_sum = h*trap_rule_sum
    #add the heights of the first and last points in our 
    #partition multiplied by h/2
    trap_rule_sum = trap_rule_sum + (h/2)*(f(a)+f(b))
    
    return trap_rule_sum


f1 = lambda x: np.sqrt(1+x**(-4))
a = 1
b = 2
n = 100

TR1a = trap_rule(f1,a,b,n)

TR1b = trap_rule(f1,a,b,10000)

print("The trapazoid rule approximation to the integral" 
      "is ", TR1a)

print("The trapazoid rule approximation to the integral" 
      "is ", TR1b)

f2 = lambda x: (1/((0.08)*np.sqrt(2*np.pi)))*np.exp(-(x-5.15)**2/(2*(.08)**2))
a = 5
b = 5.25
n = 100

TR2a = trap_rule(f2,a,b,n)
TR2b = trap_rule(f2,a,b,10000)

print("The trapazoid rule approximation to the integral" 
       "is ", TR2a)

print("The trapazoid rule approximation to the integral" 
       "is ", TR2b)


test_suite = [
    {
         "test_name": "Problem 1a",
         "variable_name": "TR1a",
         "score": 1.25,
         "description": "Trapazoid Rule arc length",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float"
     },
    {
         "test_name": "Problem 1b",
         "variable_name": "TR1b",
         "score": 1.25,
         "description": "Trapazoid Rule arc length",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float"
     },
    {
         "test_name": "Problem 2a",
         "variable_name": "TR2a",
         "score": 1.25,
         "description": "Trapazoid Rule baseball weight",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float"
     },
    {
         "test_name": "Problem 2b",
         "variable_name": "TR2b",
         "score": 1.25,
         "description": "Trapazoid Rule baseball weight",
         "hint_not_defined": "Check that your variable is defined",
         "hint_wrong_type": "Check that your variable is a float"
     }
    ]



supported_platforms = ["python"]#, "matlab"]
#matlab_credentials = "~/gspack_uw_amath_matlab_credentials"
requirements = ["numpy"]