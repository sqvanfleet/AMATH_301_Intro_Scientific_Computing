#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:52:41 2024

@author: samvanfleet
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:09:42 2024

@author: samvanfleet
"""

def Newton_method(f,df,x0,epsilon): #Notice functions can 
#be passed as arguments
    num_steps = 0 #initialize the number of steps
    while #Fill in the while loop condition for our stoping criteria:
        x = x0 - f(x0)/df(x0) #newtons update step
        x0 = x # set x0 = x for the next step in 
        #newtons method
        num_steps = num_steps + 1 #update the number 
        #of steps
    return x,num_steps

f = lambda x: # Fill in the function
# we want to use Newton's method on to find a root

df = lambda x: 3#Fill in the derivative of 
# the funciton we want to find a root 

epsilon = 10**-8

x0 = 1 #our initial guess

x,n = Newton_method(f,df,x0,epsilon)

print("x = ",x)
print("f(x) = ", f(x))
print("the number of steps is ", n)