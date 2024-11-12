#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 07:59:58 2024

@author: samvanfleet
"""

import numpy as np

"""
Throughout this class, and throughout applied mathematics in general, 
we frequently need to work with mathematical functions like

- f(x) = sin(x) or f(x) = ax^2 + bx + c.

for sin(x) we can use the predefined numpy sin function but we dont have
such a tool for polynomials or other functions.  For example when working 
with the Fibonacci sequence, we copy and pasted our code over and over. 
We can use functions in python to just write this code once and use it 
throughout our code.
"""

#%%
f = np.sin(x) #Error
#%%
f(x) = np.sin(x) #Error
#%%
"""
However this one will work
"""
f = np.sin

print(f(10))
print(f(np.pi))
#%%
"""
Before we talk about how to write a function, let's briefly review 
what they are and how to use them. Throughout this document, 
I will refer to functions in the numpy package as "python functions". 
As you know, in order to use those functions, you have to import the 
numpy package and then append the name of the function with np.. 
You have already seen quite a few python functions. 
For example, sin and cos are functions, as are append and print. 
Python functions are essentially just prewritten chunks of code 
that you can run by using their name. You can tell python to run a 
function by writing the name (possibly appended with a package name 
like np.) followed by parentheses and a list of some number of 
input values called "arguments". This process is known as "calling" 
the function. For example, the function print does not need any arguments, 
so you can call it by typing the name and a set of parentheses:
    
"""

print() #print with no arguments prints a blank line
#%%
"""
The function sin takes one argument (an angle in radians), 
so you can call it by typing the name and then a number in parentheses:
"""
x = np.sin(4)
print(x)
#%%
"""
The function append takes two arguments - an array and a number - 
and so you can call it by typing the name append, followed by 
parentheses enclosing an array and a number, each separated by a comma. 
For instance:
"""
y = np.array([1, 2, 3, 4])
print(y)
z = np.append(y, 5)
print(z)
#%%
"""
Some functions, like print, aren't really meant to return anything. 
If you try to use them in an assignment then you will get a value 
called None. We will mostly ignore that feature in this class.

Functions can only ever have one return value, 
although that value is allowed to be a list or array (or any other type).
"""
x = print("Some text")
print(x)
#%%
"""
To define your own functions, you need to specify the function name, 
any arguments and return values, as well as the code that python will 
run when the function is called. There are two different ways 
to write a function in python (well, there are several more 
related versions, but we will only use these two): 
Anonymous functions and normal functions. 
(The word "normal" is not part of the name. Somewhat ironically, python 
 doesn't have a name for non-anonymous functions. 
 If I need to specify non-anonymous functions, I will say so explicitly.) 
Each of these has slightly different syntax and can be used in slightly 
different ways.


The first type of function we will encounter is called an 
"anonymous function". You can define it with the following syntax:
    
function_name = lambda list_of_argument_names: one_line_of_code

For example we can write the anonymous function
"""

f = lambda x: 3 * x + 5
z = 4
y = 2

print("z = ", z," f(z) = ", f(z), " and y = ", y, " and f(y) = ", f(y))
#%%

"""
We can also use it in computations
"""
z = f(3) - f(2) + 3
print("z = ", z)
#%%
"""
There are a few important things to notice about this definition.

1) f is now a variable in memory. Its type is function, 
    which you can see with the type command.  
    
"""
print(type(f))
    
#%%
"""
2) x is not a variable in memory. (Actually, this may or may not be true
for you, because you might have already defined x somewhere else, 
but x does not have to be a variable. You can prove this to yourself
 by starting a blank script or a new console session, defining f as above
 and then trying to print the value of x.) This is very important - 
arguments like x can be used in the code for a function even though 
they are not already defined.


3) When you call a function, the argument you give in parentheses 
 is used as the value of x. For instance, if you write f(4), 
 then python will use 4 as the value of x.
 
