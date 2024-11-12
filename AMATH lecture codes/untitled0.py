#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:33:16 2024

@author: samvanfleet
"""

R = 5
f = lambda x: x**3 - R
df = lambda x: 3*x**2
n = 10
x_old = 3
x_new = x_old - f(x_old)/df(x_old)
print(x_new)
print(x_old)
print(abs(x_new - x_old))
epsilon = 10**(-5)
while abs(f(x_old)) > epsilon:
    x_new = x_old - f(x_old)/df(x_old)
    x_old = x_new

    
print(x_new)
