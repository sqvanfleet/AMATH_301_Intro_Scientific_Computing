#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:09:11 2024

@author: samvanfleet
"""

"""
Here is some python code that approximates f'(1) if f(x) = sin(x).  Here we 
will use the forward difference formula.
"""

#For this function we can get the exact solution.  It wont always be the case 
#where the exact answer can be found by hand but for this example we can 
#compare the exact answer with our approximation.

import numpy as np 
#call the variable a the point we want to approximate the derivative at 
a = 1
true_solution = np.cos(a)
print("true solution = ",true_solution)

#%%
"""
Lets use several different values of h to approximate our derivative 
"""

h = np.zeros(5)
for k in range(5):
    h[k] = (10)**(-k)

print("Array of h values = ", h)

#%%


"""
For each of these h values lets compute the approximate derivative using 
the forward difference scheme
"""

forward_difference = np.zeros(5)

f = lambda x:np.sin(x)

for k in range(5):
    forward_difference[k] = (f(a+h[k])-f(a))/h[k]
    
print("forward_difference = ", forward_difference)

#%%%

"""
Now lets take a look at the error: one way to do this is to look at the 
absolute value between the approximation and the true solution
"""

print(abs(forward_difference - true_solution))

"""
Notice the patteren of errors.  At each step, the error gets divided by 10. 
We also know that we divided h by 10 at each step, so this really 
is a first order method.
"""














