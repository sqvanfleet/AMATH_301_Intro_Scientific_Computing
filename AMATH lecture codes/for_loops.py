#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:12:14 2024

@author: samvanfleet
"""

import numpy as np

"""
Now we will discuss loops,
A programming concept that allows you to repeate a block of code
many times.

Suppose that we want to make the row vector x = [[0 1 2 3 4]]
as an array in python. We know at least two very easy ways to do so.
We could write it out like this
"""

x = np.array([[0, 1, 2, 3, 4]])
print("x = ", x)

#%%
"""
or we could use the arange function like this
"""
x = np.arange(0, 5)
x = np.reshape(x, (1, -1))
print("x = ", x)
#%%
"""
But suppose that we did not know about the arange function 
and did not want to type out the whole vector.

Another approach would be to make an "empty vector" x 
and then fill in the correct entries. By "empty vector", 
I mean a vector of the appropriate size but without the correct values.


Two ways to do this in python are with the np.zeros((m,n)) and the
np.ones((m,n)).  These two commands create a 2D array of shape (m,n) 
filled with zeros and ones respectively.  Note that np.zeros(m) or 
np.ones(m) creates a 1D array of zeros or ones of shape (m,)
"""

print(np.zeros((3, 4)))
#%%

print(np.zeros(5))
#%%
print(np.ones((3, 4)))
#%%
print(np.ones(5))
#%%
"""
If we want to make an empty vector of the same size as x,
we can therefore use
"""

x = np.zeros((1, 5))
print("x = ",x)

#%%
"""
One way to get the vector we want is to manually assign the values
"""

x[0, 0] = 0
x[0, 1] = 1
x[0, 2] = 2
x[0, 3] = 3
x[0, 4] = 4
print(x)

#%%
"""
Although this works for our example, it is not practical for large 
creating large arrays

This is exactly what a for loop is for. If you want to repeat 
the same block of code several times, you can use the 
python for keyword. For example, to repeat some code five times, 
we could write the code

In general it looks like
for variable_name in range(number_of_steps): 
    other code
    
    
The indentation is neccecary in python.  
Anything indented after the line 
for variable_name in range(number_of_steps):

will be apart of the loop

Here is our first example of a for loop
"""

for k in range(10):
    print(8)
    
#%%
"""
below is what python is really doing with this for loop
"""
k = 0
print(8)
k = 1
print(8)
k = 2
print(8)
k = 3
print(8)
k = 4
print(8)
k = 5 
print(8)
k = 6
print(8)
k = 7
print(8)
k = 8
print(8)
k = 9
print(8)


    
#%%
"""
In the for loop two cells above, we have told python to 
print 8 for each value of k starting from k = 0, k = 1,... all
the way to k = 9.  k = 10 is not included in typical python fashion.

- the variable k is called a loop counter or a loop index or a 
loop variable

- for is a reserved python word telling python to start a for loop

- in is a reserved python word that is used in for loops

- range(10) essentially tells python that the loop variable k needs to
go from 0 up to but not including 10

Here is are some examples of a slightly different, 
for loops note that you can use the loop variable inside your loop!
"""

for k in range(10):
    print(k)

#%%

for k in range(10):
    print("k = ", k)

#%%

for k in range(15):
    print("k = ", k)

#%%

for i in range(4):
    print("i = ",i," and i^2 = ", i**2)
    
#%%

"""
Now that we have tested a few for loops, we can try to use a loop to 
construct the row vector x = [1 2 3 4] as a 2D array
"""

x = np.zeros((1,5)) #pre-define x as a 2D array of zeros with shape
#(1,5)
for j in range(5): 
    x[0, j] = j
    
print(x)

#%%
"""
Below is what python is actually doing when it runs this for loop.  
"""
j = 0
x[0,j] = j
j = 1 
x[0,j] = j
j = 2
x[0,j] = j
j = 3
x[0,j] = j
j = 4
x[0,j] = j

print(x)

#%%
"""
For loops are widely used in practice and we will need to use them 
often in our course.

