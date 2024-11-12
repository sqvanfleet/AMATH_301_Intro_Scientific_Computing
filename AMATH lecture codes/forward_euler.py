#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 07:46:35 2024

@author: samvanfleet
"""

import numpy as np 
import matplotlib.pyplot as plt

def forward_Euler(f,a,b,x0,n):
    # This function approximates the solution to the
    # initial value problem x' = f(t,x), x(a) = x0.
    #1.) f is the right hand side of the ODE
    #2.) a is the t value in the initial condition 
    #3.) We use Euler's method to approximate x(b) along with 
    # every evenly spaced point between a and b.
    #4.) x0 is the x value in the initial condition
    #5.) n is the number of steps for Euler's method it is also the number of 
    #sub-intervals in the partition t_0 = a, t_1 = a+h, t_2 = a+2h, ..., 
    #t_n = a+nh = b.
    h = (b-a)/n
    t = np.linspace(a,b,n+1)
    x = np.zeros(n+1)
    x[0] = x0 #set the first value of x to the initial condition
    for i in range(n):
        x[i+1] = x[i] + h*f(t[i],x[i])
        
    return t,x






f1 = lambda t,x:-3*t**2*x
a1 = 0
x0p1 = 3
b1 = 1/2
n1 = 25
f1_exact = lambda t: 3*np.exp(-t**3)

t1,x1 = forward_Euler(f1, a1, b1, x0p1, n1)



plt.plot(t1,x1)
plt.plot(t1,f1_exact(t1))
plt.legend(("Euler's approximate soution", "Exact solution"))

#%%
f2 = lambda t,x: (1/3)*x*(8-x)
a2 = 0
x0p2 = 1
b2 = 5
n2 = 25
f2_exact = lambda t: 8/(1+7*np.exp(-8*t/3))

t2,x2 = forward_Euler(f2, a2, b2, x0p2, n2)



plt.plot(t2,x2)
plt.plot(t2,f2_exact(t2))
plt.legend(("Euler's approximate soution", "Exact solution"))




