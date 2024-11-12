#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:41:41 2024

@author: samvanfleet
"""


import numpy as np

def left_hand_rule(f,a,b,n):
    #This function approximates the definate integral
    #from a to b of f(x).  
    #The arguments of this function are:
    # 1.) f is the function that is being estimated 
    # 2.) a is the left endpoint of the interval 
    # 3.) b is the right enpoint of the interval 
    # 4.) n is the number of subintervals we have.
    

    #Creat the n+1 evenly spaced points from a to b
    x_partition = np.linspace(a,b,n+1) 
    #print(x_partition)
    
    #The formula for the length of the evenly 
    # spaced sub-intervals 
    h = (b-a)/n
    #print("h = ",h)
    
    #We now have all we need to approximate the definate
    #integral with the left hand rule
    
    # you can use a for loop to calculate the sum in 
    # the left hand rule approximation
    left_hand_sum = 0
    for i in range(n):
        left_hand_sum = left_hand_sum + f(x_partition[i])
        # The print statment below helps us see if our 
        # range in the for loop is correct. 
        #print(x_partition[i]) 
    
    left_hand_sum = h*left_hand_sum
    
    return left_hand_sum


#The example we did in class on 2-28

f = lambda x: x**2 
a = -1
b = 1
n = 4

left_hand_rule_1 = left_hand_rule(f,a,b,n)

print("The left hand rule approximation to our "
      "example problem from class is ",
      left_hand_rule_1)

f1 = lambda x: np.sqrt(1+x**(-4))
a = 1
b = 2
n = 100

LHR1a = left_hand_rule(f1,a,b,n)

LHR1b = left_hand_rule(f1,a,b,10000)

print("The left hand rule approximation for 1a" 
      "is ", LHR1a)

print("The left hand rule approximation  for 1b" 
      "is ", LHR1b)

f2 = lambda x: (1/((0.08)*np.sqrt(2*np.pi)))*np.exp(-(x-5.15)**2/(2*(.08)**2))
a = 5
b = 5.25
n = 100

LHR2a = left_hand_rule(f2,a,b,n)
LHR2b = left_hand_rule(f2,a,b,10000)

print("The trapazoid rule approximation to the integral" 
       "is ", LHR2a)

print("The trapazoid rule approximation to the integral" 
       "is ", LHR2b)














        
    
    
    
    
    