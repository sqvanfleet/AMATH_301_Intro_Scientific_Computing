#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:56:58 2024

@author: samvanfleet
"""

import numpy as np

n = 10

x = np.arange(1,n+1)

m = 0

for k in x:
    m = m + k**2
    
print('m = ', m)

