#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:23:24 2024

@author: samvanfleet
"""

x = .75

if x < -1:
    y = (x+3)**3
elif x < 1:
    y = -x**2 + 9
elif x < 2:
    y = -x+9
else:
    y = -(1/4)*x**2+8
    
print("y = ", y)