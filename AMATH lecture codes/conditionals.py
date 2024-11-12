#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 07:30:17 2024

@author: samvanfleet
"""


"""
An "if statement" is written by using the reserved word "if".  
These staments are useful if we want our code to behave differently 
in different situations.  For example, if we wanted to write a script
that calculates the absolute value of a number x, we would ask 
python to return 

- x if x is positive 
- and (-x) if x is negative 

In general if statments take the form 

if condition:
    # code that you would like to run when condition holds.
    
condition can be a variable and for the moment we will assume it is 
a bool variable.  Bool variables are a simple type of variable 
that are either True or False (These are also reserved words/keywords).

Before we get started with if statments, lets look at a few examples
of bool variables.
"""

x = True
print('x = ', x)
print('x is of type ', type(x))
#%%
y = False
print('y = ', y)
print('y is of type ', type(y))

#%%
"""
When python encounters an if satement, it evaluates the code 
in condition and then does one of two things. If condition is True, 
then python runs the indented code after the if statement, 
and then continues with any other un-indented code below. 
If condition is False, then python skips the indented code and goes 
directly to the un-indented code after the block.

For example
"""
x = True
print("The code before the if block is always run.")
if x:
    print("The code in the if block is run because x is True.")

print("The code after the if block is always run.")

#%%

y = False
print("The code before the if block is always run.")
if y:
    print("The code in the if block is not run because y is False.")

print("The code after the if block is always run.")

#%%

"""
To make use of this syntax, we have to know how to write code that
produces bool variables. Python has a handful of useful operators 
for this task. You are probably already very familiar 
with all of these.
"""

"""
The == operator checks if two values are equal. 
If they are equal, the entire expression evaluates to True. 
If they are not equal, the expression evaluates to False. 
For example,
"""

x = 3
y = 3
z = 2

print(x == y)

#%%

print(x == z)

#%%
"""
Notice that this is a double equals sign, not a single equals sign. 
The single equals sign is already used for assignment. 
It is very common to accidentally use assignment when you meant to 
use equality. For example, you might write
"""

if (x = z):
    print("x is equal to z")
    
#%%

if (x == z):
    print("x is equal to z")
    
if (x == y):
    print("x is equal to y")
    
#%%
"""
The > operator checks if the left value is greater than the 
right value. If the left value is greater, the expression evaluates
 to True. Otherwise, it evaluates to False.
"""

x = 3
y = 3
z = 4

print(z > x)

#%%
print(x > z)

#%%
print(x > y)

#%%
"""
The < operator checks if the left value is less than the right value.
If the left value is less, then the expression evaluates to True. 
Otherwise, it evaluates to False.
"""

x = 3
y = 3
z = 4

print(x < z)

#%%

print(z < x)

#%%

print(x < y)

#%%
"""
The >= operator checks if the left value is greater than or equal to 
the right value. If the left value is greater or equal, 
the condition evaluates to True. Otherwise, it evaluates to False.
"""

x = 3
y = 3
z = 4

print(z >= x)

#%%

print(x >= z)

#%%

print(x >= y)

#%%

"""
The <= operator checks if the left value is less or equal to the right 
value. If the left value is less or equal, the condition evaluates 
to True. Otehrwise, it evaluates to False.
"""

x = 3
y = 3
z = 4

print(x <= z)

#%%

print(z <= x)

#%%

print(x <= y)

#%%

"""
Now that we know some more about bool variables lets write some code
that calculates the absolute value of x
"""

x = 10 #value we wish to determine the absolute value of

if x>= 0:
    absolute_value_of_x = x
if x < 0:
    absolute_value_of_x = -x
print("The absolute value of x is: ")
print(absolute_value_of_x)

#%%

x = -5
if x >= 0:
    absolute_value_of_x = x
if x < 0:
    absolute_value_of_x = -x
print("The absolute value of x is: ")
print(absolute_value_of_x)

#%%

"""
Notice that we had two mutually exclusive conditions in this code 
(either x is non-negative or it is negative, but not both) 
and we wanted to run different code in either case. 
Our solution is ok, but this comes up so often that python has a 
shortcut: The else statement. In general, 
else statements work like this:
    
if condition:
    #code to run if condition is true
    
else:
    #code to run if condition is false
    
Using this we can write our absolute value code as 
"""

x = -12
if x >= 0:
    absolute_value_of_x = x
else:
    absolute_value_of_x = -x
print("The absolute value of x is: ")
print(absolute_value_of_x)

#%%

"""
This version is easier to read and debug, but it is also faster. 
That is because python only has to check one condition instead of 
evaluating both x >= 0 and x < 0.


There is actually one more level of generality for if statements. 
If we have more than two cases, but we only ever want to run one 
block of code, we can use the keyword elif. 
The general case looks like this:
    
if condition_0:
    #code block 0
    
elif condition_1:
    #code block 1

...
elif condition_n:
    #code block n
    
else:
    code block n+1
    
    
When python encounters a block like this, it checks each of the 
conditions in turn. The first time it encounters a condition that 
evaluates to True, python executes the corresponding indented block 
of code and then skips directly to un-indented code after the block. 
If all of the conditions evaluate to False, then python executes 
the last block of code (after the else) and then goes on to any 
un-indented code below. You can use as many elif statements as 
you want after an if, but only one else. For example:
"""

x = -1
y = -2

if y > x:
    print("y is greater than x")
elif y == x:
    print("y is equal to x")
elif y < 0:
    print("y is negative and less than x")
else:
    print("None of those conditions were true")
    


#%%

"""
There are two very common ways to combine conditions, 
the and operator and the or operator. The and operator evaluates 
to True if both the left and right value are True and 
evaluates to False otherwise. For instance,
"""
print(True and True)
#%%
print(True and False)
#%%
print(False and True)
#%%
print(False and False)
#%%
x = 5
y = 5
print(y == x and y < x)
#%%
"""
The or operator evaluates to True if the left or right value (or both) 
are True and it evaluates to False otherwise. For instance,
"""
print(True or True)
#%%
print(True or False)
#%%
print(False or True)
#%%
print(False or False)
#%%
x = 5 
y = 5
print(x > y or x < y)
#%%
"""
The not operator flips the value of a bool. That is, 
not True is False and not False is True.
"""
print(not True)
#%%
print(not False)




















