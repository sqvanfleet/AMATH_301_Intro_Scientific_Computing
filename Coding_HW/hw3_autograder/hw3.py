#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:19:02 2024

@author: samvanfleet
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,0,1],[4,-5,2]])
B = np.array([[7,-5,1],[1,-4,-3]])
C = np.array([[1,2],[-2,1]])
D = np.array([[3,5],[-1,4]])
x = np.array([[-5],[3]])

"""
print("A = \n", A)
print("B = \n", B)
print("C = \n", C)
print("D = \n", D)
print("x = \n", x)
"""

ans1 = B - (1/2)*A
ans2 = C@D
ans3 = A + 3*B
ans4 = D@B
ans5 = C@x
ans6 = np.transpose(A) + np.transpose(B)
ans7 = np.transpose(C@D)


A1 = np.zeros((12,15))

for i in range(12):
    for j in range(15):
        A1[i,j] = (i+1)/(j+1)
        


A2 = np.copy(A1)

A2[3:4,:] = 0

A3 = np.copy(A1[2:5,-4:])

A4 = np.copy(A1[1:2,:])


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