#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:46:02 2024

@author: samvanfleet
"""

import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(-5,5,100)
print(x)
print(x.shape)
y = 1 + x + x**2/2 + x**3/6
z = np.exp(x)
plt.plot(x,y)
plt.plot(x,z)