4) The return value is whatever the one line of code evaluates to. 
If you write f(4), then the return value is 3 * 4 + 5, which is 17.
It is also worth noting that the function_name is optional 
(which is why these are called "anonymous"). 
It will occasionally be useful to create a function without actually 
naming it, such as
"""

print(lambda x: 3 * x + 5)

#%%
"""
The behavior of the argument x might seem particularly strange. 
As we already saw, neither defining nor calling this function defines 
a variable named x. What's more, if you try this code:
"""

x = 2
f = lambda x: 3 * x + 5
y = f(10)
print("x = " ,x)
print("y = ", y)

#%%

"""
you can see that defining/calling f does not affect any other variables 
named x. This is because the arguments of the function have something 
called local scope. The variable x from the definition of x can only 
be seen by python while python is running f, and this x will 
not interfere with any variables that aren't in the function body. 
In essence, python is giving f its own private section of memory whenever 
you call it. For instance, when python executes the line y = f(10) above, 
it will make a private section of memory for f with a variable named x 
that has the value 10. This private memory is completely separate from 
the memory for the rest of your script.

Other variables you define in your script (including the variable f itself) 
live in something called the global scope. As we have already seen, 
any code in your script can access and modify any other variables in 
the global scope. 

As a general rule, functions can see/access variables from the global scope, 
but they cannot modify those variables. As an example,
"""


a = 2
f = lambda x: a * x
print(f(3))

#%%

"""
The function f can access the variable a, and so we are allowed to 
use a in the function definition, even though it is not one of the arguments.
 It is important to note that f looks up the value of a every 
 time you call it. This means that if a changes, then the result of 
 future calls of f will also change.
"""

a = 2
f = lambda x: a * x
print(f(3))
#%%
a = 10
print(f(3))

#%%
"""
It's also worth noting that the name of the argument does not matter, 
as long as you are consistent. That is, if you use the name x in the 
argument list then you also need to use the name x when you refer to 
that argument in the function body. For example, the following are 
exactly equivalent:
"""
f = lambda x: 3 * x + 5
f = lambda z: 3 * z + 5
f = lambda this_is_a_silly_variable_name123: 3 * \
    this_is_a_silly_variable_name123 + 5
#using the \ allows multiline
#pythonstatments if there are no () or []

#%%

del y #This clears the variable y from memory.
"""
However, the line
"""
f = lambda x: 3 * y + 5

#%%
"""
will not do what you want. 
Python will happily define the function f without checking the value of y. 
When try to call f, python will check the global scope for a 
variable named y. If it exists, python will use that value in the 
expression 3 * y + 5, but if it does not exist then python will 
throw an error.

"""
#%%
print(f(2))

#%%

"""
It is also worth noting that you aren't restricted to just using hard 
coded numbers as arguments when you call a function. Anything that 
evaluates to a variable of the appropriate type (in most of our cases, 
the appropriate type is any numeric type like a float or an int) is fine. 
For instance,
"""

f = lambda x: 3 * x + 5
y = np.pi
print(f(y))

#%%
"""
We can also define functions with any number of arguments
"""
f = lambda x, y: x ** 2 + y
x = f(2,3)
print(x)
#%%
a = np.array([1.0,2,3])
b = np.array([2.0,3,4])

print(f(a,b))
#%%
a = "string 1"
b = "string 2"
print(f(a,b))


#%%
y = f(3,2)
print(y)
#%%
"""
Notice that the order of the argument matters. 
In the above example, the first argument of f is used as x and the 
second argument is used as y. 
That's why f(2, 3) and f(3, 2) are not the same.


How about a function with 6 arguments
"""
g = lambda a, b, c, x, y, z: a + 2 * b - c + x ** 2 - y ** 2 + 3 * z ** 3
print(g(1, 2, 3, 4, 5, 6))
#%%
"""
Or maybe one with no arguments?
"""
h = lambda : 2 * np.pi
h()

#%%

"""
Unfortunately anonymous functions are only limited to a single expression.


