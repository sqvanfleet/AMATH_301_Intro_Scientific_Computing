#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:37:32 2024

@author: samvanfleet
"""

import numpy as np 
import matplotlib.pyplot as plt

x1 = np.linspace(-2,2,100)

y1 = 1 + x1 + x1**2/2 + x1**3/6

f1 = np.exp(x1)

plt.figure(1)
plt.plot(x1,y1,x1,f1)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("p3","f"))
plt.title("Taylor Approximation")

x2 = np.linspace(-5,5,100)

y2 = 1 + x2 + x2**2/2 + x2**3/6

f2 = np.exp(x2)

plt.figure(2)
plt.plot(x2,y2,x2,f2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("p3","f"))
plt.title("Taylor Approximation")