#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:39:53 2024

@author: samvanfleet
"""

"""
lecture 1-16-2024

This script is divided into cells that start with 
 "#%%".  To run an individual cell, click on that 
 cell and then press "shift + enter"

"""


import numpy as np

#%% 
"""
Creating evenly spaced arrays using 
np.linspace(start,stop,number).

np.linspace(start,stop,number) creates an array of
evenly spaced array of #number# elements 
between start and stop.  It will include the stop
value.

For example
"""

x = np.linspace(1,5,100)
print("x = " + str(x))

#%%
"""
Creating evenly spaced arrys using 
np.arrange(start,stop,step).

np.arrange(start,stop,step) creates an array 
whose first element is #start#, second element is
#start + step#, ..., and whose last element is 
#stop - step#.

For example
"""
x = np.arange(1,5,.5)
print("x = " + str(x))

x = np.arange(5,1,-0.5) 
print("x = " + str(x))


#%%
"""
So far we have been using 1D arrays but to work 
with vectors and matrices we need 2D arrays.

Let us start by turning 1D arrays into 
2D arrays that represent vectors.

One way to do this is to use the 
np.reshape(array_name,(rows,columns)).
This will create an array with the elements of
#array_name# with shape (rows,columns).  
For example
"""

x = np.array([1,2,3,4]) # 1D array 
print("x = " + str(x))
print("x has this many dimensions " + str(x.ndim))
print("x has shape = " + str(x.shape))

#%%

x = np.reshape(x,(1,4)) #overwirtes x as a row
#vector
print("x = " + str(x))
print("the dimensions of x are now " + 
      str(x.ndim)) #Multi-Line statement
print("x has shape = " + str(x.shape))

#%%

x = np.reshape(x,(4,1)) #overwirtes x as a
#column vector
print("x = " + str(x))
print("the dimensions of x are now " + 
      str(x.ndim)) #notice statements including 
#() can be multiline statments
print("x has shape = " + str(x.shape))



#%%
"""
Sometimes it is useful to use the shape with 
np.reshape(array_name,(rows,cols)) 
For example lets say we wanted to calculate the 
transpose of a vector 
"""
x_rows = x.shape[0] #the first entry is the 
#number of rows.
x_cols = x.shape[1] #the second entry is the
#number of columns.

print("x = " + str(x))

x_transpose = np.reshape(x,(x_cols,x_rows))
print("x^T = " + str(x_transpose))


#%%
"""
We will represent matrices in Python using 2D arrays.  Here is 
an example of a 4x3 matrix saved as an np.array
"""

A = np.array([[-1,2,1],[3,0,-1],[4,-2,2],[-2,1,3]])
# ses the entire matrix, and then
# each row is enclosed in another set of brackets.
# You then use commas to separate entries within a row and to 
# separate different rows.
print("A = " + str(A))
print("A is of type " + str(type(A)))
print("A has dimensions = " + str(A.ndim))
print("The shape of A = " + str(A.shape))

#%%
"""
Note that we can also create column and row vectors directly without
using the reshape command.  For example
"""
x = np.array([[1],[2],[3]]) 
y = np.array([[4,5,6]])
print("x = " + str(x))
print("x is of type " + str(type(x)))
print("x has dimensions = " + str(x.ndim))
print("The shape of x = " + str(x.shape))

print("y = " + str(y))
print("y is of type " + str(type(y)))
print("y has dimensions = " + str(y.ndim))
print("The shape of y = " + str(y.shape))


#%%

"""
We can preforme matrix arithmitic provided our matrices are
appropriate sizes.  Along with the matrix A defined above, let us
define the matrices B, C, and D
"""

B = np.array([[1,-2,0,3],[2,1,-4,1],[-3,0,1,1]])
C = np.array([[1,0,2],[3,-1,1],[2,2,0]])
D = np.array([[1,2,-1],[3,-2,2],[-1,1,0]])

"""
Here are some examples of the elementwise operations you can 
preforme on matrices.
"""

print("A = " + str(A))
print("A + 5 = " + str(A + 5)) #adds 5 to each element of A
print("B = " + str(B))
print("B - 2 = " + str(B - 2)) #subtracts 2 from each element of B
print("C = " + str(C))
print("C*3 = " + str(3*C)) #multiplies each element by 3
print("D = " + str(D))
print("D/4 = " + str(D/4)) #divides each element by 4
print("A = " + str(A))
print("A**2 = " + str(A**2)) #squares each element

#%% 
"""
We can also preform matrix addition and subtraction and we can
also preform elementwise multiplication and division
"""

print("C + D = " + str(C+D))# Add each element of C to its
#corresponding element of D.
print("C - D = " +str(C-D)) #subtracts each element of D from its 
#corresponding element in C.
print("C*D = " + str(C*D)) #multiplies each corresponding element 
#of C and D.

 #%%
 print("C/D = " + str(C/D)) # will result in an error since this 
 # this takes each element of C and divides it by its
 # corresponding element in D but some of the elements in D are 0.
 
 #%%
 print("C**D = " + str(C**D)) # will result in an error but this is
 # more technical he problem is that we only used whole numbers 
 #when constructing our matrices and so python assumed that we 
 #wanted elements of type int.  Unfortunately, python does not 
 # allow raising integers to negative powers.
 
 #%%
 #One way to fix this is to construct an array of floats instead
 
C_float = np.array([[1.0, 0, 2], [3, -1, 1], [2, 2, 0]])
print("C = " +str(C))
print("C_float = " + str(C_float))
print("C_float**D = " + str(C_float ** D))

"""
Replacing just one of the entries as a decimal caused all of the
entries in C_float to be floats
"""

#%%
"""
We can also change C to a matrix of floats with
array_name.astype("float64").
"""
print("The elements of C have type = " + str(C.dtype))
C = C.astype("float64")
print("The elements of C now have type = " + str(C.dtype))

#%%%
"""
To add two matrices they must have the same size.  For example
"""
print("A is of shape " + str(A.shape))
print("B is of shape " + str(B.shape))
print("A + B = " + str(A+B)) #Error because A and B are different 
#shapes.

#%%

"""
Accessing and modifying entries of a matrix works similarily to 
1D arrays.  Let us see what happens when we try A[2]
"""
print("A = " + str(A))
print("A[2] = " + str(A[2])) # the third row of A
print("A[0] = " + str(A[0])) # the first row of A
print("A[-1] = " + str(A[-1]))# the last row of A

#%%

"""
If you want to access an individual element of a matrix instead 
of an entire row, you have to use one more set of brackets. For
example, the second entry (index 1) in the 
third row (index 2) can be found with the code
"""

print("A = " + str(A))
print("A[2,1] = " + str(A[2,1]))

"""
In general this is name_array[row_index,col_index].
"""

#%%
"""
We can use array slicing to access submatrices.  For example
"""
print("A = " + str(A))
print("A[1:3,0:3] = " + str(A[1:3,0:3]))
"""
Remeber that when using the : for slicing 1:3 means indices 1 and 2
but not 3 and 0:3 means indices 0, 1, and 2 but not 3. 

