#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:42:46 2024

@author: samvanfleet
"""

import numpy as np
def left_hand_rule(f,a,b,n):
    x = np.linspace(a,b,n+1) 
    h = (b-a)/n
    sum = 0
    for i in range(n):
        sum = sum + f(x[i+1])
    sum = h*sum
    return sum

f = lambda x: (x+1)**2 
a = -1
b = 1
n = 4

left_hand_rule_1 = left_hand_rule(f,a,b,n)

print("The left hand rule approximation to our "
      "example problem from class is ",
      left_hand_rule_1)