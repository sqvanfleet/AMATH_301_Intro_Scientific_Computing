#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:12:00 2024

@author: samvanfleet
"""

"""
Lecture 1-17-2024 
We are using blocks for this lecture script
"""
#%%
"""
In Python and other programming languages we have pointers 
for variable assignments, which basically allows you to use 
a single spot in memory for multiple variables. 
This won't be an issue for single variables, 
but will be an issue for lists and arrays. For example
"""
import numpy as np


A = np.array([[1,1],[1,1]])
print("A = ", A, "\n") #here is another way to concatanate A 
# to a string in a print statement.  Also the "\n" creates
# a line break.

A1 = A
#%%
A1[0,1] = 2
print("A1 = ", A1)
print("A = ", A)

#%%
"""
If we use copy(), we can change A1 without changing A
"""
A = np.array([[1,1], [1,1]])
print("A = ", A, "\n") # '\n' adds a linebreak
#%%
A1 = A.copy()
A1[0,1] = 2
print("A1 = ",A1)
print("A = ", A)

"""
When in doubt .copy() it out.
"""
#%%
"""
Let us move on to creating graphs in python.
As an example, let's start by trying to plot the curve
y = x^2 - 3.

Python creates plots by taking a list of x values and a list of 
y values, then plots each point (x,y) and then connects the dots.

For our list of x values we can use either a 1D array or a column
vector represented as a 2D array. 

However we cant use a row vector.
"""

"""
We could use np.linspace() to create our 1D array
"""
x = np.linspace(-2,3,10) #1D array of 10 equally spaced numbers 
#between -2 and 3.

print("x = ", x)
#%%

"""
We could also use np.arrange() to create our 1D array
"""

x = np.arange(-2,3.5,.5)
print("x = ", x)
#%%
"""
Using either of the blocks above to create x, we can now use it
to create y.
"""
y = x**2-3
print("x = ", x)
print("y = ", y)
#%%
import matplotlib.pyplot as plt
"""
Importing matplotlib.pyplot allows us to use all of it's 
plotting tools.  Anytime you wish to use python to plot you 
need to import this package.
"""

"""
In general, plt.plot(array_of_x_values, array_of_y_values)
creates a plot of array_of_x_values vrs array_of_y_values.
For examle from the cells above we have x and y and we can 
plot them
"""
plt.plot(x,y) #creates the plot which appears in the plots page

plt.show(plt.plot(x,y)) #shows the plot in the console if you are 
#not using Spyder

#%%

"""
We can modify the appearance of this graph in many different ways.
For example, we might want to change the color of the line. 
There are two ways to do so. First, python has several shortcuts 
for colors. For example, "k" stands for black, 
"b" stands for blue and "r" stands for red. 
(You can nd a list of all of these shortcuts in the 
documentation for plot.) If we wanted a red curve, we could use
"""

plt.plot(x,y, "r") 
#%%
"""
Another option is 
"""
plt.plot(x, y, color="r")

#%%

"""
You can also change the line style 
(for instance, dotted lines, dashed lines, etc.) 
There are shortcut symbols for all of these. You do
not need to memorize the symbols since
you can look them up in the python documentation 
for plot whenever necessary. As an
example, the shortcut ":" stands for dotted line, 
so you can use
"""

plt.plot(x,y,":") #creates a plot with a dotted line
#%%
"""
Another option for this is 
"""
plt.plot(x, y, linestyle=":")


#%%
"""
For a red dotted curve we can combine the shortcuts
"""

plt.plot(x,y,"r:")

#%%

"""
We can change the shape of the markers (the points (x,y)) 
"""
plt.plot(x,y,"o") 

#%%

"""
We can combine shortcuts 
"""

plt.plot(x, y, "k:o") #black dotted line with "o" markers

#%%
"""
There are lots of things we can modify but they may not have 
shortcuts.  For example the linewidth option allows you to 
modify the width of the line
"""

plt.plot(x,y,linewidth=10)


#%%

"""
Lets make a plot with a lot of options 
"""

plt.plot(x, y, color="m", 
                 linestyle="--", linewidth=3, marker="+")

#%%
"""
You can also customize the rest of the graph as well.
We will only look at a few of the simplest options here, 
but I strongly encourage you to explore the python 
documentation and see how to change other features.
"""

plt.plot(x, y, "r")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of a parabola")

#%%
"""
We can put multiple curves on one plot.
Lets plot y = x^2 - 3 and y = x^3 + 2x - 5 on one plot
"""

x = np.arange(-2, 3.5, 0.5)
y = x ** 2 - 3
z = x ** 3 + 2 * x - 5
plt.plot(x, y, "r")
plt.plot(x, z, "k")

#%%
"""
It is also possible to combine both into a single plot command.
The general syntax is plt.plot(x1, y1, options, x2, y2, options). 
For example,
"""
plt.plot(x, y, "r", x, z, "k")

#%%
"""
If you include multiple curves on the same plot like this, 
it is always good practice to add a legend so that r
eaders will be able to understand your graph. 
You can do so with the legend command, which is also part 
of pyplot. The syntax is plt.legend((label1, label2, ...)),
where each label is encased in quotation marks. 
The labels should go in the same order that you made the plots. 
For example,
"""
plt.plot(x, y, "r")
plt.plot(x, z, "k")
plt.legend(("Quadratic", "Cubic"))

#%%
"""
Notice that the call to legend requires two sets of parentheses,
unlike most of the other commands we've seen. 
(We'll talk about why when we learn how to define functions.)

In this case, the legend is in a pretty good location, 
but often python will put it somewhere you don't want, 
such as covering up one of the curves. You can manually 
adjust the position with the following syntax:
"""

plt.plot(x, y, "r")
plt.plot(x, z, "k")
plt.legend(("Quadratic", "Cubic"), loc="upper center")


#%%

"""
If you want different graphs on different figures, 
you can open a new figure window with the figure command. 
The syntax is plt.figure(figure_number). 
For example,
"""

plt.figure(1)
plt.plot(x, y, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("quadratic")

plt.figure(2)
plt.plot(x, z, "k")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic")








