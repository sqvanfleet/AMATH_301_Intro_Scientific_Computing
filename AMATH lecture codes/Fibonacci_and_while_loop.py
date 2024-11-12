#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 07:38:37 2024

@author: samvanfleet
"""

#%%
"""
As an example coding exercise, we will try to calculate some 
Fibonacci numbers.  The Fibonacci numbers are a sequence defined by 
the recurrence relation:
    F_n = F_{n-1} + F_{n-2},
    
    where F_1 = 1 and F_2 = 1.
    
In other words, the next Fibonacci number is found by adding the previous 
two.  LLets start by computing the first 20 Fibonacci numbers.
"""
import numpy as np
N = 20 # We want to compute the first 20 Fibonacci numbers

fib = np.zeros(N)
print(fib)

fib[0] = 1;
fib[1] = 1;

print(fib)
#%%
"""
Now that we have initialized we need to create our loop.
"""

for i in range(2,N):
    fib[i] = fib[i-1] + fib[i-2]
    
print("The first ", N, "Fibonacci numbers are \n", fib)

#%%
"""
Now lets ask python to compute the first 200 Fibonacci numbers.
"""
N = 200

fib = np.ones(N) #Another way to initialize for this example

for i in range(2,N):
    fib[i] = fib[i-1] + fib[i-2]
    
print("The", N, "th Fibonacci number is \n", fib[-1])
#%%
"""
Suppose that we now want to calculate all of the Fibonacci numbers that are
less than a certain number (lets say 1,000,000) for our example.  We can use 
an if statment to tell python to stop our loop if any of the Fibonacci numbers 
become larger than 1,000,000. (using the keyword break)


Lets use our above Fibonacci code
"""

N = 20

fib = np.ones(N) #Another way to initialize for this example

for i in range(2,N):
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] >= 1000000:
        break #tells python to stop whatever loop it is running
    
print("The first ", N, "Fibonacci Numbers are: \n", fib)

#%%
"""
It appears that the first 20 Fibbonacci numbers are not larger than 1,000,000.
We can increase the value of N to 200
"""
N = 200

fib = np.ones(N) #Another way to initialize for this example

for i in range(2,N):
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] >= 1000000:
        break #tells python to stop whatever loop it is running
    
print("The first ", N, "Fibonacci Numbers are: \n", fib)

#%%
"""
It turns out that there are only 30 Fibonacci numbers less than 1,000,000.
How can we get rid of all of the extra numbers?

One way is to use the loop variable which is still defined when the loop 
is finished.
"""
print("the loop variable i = ", i)

#%%
"""
Notice that the way our if statment was constructed, the array fib has one
extra number that is over 1,000,000.
"""
print("fib[i-1] = ", fib[i-1])
print("fib[i] = ", fib[i])

#%%
"""
We can use an array slice to cut off all the values we dont want.
"""
N = 200

fib = np.ones(N) #Another way to initialize for this example

for i in range(2,N):
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] >= 1000000:
        break #tells python to stop whatever loop it is running


fib = fib[:i]
print("The first ", i, "Fibonacci Numbers under a 1,000,000 are: \n", fib)
print(fib.shape)
#%%
print("There are ", fib.shape[0], "Fibonacci numbers under 1,000,000")


#%%
"""
Python actually has another type of loop called the while loop. 
The general syntax for a while loop is 

    while condition:
        # code in the while loop 
    
When python encounters a while loop, it checks to see if the condition
 is True. If it is, then python runs the indented block of code. 
 Python then returns to the top of the while loop and starts over. 
 If the condition is ever False, then python will instead skip to the 
 next line of un-indented code.
 
So another way to write our Fibonacci code is:
"""

fib = np.zeros(2)
fib[0] = 1
fib[1] = 1

while fib[-1] < 1000000:
    fib = np.append(fib, fib[-1] + fib[-2])
    
fib = fib[:-1]
print(fib)

#%%
"""
There is one very important point that you have to keep in mind when 
working with while loops. It is possible that the condition in your 
loop never becomes False. If this happens, then the loop will just 
repeat forever and your code will never stop running. As a silly example, 
this code prints the number 1 forever:
"""
while True: 
    print(1)

"""
To stop an infinate loop in Spyder, click anywhere in the python console and
then hit "control + c".
"""













