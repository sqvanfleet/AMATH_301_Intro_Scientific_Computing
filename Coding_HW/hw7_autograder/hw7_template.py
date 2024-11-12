#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 

"""
The y array represents the population (in millions)
of the united states starting at the year 1800, increasing 
by 10 years up to the year 1910.

For example there were 7.240 million people living in the united states
in 1810.
"""

y = np.array([5.308,7.240,9.638,12.861,17.064,
              23.192,31.443,38.558,
              50.189,62.980,76.212,92.228])
n = y.shape[0]
dt = 10 

"""
We can use the difference method
to approximate the growth rate of the united states population 
from the years 1800 through 1900
"""


"""
Forward difference
"""


forward_diff = np.zeros(n)

for i in range(n-1):

    forward_diff[i] = (y[i+1]-y[i])/dt
    

"""
We can use the backwards difference method
to approximate the growth rate of the united states population 
from the years 1810 through 1910
"""

backward_diff = np.zeros(n)

for i in range(1,n):
    
    #fill in the backwards difference formula
    
    
    
"""
We can use the backwards difference method
to approximate the growth rate of the united states population 
from the years 1810 through 1910
"""

central_diff = np.zeros(n)

for i in range(1,n-1):
    
    #Fill in the central difference formula 
    
print(forward_diff)

print(backward_diff)

print(central_diff)















