import numpy as np

# reminder, this is an array:
one_d = np.array([1,2,3,4,5])
# you can not change the size/shape of an array
# arrays all have one data type 

# you might remember that arrays have a shape: 
one_d.shape

# we are going to create our first 2-D array
two_d = np.array(
    [[1,2,3],
     [4,5,6]]
)

print(two_d)
# there are two lines corresponding to the number of sublists
# and three columns, corresponding to the number of elements in each sublist
# if the sublists did not have the same number of sublists
# you'll get an error

# now we have a 2d array, let's review the shape
print(two_d.shape)
# with a matrix, the first element of the shape is always the number of ROWS
# the second is always the number of COLUMNS

# A 2D array is... an array!
print(type(two_d))
print(type(one_d))
# an array of multiple dimensions will work in an extremely similar fashion to 1D
# one term you might see:
# 1D array is a VECTOR
# 2D array is a MATRIX
# a single element is a scalar (just a single number/value)

# ok, so if 2D arrays are array, we can probably index them
# let's see how that works: 
print(two_d[0]) # returns the first row of the array, which has the data type array
print(two_d[-1]) # returns the last row 

# we can also do slices on 2d arrays:
print(two_d[0:2]) # the first two rows of my matrix
print(two_d[0:1]) # when you ask for a slice, you're going to get a matrix

print(one_d[0]) # this returns one element (scalar)
print(one_d[0:1]) # this returns an array
print(two_d[0]) # this returns an array
print(two_d[0:1]) # this returns a matrix
# when you slice an array, you get an array. when you index an array, you get a scalar
# when you slice a matrix, you get a matrix. when you index a matrix, you get a vector

# indexing columns:
print(two_d[0,0]) # first number is rows, second number is columns
print(two_d[0,2])
print(two_d[-1,-1])

# what if you want ALL of the rows? 
print(two_d[:,1])
print(two_d[:, 0:2])

two_d = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)

# exercise 1: using indexing, replace the element 5 by 999
two_d[1,1] = 999
print(two_d)

# exercise 2: replace the final column by [7,14,21]
two_d[:, 2] = [7, 14, 21] # could do -1 instead of 2, since the language was "final"
print(two_d)

# final exercise: double the values in the first row
two_d[0, :] = two_d[0, :]*2
print(two_d)

two_d = np.array([
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
])

# exercise 4: replace all the negative values in the matrix by 0s
# a) write a mask matrix that contains true where all negatives are in 2d
# b) use the mask to print all these negative values
# c) use the mask to replace the negative values by 0s

mask = two_d < 0
print(mask)
two_d[mask] # this does not index to a matrix because the other items have been erased
two_d[mask] = 0
print(two_d)

# we already saw on tuesday that the main benefits of arrays is that you can 
# add, multiply, divide, or subtract them, as long as they have compatible shapes
# the same is true for matrices

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [1,1],
    [2,4]
])

print(a+b)
print(a-b)
print(a/b)
print(a*b)

# one final matrix concept:

# 2D arrays have the same methods as 1D arrays, with a very small twist

units_sold = np.array([
    # how many items of products a,b,c were sold in months
    # january through april
    [120, 150, 130, 170],
    [75, 60, 90, 80],
    [300, 330, 310, 350]
])

print(units_sold)
# you probably remember that arrays have methods like sum(), mean(), min(), max:
# what happens if we do 
units_sold.mean() # this is the mean of the whole shebang (grand mean)
# the mean of all sales across all products and months

# when you have matrix data, it can be nice to get the means by rows or columns
# methods have a magic keyword called axis
# axis tells you what axis is being summarized on 
print(units_sold.mean(axis=0)) #average sale at the month level (4)
# if instead we do
print(units_sold.mean(axis=1)) #average sale at the product level (3)
# the axis specifices the axis that will disappear 
# upon which the method will be applied

# exercise 1: the method min() gives the minimum of an array. use this method
# to find the smallest amount sold across the four months for each product
print(units_sold.min(axis=1)) 
# we want this at the product level
# the axis associated with products is rows (1)

# exercise 2: find the largest sale generated for ANY product across the four months
print(units_sold.max()) # grand max over all dimensions

# find the largest sale for product A
print(units_sold[0,:].max())
# index for the first row, all columns

