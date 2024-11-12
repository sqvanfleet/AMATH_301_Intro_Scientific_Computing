#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:29:57 2024

@author: samvanfleet
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,0,-1],[4,-5,2]])
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








test_suite = [
    {
        "test_name": "Problem 1a matrix A",
        "variable_name": "A",
        "description": "Initialize A",
        "atol": 1e-8,
        "score": .2,
        "hint_not_defined": "Double check that you named your array A.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your A variable should be a 2x3 2D array."
    },
    {
        "test_name": "Problem 1a matrix B",
        "variable_name": "B",
        "description": "Initialize B",
        "atol": 1e-8,
        "score": .2,
        "hint_not_defined": "Double check that you named your array B.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy Array.",
        "hint_wrong_size_python": "Your B variable should be a 2x3 2D array."
    },
    {
        "test_name": "Problem 1a matrix C",
        "variable_name": "C",
        "description": "Initialize C",
        "atol": 1e-8,
        "score": .2,
        "hint_not_defined": "Double check that you named your answer C.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your C variable should be a 2x2 2D array."
    },
    {
        "test_name": "Problem 1a matrix D",
        "variable_name": "D",
        "description": "Initialize D",
        "atol": 1e-8,
        "score": .2,
        "hint_not_defined": "Double check that you named your answer D.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your D variable should be a 2x2 2D array."
    },
    {
        "test_name": "Problem 1a vector x",
        "variable_name": "x",
        "description": "Initialize x",
        "atol": 1e-8,
        "score": .1,
        "hint_not_defined": "Double check that you named your answer x.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your x variable should be a 2x1 2D array."
    },
    {
        "test_name": "Problem 1b",
        "variable_name": "ans1",
        "description": "Calculate B-(1/2)A",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans1.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x3 2D array."
    },
    {
        "test_name": "Problem 1c",
        "variable_name": "ans2",
        "description": "Calculate CD",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans2.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x2 2D array.",
        "hint_wrong_operator_python": "Make sure to use @ and not * for matrix multiplication"
    },
    {
        "test_name": "Problem 1d",
        "variable_name": "ans3",
        "description": "Calculate A + 3B.",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans3.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x3 2D array.",
    },
    {
        "test_name": "Problem 1e",
        "variable_name": "ans4",
        "description": "Calculate DB.",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans4.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x3 2D array.",
        "hint_wrong_operator_python": "Make sure to use @ and not * for matrix multiplication"
    },
    {
        "test_name": "Problem 1f",
        "variable_name": "ans5",
        "description": "Calculate Cx.",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans5.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x1 2D array.",
        "hint_wrong_operator_python": "Make sure to use @ and not * for matrix multiplication"
    },
    {
        "test_name": "Problem 1g",
        "variable_name": "ans6",
        "description": "Calculate A^T + B^T.",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans6.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 3x2 2D array.",
        "hint_wrong_function_python": "Make sure to use np.transpose()"
    },
    {
        "test_name": "Problem 1h",
        "variable_name": "ans7",
        "description": "Calculate (CD)^T.",
        "atol": 1e-8,
        "score": .3,
        "hint_not_defined": "Double check that you named your answer ans7.",
        # "hint_tolerance": "",
        "hint_wrong_type_python": "Make sure you are using a numpy array.",
        "hint_wrong_size_python": "Your answer should be a 2x2 2D array.",
        "hint_wrong_function_python": "Make sure to use np.transpose()"
    },
    {
        "test_name": "Problem 2a",
        "variable_name": "A1",
        "description": "Create A1 with for loops.",
        "atol": 1e-8,
        "score": .8,
        "hint_not_defined": "Double check that you named your answer A.",
        # "hint_tolerance": "",
        "hint_python": "This can be done without the incrementing technique.",
        "hint_wrong_size_python": "Your answer should be a 12x15 2D array."
    },
    {
        "test_name": "Problem 2b",
        "variable_name": "A2",
        "description": "Create A2.",
        "atol": 1e-8,
        "score": .4,
        "hint_not_defined": "Double check that you named your answer A2.",
        # "hint_tolerance": "",
        "hint_python": "Try array slicing.",
        "hint_wrong_size_python": "Your answer should be a 1x15 2D array."
    },
    {
        "test_name": "Problem 2c",
        "variable_name": "A3",
        "description": "Create A3.",
        "atol": 1e-8,
        "score": .4,
        "hint_not_defined": "Double check that you named your answer A3.",
        # "hint_tolerance": "",
        "hint_python": "Are you slicing the right rows and columns.",
        "hint_wrong_size_python": "Your answer should be a 3x4 2D array."
    },
    {
        "test_name": "Problem 2d",
        "variable_name": "A4",
        "description": "Create A4.",
        "atol": 1e-8,
        "score": .4,
        "hint_not_defined": "Double check that you named your answer A4.",
        # "hint_tolerance": "",
        "hint_python": "Are you slicing the right rows and columns.",
        "hint_wrong_size_python": "Your answer should be a 1x15 2D array."
    },
]

supported_platforms = ["python"]#, "matlab"]
#matlab_credentials = "~/gspack_uw_amath_matlab_credentials"
requirements = ["numpy"]
