for practice, we will use a for loop to create another
vector, x = [1 1.1 1.2 1.3 1.4]^T as a 2D array.
"""



"""
One strategy for this is to use an incrementing approac and 
the idea is to assign the first desired value
to a variable before the loop, lets call it x_value.  Then we identify 
a pattern and use it to overwrite x_value on each step of the loop. 
Finally we can use this in our calculation 

We also must not forget to create a correctly shaped 2D array of zeros 
before the loop
"""

x_value = 1 #initialization
x = np.zeros((5,1))

for k in range(5):
    x[k,0] = x_value 
    x_value = x_value + 0.1
    
print(x)

#%%

"""
The incrementing approach described above is a standard approach 
and should almost always be your first choice. In this case, 
however, we have another interesting option:
We can find a formula for x_value interms of k. 
In particular, we can use
"""

x = np.zeros((5, 1))
for k in range(5):
    x[k, 0] = 1 + 0.1 * k
    
print("x = ", x)

#%%
"""
It is worth noting that the range(5) part of our for loops 
can be generalized quite a bit. For example, we can replace 
it with the syntax range(start, stop, step)

- This syntax makes the loop variable begin at start and increase 
in increments of step until just before it reaches stop.

For example,
"""

for k in range(2, 12, 3):
    print(k)

#%%
"""
We can replace range with a wide variety of different statements. 
A discussion of what exactly range does or what statements are allowed 
to replace it is well beyond the scope of this class. 
That said, it is useful to know that we can replace the 
range statement with a 1D numpy array. 


For example we can make the following array 
"""
x = np.arange(3,10)#note here that when arange(3,10) is used 
# it assumes the step is 1. i.e. it is the same as arange(3,10,1)
print("x = ", x)
y = np.sin(x) 
print("y = ", y)

#%%
"""
now we can use the 1D arrays x or y in the place of the range(value)
in our for loops.  For example
"""

for k in x:
    print(k)
    
#%%
    
for j in y:
    print(j)

#%%
"""
As you can see, when we use a 1D numpy array instead of range, 
the loop variable takes on the value of each entry 
of the array in turn.


For now, it is a good idea to use range() in your for loops whenever
possible.

"""
#%%%
"""
Now lets try to use a nested loop to fill a 4 by 3 matrix.

Just as we had to initialize a 1D array we also have to initialize 
a 2D array.  One approach is to use np.zeros((num_rows,num_cols)).
This creates a 2D array with shape (num_rows,num_cols).
"""

"""
Without a for loop you would need to do something like
"""
A = np.zeros((4, 3))
A[0, 0] = 1
A[0, 1] = 2
A[0, 2] = 3

A[1, 0] = 4
A[1, 1] = 5
A[1, 2] = 6

A[2, 0] = 7
A[2, 1] = 8
A[2, 2] = 9

A[3, 0] = 10
A[3, 1] = 11
A[3, 2] = 12

print('A = ', A)

#%%%
"""
We can do this with one loop like so 
"""

A = np.zeros((4,3))
for i in range(3):
    A[0,i] = i+1
    A[1,i] = i+4
    A[2,i] = i+7
    A[3,i] = i+10
print('A = ', A)

#%%
"""
We can use even less lines of code with what is called a nested loop,
which is a loop inside of a loop.  For example 
"""

A = np.zeros((4,3))
Avalue = 1 #initializer
for i in range(4):
    for j in range(3):
        A[i,j] = Avalue 
        Avalue = Avalue + 1 #overwrite the Avalue
        
print("A = ", A)

#%%
"""
Notice the indentation - it is very important. 
All the code in the first for loop is indented once 
(in this notebook, one indentation is four spaces). 
All the code in the second for loop is indented an additional time. 
When the loops are over, we return to the original indentation.

You should carefully study this example until you can clearly see why 
it creates the matrix we are looking for and what order everything 
happens in. In particular, it may help to have python print out the 
values of i, j and A_value at every step.
"""

A = np.zeros((4,3))
for i in range(4):
    for j in range(3):
        A[i,j] = (i+1)/(j+1)

print(A)


    