This distinction doesn't really matter to us, but it's worth noting
 that an assignment like x = 3 is not an expression,
 so you cannot use it in an anonymous function. 
In particular, you cannot include an if statement or a loop inside 
an anonymous function, because those require more than one line of code. 
If you want to use a more complicated function in one of your scripts,
 you can write a normal function.  Note we will now call normal functions 
 functions.

Function definitions have the following syntax:

def function_name(list_of_arguments):
    #code to run in the function
    return return_value


Our first example will be a function for the formula 
y = 2x^3 + 11
"""
def my_first_function(x):
    y = 2*x**3+11
    return y

#%%
"""
We can now call this function
"""
print(my_first_function(3))

#%%
"""
def and return are kywords/reserved words in python. The function 
definition must always start with a def and end with a :.
The function_name can be any legal python name 

All of the code in the function body, including the line with return, 
must be indented, just like in a loop or conditional statement.

The list_of_argument_names works exactly the same as in an anonymous function.
We have only used one variable here (x), but we can list as many 
as we want and separate them with commas. Just like with anonymous 
functions, these arguments exist in their own local scope 
(i.e., a private section of memory) and cannot be accessed or 
modified by any code outside of the function.

The return_value is an expression that evaluates to whatever you want
 the function to return. It is common to assign your return value
 to a variable and then use that variable name as the return_value,
 but you can put any expression you want after the return. For instance,
 we could rewrite the same function as
"""

def my_first_function(x):
    return 2 * x ** 3 + 11
    


print(my_first_function(3))

#%%
"""
You are technically allowed to put code in lines after the return, without 
an error but python will not run any code in a function 
after it encounters a return.


Because we have already seen this example, lets try to write our own 
absolute value function
"""

def my_abs(x):
    if x >= 0:
        abs_x = x
    else:
        abs_x = -x
    return abs_x

#%%

"""
Now that we have ran the cell above, lets try testing out our absolute
value function
"""

print(my_abs(-3))
#%%

"""
How about a function for our Fibonacci numbers example.  Here we will take 
three arguments:
    - F1 the first number in the sequence
    - F2 the second number in the Fibonacci sequence
    (These are usually both one but they can take on other values)
    - N will be the amount of Fibonacci numbers we want to calculate
"""


def first_N_fib(F1, F2, N):
    fib = np.zeros(N)
    fib[0] = F1
    fib[1] = F2
    
    for i in range(2,N):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib
#%%

print(first_N_fib(1, 1, 20))

#%%
N = 300
F1 = 1
F2 = 1

#%%

print(first_N_fib(F1,F2,N))

#%%

"""
We can also import functions from another python file.  This is 
useful if you find your self using a function in many different scrips and
you only want to write it once.  Also doing this reduces the chance for 
error or bu that comes from writing a function multiple times.

To do this you can use the code
"""

import fibonacci

x = fibonacci.fibonacci_function(1, 1, 10)

print(x)


#%%

"""
It's important to note that the import statement runs the entire file 
you are importing. In this case, the statement import fibonacci runs 
the entire file fibonacci.py. If fibonacci.py is nothing but function 
definitions, then this is probably exactly what you want, 
but if fibonacci is littered with print statements or other code, 
those will also be run.
"""
#%%

"""
Now that you can define your own functions, it is possible for you to 
define a function with the same name as a builtin python function. 
As a silly example, you could define your own function print with the code
"""

def print(x):
    return x**2

#%%

print(3)

#%%

print("some text")

#%%

"""
This is called shadowing or we say that we have shadowed the origional 
function.  It still exists, but we cannot access it because we 
took the name print and used it for something else.  Note you can also assign
print as a variable name.  
"""

print = 3


#%%

"""
It is advisable that you avoid shadowing to avoid confusion.  However if you 
need to clear a variable or function from memory in python you can use the 
keword del
"""

del print
#%%

print("now print() is back to normal")