In general start:stop will give all the indecies starting at #start# 
up to but not including #stop#

We can also omit #start# and it will assume that start is 0
"""
print("A[:3,0:3] = " + str(A[:3,0:3]))

"""
If we omit #stop# python will assume that stop is the last index
but include it for example
"""

print("A[1:3,1:] = " + str(A[1:3,1:]))
print("A[1:3,1:].shape = " + str(A[1:3,1:].shape))

#%%
"""
If both the stop and start are omited then python uses every 
index for example 
"""

print("A[:, 0:2] = " + str(A[:, 0:2]))
print("A[1,:] = " + str(A[1,:]))
print("A[:,2] = " + str(A[:,2]))

"""
Unfortunately the shape of the these resulting arrays is not 
perserved when you do this
"""

print("A[1,:].shape = " + str(A[1,:].shape)) #shape is not preserved
print("A[:,2].shape = " + str(A[:,2].shape)) #shape is not preserved
print("A[1:3,:].shape = " + str(A[:,0:2].shape)) #shape is preseved

#%%%

"""
Thankfully we can use np.reshape here manually correct the shape
"""

print("A[1,:] = " + str(A[1,:]))
print("A[1,:].shape = " + str(A[1,:].shape))
#%%
print("np.reshape(A[1,:],(1,-1)) = " + str(np.reshape(A[1,:],(1,-1))))
print("np.reshape(A[1,:],(1,-1)).shape = " + 
      str(np.reshape(A[1,:],(1,-1)).shape))
#%%

print("np.reshape(A[:,2],(-1,1)) = " + str(np.reshape(A[1,:],(-1,1))))
print("np.reshape(A[1,:],(-1,1)).shape = " + 
      str(np.reshape(A[1,:],(-1,1)).shape))

#%%

"""
Yet another option to extract rows and columns from a matrix and 
retain their shape when using the : operator is to replace a single 
number with a slice.  For example the index 2 and the slice 2:3 
are the same thing.  
"""

print("A[1:2, :] = " + str(A[1:2, :]))
print("A[1:2, :].shape = " + str(A[1:2,:].shape))
#%%

print("A[:,2:3] = " + str(A[:,2:3]))
print("A[:,2:3].shape = " + str(A[:,2:3].shape))

"""
The benifit here is that we do not need to reshape our array
"""

#%%

"""
Python has a matrix multiplication operator and it is @.  For example
if the matrices A and B are defined as 
"""

A = np.array([[-1,2,1],[3,0,1],[4,-2,2],[-2,1,3]])
B = np.array([[1,-2],[2,1],[-3,0]])

print("A = " + str(A))
print("B = " + str(B))
#%%
print("A@B = " + str(A@B))


#%%

"""
Since A is 4x3 matrix and B is a 3x2 matrix B@A is not defined.
"""
print("B@A = " + str(B@A)) #Error

#%%
"""
The dot product when vectors a and b are expressed as 1D arrays using 
np.dot(a,b).
"""

a = np.array([2,-3,1,4])
b = np.array([-1,-2,1,3])

print("a = " + str(a) + "\n and a has shape " + str(a.shape))
print("b = " + str(b) + "\n and a has shape " + str(b.shape))
#%%
print("np.dot(a,b) = " + str(np.dot(a,b)))
print("np.dot(b,a) = " + str(np.dot(b,a)))

#%% 
"""
When a and b are expressed as 2D arrays (in order to specify 
    row or column vector) then we can use the 
"""
a = np.reshape(a,(-1,1)) #overwrite a 
b = np.reshape(b,(-1,1)) #overwrite b

print("the shape of a is now " + str(a.shape))
print("the shape of b is now " + str(b.shape))

#%%
print(np.dot(a,b))

#%%

"""
When a and b are column vectors or 2D arrays of shape (:,1),
the dot product is the matrix multiplication a^Tb.  
We can use array_name.transpose and the @ 
operator to calculate the dot product.
"""

print("a = " + str(a))
print("np.transpose(a) = " + str(np.transpose(a)))
#%%
print("np.transpose(a)@b = " + str(np.transpose(a)@b))
dot = np.transpose(a)@b
#%%
print("dot[0,0] = " + str(dot[0,0]))










