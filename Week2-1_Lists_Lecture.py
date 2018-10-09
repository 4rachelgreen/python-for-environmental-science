# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Name:         Week2-1_Lists_Lecture.py
# Purpose:      Example and Notes for Lists
#
# Compatibility: Python 3.5
#
# Author:       James Dietrich, Dartmouth College
#               james.t.dietrich@dartmouth.edu
# Created:      Mon Nov 14 15:02:12 2016
# Copyright:    (c) James Dietrich 2015
# Licence:      MIT
#
#------------------------------------------------------------------------------
#%

# LISTS

# LISTS - containers for multiple values

num_list = [1,2,3,4,5,6,7,8,9]

str_list = ["me", "myself", "i"]

mixed_list = [1,2,"three",4,"five"]   # not ususally recommended

# Instead of using mixed lists, use two lists- one with names, the other with values.

# List indexing - same as string indexing - start from zero

#       num_list = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
# index            < 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 >
# rev index        < -9, -8, -7, -6, -5, -4, -3, -2, -1>

#       str_list = ["me", "myself", "i"]
# index            [  0 ,    1    ,  2 ]
# rev index        [ -3 ,   -2    ,  -1]

num_list[3]     # one value
num_list[-2]    # from the end
num_list[3:5]   # range
num_list[3:]    # all values after and index

# selecting a range of values (slicing)
# index range (exclusive, does not include the last index)
num_list[0:3]

# ??? print the values 4,5,6,7 from num_list
<<<<<<< Updated upstream
num_list[3:7]
num_list[-6,-2]  # smae thing, just using the reverse case
=======
print(num_list[3:7])
print(num_list[-6:-2])
>>>>>>> Stashed changes

# every nth value - list[start:end:step]
num_list[1:-1:2]

# ??? odd numbers
num_list[0:9:2]
num_list[0::2]

#List length
len(str_list)

# reassigning
str_list[2] = "giraffe"


#%%------
# TUPLES - lists that cannot be changed after they are created
# created with Parentheses ()

# Probably most useful for storing constants in scripts...  otherwise, pretty useless

my_tup = ("one","two", "three")
my_tup.

my_tup[2] = 4.5

#%%
# List methods

colors = ['red', 'blue', 'green', 'black', 'white']

# add element at the end
colors.append('pink')

# insert(index, value)
colors.insert(4,"PURPLE")

# ??? add the value "Cyan" at the begining of the list
colors.insert(0, 'cyan')

# delete element with index (or transfer out)
colors.pop()        # removes last element
colors.pop(2)       # removes element in index

# remove with delete (del) command
del(colors[2:4])

# remove element that match query
# * only removes the first element that matchs
colors = ['red', 'blue', 'green', 'black', 'white', 'red']
colors.remove('red')

# sorting in place
# default is assending
colors.sort()

# decending w/ sort option
num_list.sort(reverse=True)

# sorting to a new variable
rand_list = [ 5.1 , 3.42 , 3.333 , 100.4 , 0.5 , 26.0 , 7.44 , 5.8 , 39.0 ]

# ??? create two new variables, 1) sorted ascending 2) sorted descending
rand_list_asc = sorted(rand_list)
rand_list_asc = sorted(rand_list, reverse = True)

#%%

# CONSTRUCTING SEQUENTIAL LISTS

# using the RANGE function
# range(start, stop[, step])  **stop value is exclusive
my_list  = range(1,10)

print(my_list)

# we need to tell Python to make a list from the range object...
my_list  = list(range(1,10))
print(my_list)

my_list_float  = list(range(1.0,10.))

# ??? construct a list with steps of 100 from 0 - 1000
my_list_2 = list(range(0, 1001, 100))


#%%

# LISTS of LISTS

# Lists of lists are indexed separately
multi_list = [[1,2,3],['a','b','c']]    

list_1 = [1,2,3]
list_2 = ['a','b','c']

list_merge = list_1 + list_2

list_merge2 = [list_1,list_2]   # Same as multi_list

# splicing
# list[index1][index2]

print(multi_list[1][2])

# ??? extract the value 2 & 3 from the list
print(multi_list[0][1:3])

#%%

# LIST MATH

list_add = rand_list[4] + rand_list[-1]
print(list_add)

# from our euclidean distance example from last lecture
# use list math to rewrite the distance equation with list inputs

#        [ x ,  y ]
pt_one = [3.4, 9.0]
pt_two = [-2.3,-5.5]

# ??? math...


#%%

# LIST COPYS
# copying lists can be tricky

colors = ['red', 'blue', 'green', 'black', 'white']

# Creating a new variable that equals the list is a view, not a true copy.
colors_copy = colors

colors_copy[3] = "gray"

# To make a true, independent copy

colors = ['red', 'blue', 'green', 'black', 'white']

colors_copy = colors.copy()
# or
colors_copy = colors[:]
# or
colors_copy = list(colors)




